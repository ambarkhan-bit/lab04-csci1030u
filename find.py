# Part 1 - a small "find" tool (like a simplified `grep`).
#
# This is a COMMAND-LINE program: you run it from the terminal and pass it
# arguments, e.g.   python find.py apple sample.txt
#
# The argument parser is started for you. Finish the TODOs below.

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Print the lines of a file that contain a given pattern.")
    parser.add_argument("pattern", help="the text to look for")
    parser.add_argument("filename", help="the file to search")
    parser.add_argument("-i", "--ignore-case", action="store_true",
                        help="ignore upper/lower case when matching")

    args = parser.parse_args()

    with open(args.filename) as f:
        for number, line in enumerate(f, start=1):
            line = line.rstrip("\n")
            if args.ignore_case:
                found = args.pattern.lower() in line.lower()
            else:
                found = args.pattern in line
            if found:
                print(f"{number}: {line}")


if __name__ == "__main__":
    main()
