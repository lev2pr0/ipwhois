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
import csv
import re



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

def filepath_check(filepath):
    if filepath == None:
        filepath = input("Enter file path: ")
    target_file = os.path.abspath(filepath)

    if os.path.isdir(target_file) == True:
        print(f"'{target_file}' is a Directory path.")
        print("")
        print("Please provide path to .TXT or .CSV file.")
        print("")
        print("Exiting.. Goodbye..")
        exit(1)

    if not os.path.exists(target_file):
        print(f"File '{target_file}' does not exist.")
        print("")
        print("Exiting.. Goodbye..")
        exit(1)

def check_file_type(filepath):
    filename, file_extension = os.path.splitext(filepath)
    file_extension = file_extension.lower()

    if file_extension == '.txt':
        report = ".txt"
        return report

    if file_extension == '.csv':
        report = ".csv"
        return report

    return file_extension

def scan_export(file_type, filepath, ip_column_name):
    target_file = os.path.abspath(filepath)
    ipv4_pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')

    if file_type == '.csv':
        iplist = []
        try:
            with open(target_file, mode='r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                if ip_column_name not in reader.fieldnames:
                    print(f"Error: Column '{ip_column_name}' not found in the CSV file.")
                    return iplist
                for row in reader:
                    potential_ip = row.get(ip_column_name, '')
                    ip_match = ipv4_pattern.search(potential_ip)
                    if ip_match:
                        iplist.append(ip_match.group(0))
        except Exception as e:
            print(f"An error occurred: {e}")
        return iplist

    if file_type == '.txt':
        iplist = []
        try:
            with open(target_file, mode='r') as txtfile:
                for line in txtfile:
                    split_line = line.split()
                    for potential_ip in split_line:
                        if ipv4_pattern.match(potential_ip):
                            iplist.append(potential_ip)
        except Exception as e:
            print(f"An error occurred: {e}")
        return iplist

def main():
    system_check()

    filepath = sys.argv[1]
    arguments_list = sys.argv[2:]

    # Check for --verbose to set to TRUE
    if len(sys.argv) > 1:
        if "--verbose" in arguments_list:
            verbose = True
            print("Verbose mode enabled.")
            print("")


    filepath_check(filepath)
    file_type = check_file_type(filepath)
    print(f"Provided file: {filepath}")
    print(f"File type: {file_type}")

    if file_type not in ['.txt', '.csv']:
        print("")
        print(f"'{file_type} file types' is not supported.")
        print("Please provide path to .TXT or .CSV file.")
        print("")
        print("Exiting.. Goodbye..")
        exit(1)

    if file_type == '.csv':
        prompt = input("Enter the column name containing IPs [case sensitive]: ")
        ip_column_name = prompt
        ip_found = scan_export(file_type, filepath, ip_column_name)
        print(f"IP(s) found: {ip_found}")
        print("")
    else:
        ip_found = scan_export(file_type, filepath, ip_column_name=None)
        print(f"IP(s) found: {ip_found}")
        print("")

if len(sys.argv) == 1:
        print("Usage: python3 ipwhois.py '<filepath>'")
        print("")
        print("Exiting.. Goodbye..")
        exit(1)

main()
