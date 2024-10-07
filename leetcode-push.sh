#!/bin/bash

# Function to update README.md
update_readme() {
    local total=$1
    local easy=$2
    local medium=$3
    local hard=$4
    local filename=$5
    local topic=$6
    local difficulty=$7

    if [ ! -f "README.md" ]; then
        echo "Error: README.md not found. Please create a README.md file in the repository root."
        exit 1
    fi

    # Update the problem count
    sed -i '' "s/Total LeetCode problems solved: .* - Easy: .* - Medium: .* - Hard: .*/Total LeetCode problems solved: $total - Easy: $easy - Medium: $medium - Hard: $hard/" README.md

    # Add the new problem to the table
    if [ -n "$filename" ]; then
        problem_number=$(echo $filename | cut -d'-' -f1)
        problem_name=$(echo $filename | sed -E 's/[0-9]+-(.+)\.py/\1/' | tr '-' ' ' | sed 's/\b\(.\)/\u\1/g')
        echo "| $problem_number | $problem_name | [Python](./python/$topic/$difficulty/$filename) | $topic | $difficulty |" >> README.md
    fi

    echo "Updated README.md with new problem counts and details."
}

# Function to validate filename format
validate_filename() {
    if ! [[ $1 =~ ^[0-9]{4}-[a-z0-9-]+\.py$ ]]; then
        echo "Error: Filename must be in the format XXXX-problem-name.py (e.g., 0036-valid-sudoku.py)"
        exit 1
    fi
}

# Function to push changes to GitHub
push_to_github() {
    local problem_number=$1
    local problem_name=$2
    local language=$3
    local topic=$4
    local difficulty=$5

    git add .
    git commit -m "Add solution for LeetCode $problem_number: $problem_name ($language, $topic, $difficulty)"
    git push origin main
    echo "Changes pushed to GitHub."
}

# Check if correct number of arguments is provided
if [ $# -lt 3 ] || [ $# -gt 5 ]; then
    echo "Usage: $0 <filename> <topic> <difficulty> [needs_review] [\"reflection\"]"
    echo "  or   $0 <filename> -unr yes|no"
    echo "  or   $0 <filename> -ur \"reflection\""
    echo "Example: $0 0036-valid-sudoku.py array medium"
    echo "         $0 0036-valid-sudoku.py array medium yes \"Used hash set for each row, column, and 3x3 box\""
    echo "         $0 0036-valid-sudoku.py -unr yes"
    echo "         $0 0036-valid-sudoku.py -ur \"Optimized solution using bitmasking\""
    exit 1
fi

filename=$1
validate_filename "$filename"
flag=${2:-}

# CSV log file
log_file="leetcode_log.csv"

# Create the CSV file if it doesn't exist or if it's empty
if [ ! -f "$log_file" ] || [ ! -s "$log_file" ]; then
    echo "Problem Number,Problem Name,Language,Topic,Difficulty,Link,Needs Review,Date Completed,Reflection" > "$log_file"
fi

# Extract problem info from filename
problem_number=$(echo $filename | cut -d'-' -f1)
problem_name=$(echo $filename | sed -E 's/[0-9]+-(.+)\.py/\1/')

# Determine language (always python in this case)
language="python"

update_csv() {
    local field=$1
    local new_value=$2
    awk -F, -v OFS=',' -v pnum="$problem_number" -v field="$field" -v val="$new_value" '
    $1 == pnum {$field = val}
    {print}
    ' "$log_file" > temp.csv && mv temp.csv "$log_file"
}

if [ "$flag" = "-unr" ]; then
    # Update the 'Needs Review' status
    if [ "$3" != "yes" ] && [ "$3" != "no" ]; then
        echo "Error: -unr flag must be followed by 'yes' or 'no'."
        exit 1
    fi
    update_csv 7 "$3"
    echo "Updated 'Needs Review' status for problem $problem_number to $3."
    push_to_github $problem_number $problem_name $language "N/A" "N/A"
elif [ "$flag" = "-ur" ]; then
    # Update the reflection
    if [ -z "$3" ]; then
        echo "Error: -ur flag must be followed by a reflection in quotes."
        exit 1
    fi
    update_csv 9 "$3"
    echo "Updated reflection for problem $problem_number."
    push_to_github $problem_number $problem_name $language "N/A" "N/A"
else
    # Add new entry or update existing one
    topic=$2
    difficulty=$3
    needs_review=${4:-no}  # Default to 'no' if not provided
    reflection=${5:-"Initial solution"}  # Default to 'Initial solution' if not provided
    link="https://leetcode.com/problems/$problem_name/"

    # Create folder structure
    folder="$language/$topic/$difficulty"
    mkdir -p "$folder"

    # Check if the file already exists in the target directory
    if [ -f "$folder/$filename" ]; then
        echo "File $filename already exists in $folder/. Skipping file creation and README update."
        file_existed=true
    else
        # Create the file if it doesn't exist, or move it if it does
        if [ ! -f "$filename" ]; then
            touch "$folder/$filename"
            echo "# Add your solution for $problem_name here" > "$folder/$filename"
            echo "Created $filename in $folder/"
        else
            mv "$filename" "$folder/"
            echo "Moved $filename to $folder/"
        fi
        file_existed=false
    fi

    if grep -q "^$problem_number," "$log_file"; then
        # Update existing entry
        awk -F, -v OFS=',' -v pnum="$problem_number" -v pname="$problem_name" -v lang="$language" -v top="$topic" -v diff="$difficulty" -v lnk="$link" -v nr="$needs_review" -v refl="$reflection" '
        $1 == pnum {$2=pname; $3=lang; $4=top; $5=diff; $6=lnk; $7=nr; $9=refl}
        {print}
        ' "$log_file" > temp.csv && mv temp.csv "$log_file"
        echo "Updated entry for problem $problem_number."
    else
        # Add new entry
        echo "$problem_number,\"$problem_name\",$language,$topic,$difficulty,$link,$needs_review,$(date +%Y-%m-%d),\"$reflection\"" >> "$log_file"
        echo "Added new entry for problem $problem_number."
    fi

    # Update README.md only if the file didn't exist before
    if [ "$file_existed" != true ]; then
        total=$(wc -l < "$log_file")
        total=$((total - 1))  # Subtract 1 to account for the header line
        easy=$(grep -c ",easy," "$log_file")
        medium=$(grep -c ",medium," "$log_file")
        hard=$(grep -c ",hard," "$log_file")

        update_readme $total $easy $medium $hard "$filename" "$topic" "$difficulty"
    fi

    push_to_github $problem_number $problem_name $language $topic $difficulty
fi

echo "Local operations completed successfully!"
