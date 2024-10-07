# LeetCode Solutions

Total LeetCode problems solved: 1 - Easy: 0 - Medium: 1 - Hard: 0

This repository contains my solutions to various LeetCode problems. The solutions are organized by programming language, then by topic, and finally by difficulty level.

## Repository Structure
\`\`\`
leetcode-solutions/
│
├── python/
│   ├── arrays/
│   │   ├── easy/
│   │   ├── medium/
│   │   └── hard/
│   ├── linked-lists/
│   │   ├── easy/
│   │   ├── medium/
│   │   └── hard/
│   └── ...
│
├── java/
│   ├── trees/
│   │   ├── easy/
│   │   ├── medium/
│   │   └── hard/
│   └── ...
│
├── cpp/
│   ├── graphs/
│   │   ├── easy/
│   │   ├── medium/
│   │   └── hard/
│   └── ...
│
├── contests/
│   └── ...
│
└── leetcode-push.sh
\`\`\`

## Usage
To add a new solution:
1. Solve the problem and save your solution in the repository root with the naming format: \`XXXX-problem-name.py\`
2. Run the \`leetcode-push.sh\` script with the following arguments:
\`\`\`bash
./leetcode-push.sh <filename> <topic> <difficulty>
\`\`\`
For example:
\`\`\`bash
./leetcode-push.sh 0001-two-sum.py arrays easy
\`\`\`
This will:
- Move the file to the appropriate folder based on the topic and difficulty
- Update the CSV log file with problem details
- Update this README with the latest problem counts

## Languages
- Python
- Java
- C++
- and more...

## Topics
- Arrays
- Linked Lists
- Trees
- Graphs
- Dynamic Programming
- and more...

## Contributing
This is a personal repository for my own LeetCode solutions. However, if you spot any errors or have suggestions for improvements, feel free to open an issue.

## License
This project is open source and available under the [MIT License](LICENSE).
| 0036 | valid sudoku | [Python](./python/array/medium/0036-valid-sudoku.py) | array | medium |
