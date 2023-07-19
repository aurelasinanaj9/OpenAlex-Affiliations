#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 22:13:30 2023

@author: aurelasinanaj
"""

import gzip


# folder_path = "output"  # Path to the root folder

# for root, dirs, files in os.walk(folder_path):
#     for file in files:
#         if file.startswith('matched'):
#             file_path = os.path.join(root, file)

#             with gzip.open(file_path, 'rt') as f:
#                 for line in f:
#                     data = json.loads(line)
#                     if 'id' in data and data['id'] == 'https://openalex.org/W2121528906':
#                         print(data)
#                         print("File:", file)
#                         print("Subfolder:", root)
#                         break
                    
                    
import csv

input_file = "sample.csv.gz"  # Path to the input CSV file
output_file = "cropped.csv.gz"  # Path to the output cropped CSV file
line_number = 11630  # Line number to start from (inclusive)

with gzip.open(input_file, 'rt') as file:
    reader = csv.reader(file)
    rows = list(reader)

header = rows[0]
cropped_rows = [header] + rows[line_number - 1:] 

with gzip.open(output_file, 'wt', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(cropped_rows)

print(f"File '{output_file}' created with lines starting from line number {line_number}.")