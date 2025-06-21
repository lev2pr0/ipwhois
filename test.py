import os
import csv

def ip_counter(iplist):
    ip_count = {}
    for ip in iplist:
        ip_count[ip] = ip_count.get(ip, 0) + 1

    output_filename_csv = "ipcount_verbose.csv"
    with open(output_filename_csv, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['IP', 'Count'])

        for ip, count in ip_count.items():
            csv_writer.writerow([ip, count])

    return f"CSV data exported to {output_filename_csv}\nLocation: {os.getcwd()}"


results = ip_counter(['192.168.1.1', '192.168.1.2', '192.168.1.1'])
print(results)
