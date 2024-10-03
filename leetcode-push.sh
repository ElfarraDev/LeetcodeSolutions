#!/bin/bash

if [ $# -ne 4 ]; then
    echo "Usage: $0 <filename> <language> <topic> <difficulty>"
    echo "Example: $0 0001_two_sum.py python arrays easy"
    exit 1
fi

filename=$1
language=$2
topic=$3
difficulty=$4

problem_info=$(echo $filename | sed -E 's/([0-9]+)_(.+)\..+/\1 \2/')
problem_number=$(echo $problem_info | cut -d' ' -f1)
problem_name=$(echo $problem_info | cut -d' ' -f2-)

folder="$language/$topic/$difficulty"
mkdir -p "$folder"
mv "$filename" "$folder/"

git add .
git commit -m "LeetCode $problem_number: $problem_name ($language, $topic, $difficulty)"
git push origin main

echo "Successfully pushed $filename to GitHub in $folder!"
