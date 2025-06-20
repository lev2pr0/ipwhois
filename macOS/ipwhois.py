#!/usr/bin/env python3

"""
Filename: ipwhois.py
Author: Levar Norwood
Date: YYYY-MM-DD
Version: 1.0
Description: Briefly describe what your script does.
README: https://github.com/lev2pr0/ipwhois
"""

import os
import sys

def system_check():
    if sys.platform.startswith("win"):
        print("Windows detected. Not supported. Please use Powershell version.")
        print("=======================================")
        print("")
        print("Exiting.. Goodbye..")
        exit(1)
    elif sys.platform.startswith("darwin"):
        os.system("clear")
        print("macOS detected.")
        print("Starting...")
        print("")

    else:
        print(f"Platform '{sys.platform}' detected. Not supported")
        print("=======================================")
        print("")
        print("Exiting.. Goodbye..")
        exit(1)

def filepath_check(file_path):
    if file_path == None:
        file_path = input("Enter file path: ")
    target_file = os.path.abspath(file_path)

    if os.path.isdir(target_file) == True:
        print(f"'{target_file}' is a Directory path.")
        print("")
        print("Please provide path to .TXT or .CSV file.")
        print("=======================================")
        print("")
        print("Exiting.. Goodbye..")
        exit(1)

    if not os.path.exists(target_file):
        print(f"File '{target_file}' does not exist.")
        print("=======================================")
        print("")
        print("Exiting.. Goodbye..")
        exit(1)

def check_file_type(filepath):
    filename, file_extension = os.path.splitext(filepath)
    file_extension = file_extension.lower()

    if file_extension == '.txt':
        report = ".txt file"
        return report

    if file_extension == '.csv':
        report = ".csv file"
        return report

    return f"{file_extension} file"


def main():
    system_check()

    file_path = sys.argv[1]
    arguments_list = sys.argv[2:]

    # Check for --verbose to add prompt and set to TRUE
    if len(sys.argv) > 1:
        if "--verbose" in arguments_list:
            verbose = True
            print("Verbose mode enabled.")
            print("")

    filepath_check(file_path)
    file_type = check_file_type(file_path)
    print(f"File type: {file_type}")

    if file_type not in ['.txt file', '.csv file']:
        print(f"'{file_type} types' is not supported.")
        print("Please provide path to .TXT or .CSV file.")
        print("=======================================")
        print("")
        print("Exiting.. Goodbye..")
        exit(1)

if len(sys.argv) == 1:
        print("Usage: python3 ipwhois.py '<File_Path>'")
        print("=======================================")
        print("")
        print("Exiting.. Goodbye..")
        exit(1)

main()
