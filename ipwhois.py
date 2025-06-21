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
import urllib.request
import urllib.error
import json

# System Check and clear terminal
def system_check():
    if sys.platform.startswith("win"):
        os.system("cls")
        print("Windows detected.")
        print("Starting...")
        print("")
    elif sys.platform.startswith("darwin"):
        os.system("clear")
        print("macOS detected.")
        print("Starting...")
        print("")
    else:
        os.system("clear")
        print(f"Platform '{sys.platform}' detected.")
        print("Starting...")
        print("")

# Verify filepath exists
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

# Check for file type
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

# Scan file for IPv4 and export to a list
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
            exit(1)
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
            exit(1)
        return iplist

# Final function to run whois on IP addresses and export to csv
def ipwhois_run(ip_found, verbose=False):
    unique_ips = list(set(ip_found))
    baseurl = 'https://ipinfo.io/'
    ipwhois_dict = {
        "IP": "ip",
        "Name": "org",
        "Country": "country",
        "City": "city",
    }

    verbose_ipwhois_dict = {
        "IP": "ip",
        "Name": "org",
        "Hostname": "hostname",
        "Country": "country",
        "City": "city",
        "Region": "region",
        "Postal": "postal",
        "Coordinates": "loc",
    }

    ip_data = []
    for ip in unique_ips:
        url = baseurl + ip
        print(f"Connecting to {url}...")
        try:
            ipwhois_data = urllib.request.urlopen(url).read().decode('utf-8')
        except urllib.error.HTTPError as e:
            print(f"HTTP error encountered: {e.code} {e.reason}")
            return exit(1)
        except urllib.error.URLError as e:
            print(f"URLError encountered: {e.reason}")
            return exit(1)
        except Exception as e:
            print(f"Unexpected error encountered: {e}")
            return exit(1)
        else:
            print("Request successful")
            convert = json.loads(ipwhois_data)
            ip_data.append(convert)

    if verbose == True:
        print(ip_data)
        output_filename_csv = "ipwhois_verbose.csv"
        csv_headers = verbose_ipwhois_dict.keys()
        actual_data_keys = [verbose_ipwhois_dict[header] for header in csv_headers]

        with open(output_filename_csv, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)

            csv_writer.writerow(csv_headers)

            for record in ip_data:
                row = []
                for key in actual_data_keys:
                    row.append(record.get(key, 'null'))
                csv_writer.writerow(row)

        return f"CSV data exported to {output_filename_csv}"

    else:
        output_filename_csv = "ipwhois.csv"
        csv_headers = ipwhois_dict.keys()
        actual_data_keys = [ipwhois_dict[header] for header in csv_headers]

        with open(output_filename_csv, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)

            csv_writer.writerow(csv_headers)

            for record in ip_data:
                row = []
                for key in actual_data_keys:
                    row.append(record.get(key, 'null'))
                csv_writer.writerow(row)

        return f"CSV data exported to {output_filename_csv}"


def main():
    system_check()

    filepath = sys.argv[1]
    arguments_list = sys.argv[2:]

    # Check for --verbose to set to TRUE
    verbose = False
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

    result = ipwhois_run(ip_found, verbose)
    print(result)
    print("All done.. Goodbye..")


# Main function starts here
if len(sys.argv) == 1:
        print("Usage: python3 ipwhois.py '<filepath>'")
        print("")
        print("Exiting.. Goodbye..")
        exit(1)

main()
