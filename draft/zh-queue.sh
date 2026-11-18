#!/bin/bash
# Haiku queue for the physics + chemistry zh pilot run (2026-11-18): one global queue so that at most three run.py
# jobs (years) run at once across both repos, --workers 3 each (9 calls in flight). Jobs come from draft/zh-queue.list,
# one "<repo-dir> <year>" per line, read as the queue advances, so chemistry's years can be appended later; a line
# "END" ends the queue. Each year is re-run up to PASSES passes until it reports 0 rejected sections. Waits on PIDs,
# never pgrep. Before each launch it reads the weekly plan and stops launching at CAP % (run's pause rule: +25 points
# from 9 % = 34 %). Logs: <repo>/draft/pilot-<year>-zh/run.log; this queue: draft/zh-queue.log.
cd /home/bvirrion/repositories/one-course/pilot_translation || exit 2
LIST=../one-physics-book/draft/zh-queue.list
CAP=${CAP:-34}
desc() { local subj=$1 y=$2; case $y in
  grade-[1-5]) echo "primary school $subj textbook (${y/grade-/grade }, young children)";;
  grade-[6-9]) echo "middle school $subj textbook (${y/grade-/grade })";;
  grade-1[0-2]) echo "high school $subj textbook (${y/grade-/grade })";;
  bachelor-*) echo "university $subj textbook (year ${y#bachelor-} of a $subj bachelor)";;
esac; }
usage() { timeout 120 claude -p /usage --tools '' 2>/dev/null | grep -o 'all models): [0-9]*' | grep -o '[0-9]*$'; }
one() {
  local repo=$1 y=$2 subj=${1#one-}; subj=${subj%-book}
  local R=../$repo RUN=../$repo/draft/pilot-$y-zh
  mkdir -p $RUN
  for pass in $(seq 1 ${PASSES:-5}); do
    python3 run.py --repo $R --year $y --lang zh --workers ${W:-3} --book-desc "$(desc $subj $y)" >> $RUN/run.log 2>&1
    tail -1 $RUN/run.log | grep -q "0 with a rejected section; 0 stopped" && { echo "$(date +%m-%d\ %H:%M) $repo $y done (pass $pass)"; return; }
    tail -1 $RUN/run.log | grep -q " 0 stopped" || sleep 600
  done
  echo "$(date +%m-%d\ %H:%M) $repo $y NOT CLEAN after ${PASSES:-5} passes"
}
pids=(); i=0
while true; do
  line=$(sed -n "$((i+1))p" $LIST)
  [ "$line" = "END" ] && break
  if [ -z "$line" ]; then sleep 120; continue; fi        # waiting for lines to be appended
  while [ ${#pids[@]} -ge 3 ]; do
    wait -n; alive=(); for p in "${pids[@]}"; do kill -0 $p 2>/dev/null && alive+=($p); done; pids=("${alive[@]}")
  done
  u=$(usage); if [ -n "$u" ] && [ "$u" -ge "$CAP" ]; then echo "$(date +%m-%d\ %H:%M) weekly plan at $u % >= $CAP %: PAUSED before $line"; break; fi
  set -- $line; one $1 $2 & pids+=($!); echo "$(date +%m-%d\ %H:%M) started $line (plan $u %)"
  i=$((i+1))
done
wait
echo "$(date +%m-%d\ %H:%M) queue finished"
