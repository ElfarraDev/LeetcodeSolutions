# LeetCode Solutions

This repository contains my solutions to various LeetCode problems. The solutions are organized by programming language, then by topic, and finally by difficulty level.

## Repository Structure

```
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
```

## Usage

To add a new solution:

1. Solve the problem and save your solution in the repository root with the naming format: `XXXX_problem_name.extension`
2. Run the `leetcode-push.sh` script with the following arguments:

```bash
./leetcode-push.sh <filename> <language> <topic> <difficulty>
```

For example:
```bash
./leetcode-push.sh 0001_two_sum.py python arrays easy
```

This will:
- Move the file to the appropriate folder based on the language, topic, and difficulty
- Commit the changes with a standardized message
- Push the changes to GitHub

## Languages

- Python
- Java
- C++
- (Add more languages as you use them)

## Topics

- Arrays
- Linked Lists
- Trees
- Graphs
- Dynamic Programming
- (Add more topics as you cover them)

## Contributing

This is a personal repository for my own LeetCode solutions. However, if you spot any errors or have suggestions for improvements, feel free to open an issue.

## License

This project is open source and available under the [MIT License](LICENSE).
