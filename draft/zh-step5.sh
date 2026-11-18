#!/bin/bash
# Step 5 for one year, run as a queue "cmd" line (one Haiku call at a time): post.py --units, repair.py, post.py.
# Usage (from pilot_translation/): bash ../one-physics-book/draft/zh-step5.sh <repo-dir> <year>
repo=$1 y=$2; subj=${repo#one-}; subj=${subj%-book}; R=../$repo; RUN=$R/draft/pilot-$y-zh
case $y in grade-[1-5]) d="primary school $subj textbook (${y/grade-/grade }, young children)";;
  grade-[6-9]) d="middle school $subj textbook (${y/grade-/grade })";; grade-1[0-2]) d="high school $subj textbook (${y/grade-/grade })";;
  bachelor-*) d="university $subj textbook (year ${y#bachelor-} of a $subj bachelor)";; esac
python3 post.py --repo $R --year $y --lang zh --units > $RUN/post1.log 2>&1
python3 repair.py --repo $R --year $y --lang zh --book-desc "$d" > $RUN/repair.log 2>&1
python3 post.py --repo $R --year $y --lang zh --units > $RUN/post.log 2>&1
