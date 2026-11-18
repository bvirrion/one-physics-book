#!/bin/bash
# Haiku queue v4 for the physics + chemistry zh pilot run (2026-11-18), replacing v3, which read its next line BEFORE waiting for a slot (an edit to that line came too late: grade-7 ran twice, a cmd line was skipped); v3 replaced v2 only to add "cmd" lines; v2 replaced zh-queue.sh, which slept 10 min after
# every pass with a rejected section (it read the last log line, "Not finished...", for " 0 stopped"). One global queue:
# at most three run.py jobs at once across both repos, --workers W (3) each, so 9 Haiku calls in flight. Jobs come from
# draft/zh-queue4.list, one "<repo-dir> <year> [chapter ...]" per line, read as the queue advances; "END" ends it.
# A year is re-run up to PASSES (3) passes while it has rejected sections; what survives is hand-finished (fixsec.py).
# Sleeps 10 min only after a pass with a failed call. Waits on PIDs, never pgrep. Reads the weekly plan before each
# launch and stops launching at CAP % (pause rule: +25 points from 9 % = 34 %). Log: draft/zh-queue4.log.
# A line "cmd <shell command>" (run from pilot_translation/) takes one job slot: repair.py makes one Haiku call at a
# time, so a slot of 3 is never exceeded. Arguments: PIDs already holding slots (an earlier queue's year jobs).
cd /home/bvirrion/repositories/one-course/pilot_translation || exit 2
LIST=../one-physics-book/draft/zh-queue4.list
CAP=${CAP:-34}
desc() { local subj=$1 y=$2; case $y in
  grade-[1-5]) echo "primary school $subj textbook (${y/grade-/grade }, young children)";;
  grade-[6-9]) echo "middle school $subj textbook (${y/grade-/grade })";;
  grade-1[0-2]) echo "high school $subj textbook (${y/grade-/grade })";;
  bachelor-*) echo "university $subj textbook (year ${y#bachelor-} of a $subj bachelor)";;
esac; }
usage() { timeout 120 claude -p /usage --tools '' 2>/dev/null | grep -o 'all models): [0-9]*' | grep -o '[0-9]*$'; }
one() {
  local repo=$1 y=$2; shift 2; local subj=${repo#one-}; subj=${subj%-book}
  local R=../$repo RUN=../$repo/draft/pilot-$y-zh ch=""; [ $# -gt 0 ] && ch="--chapters $*"
  mkdir -p $RUN
  for pass in $(seq 1 ${PASSES:-3}); do
    python3 run.py --repo $R --year $y --lang zh --workers ${W:-3} $ch --book-desc "$(desc $subj $y)" >> $RUN/run.log 2>&1
    last=$(grep "^written" $RUN/run.log | tail -1)
    echo "$last" | grep -q "s; 0 with a rejected section; 0 stop" && { echo "$(date +%m-%d\ %H:%M) $repo $y $* done (pass $pass)"; return; }
    echo "$last" | grep -q " 0 stopped" || sleep 600
  done
  echo "$(date +%m-%d\ %H:%M) $repo $y $* NOT CLEAN after ${PASSES:-3} passes: $(echo $last | cut -c1-80)"
}
pids=("$@"); i=0
while true; do
  while true; do
    alive=(); for p in "${pids[@]}"; do kill -0 $p 2>/dev/null && alive+=($p); done; pids=("${alive[@]}")
    [ ${#pids[@]} -lt 3 ] && break; sleep 20
  done
  line=$(sed -n "$((i+1))p" $LIST)      # read only once a slot is free: every line not yet started can be edited
  [ "$line" = "END" ] && break
  if [ -z "$line" ]; then sleep 120; continue; fi
  u=$(usage); if [ -n "$u" ] && [ "$u" -ge "$CAP" ]; then echo "$(date +%m-%d\ %H:%M) weekly plan at $u % >= $CAP %: PAUSED before $line"; break; fi
  set -- $line
  if [ "$1" = cmd ]; then
    ( bash -c "${line#cmd }"; echo "$(date +%m-%d\ %H:%M) cmd done (exit $?): ${line#cmd }" ) & pids+=($!)
  else
    one $line & pids+=($!)
  fi
  echo "$(date +%m-%d\ %H:%M) started $line (plan $u %)"
  i=$((i+1))
done
wait
echo "$(date +%m-%d\ %H:%M) queue finished"
