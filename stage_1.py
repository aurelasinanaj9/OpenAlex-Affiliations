#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 14:11:25 2023

@author: aurelasinanaj
"""


import os
import gzip
import json
import random


# # getting a random sample
# folder_path = 'output'
# lines_to_extract = 10000 # total number of lines (papers) to extract

# output_file = 'output.json.gz'
# output_file_path = os.path.join(folder_path, output_file)

# with gzip.open(output_file_path, 'wt') as output:
#     lines_written = 0

#     for root, dirs, files in os.walk(folder_path):
#         for file in files:
#             if file.startswith('matched'):
#                 file_path = os.path.join(root, file)
                

#                 with gzip.open(file_path, 'rt') as f:
#                     file_content = f.read()
#                     data = json.loads(file_content)

#                     if data:
#                         random_line = random.choice(data)
#                         output.write(json.dumps(random_line) + '\n')
#                         lines_written += 1
                    
#                     if lines_written >= lines_to_extract:
#                         break


#         if lines_written >= lines_to_extract:
#             break

# print("Extraction complete. Lines saved in:", output_file_path)


# with gzip.open('output/updated_date=2023-02-01/matched_part_013.json.gz', 'rt') as f,\
#         gzip.open('output/output.json.gz', 'wt') as sample:
#             for index, line in enumerate(f): 
#                 sample.write(line)
        
#                 if index + 1 >= 10000:
#                     break
            
# print("Extraction complete. Lines saved")

output_file = 'output/output.json.gz'
i = 0
length = 1
position = 0

with gzip.open(output_file, 'wt') as sample:
    
    length += 1
    position += 1
    for folder_name in os.listdir('output'):
        folder_path = os.path.join('output', folder_name)
        
        if os.path.isdir(folder_path) and folder_name.startswith('updated_date='):
            
            for file_name in os.listdir(folder_path):
                if file_name.startswith('matched'):
                    file_path = os.path.join(folder_path, file_name)
                    
                    with gzip.open(file_path, 'rt') as f:
                        lines = f.readlines()
                        if len(lines) >= length:
                            sample.write(lines[position])
                            i += 1
                            
                
                        if i >= 10000:
                            break
                            
            if i >= 10000:
                break
            
                        
                            

print("Extraction complete. Lines saved.")


output_file = 'output/output.json.gz'
lines_to_retrieve = 10000

with gzip.open(output_file, 'wt') as sample:
    line_count = 0
    line_position = 0

    while line_count < lines_to_retrieve:
        for folder_name in os.listdir('output'):
            folder_path = os.path.join('output', folder_name)

            if os.path.isdir(folder_path) and folder_name.startswith('updated_date='):
                for file_name in os.listdir(folder_path):
                    if file_name.startswith('matched'):
                        file_path = os.path.join(folder_path, file_name)

                        with gzip.open(file_path, 'rt') as f:
                            lines = f.readlines()
                            if len(lines) > line_position:
                                sample.write(lines[line_position])
                                line_count += 1

                    if line_count >= lines_to_retrieve:
                        break

            if line_count >= lines_to_retrieve:
                break

        line_position += 1

print("Extraction complete. Lines saved.")
        
        


