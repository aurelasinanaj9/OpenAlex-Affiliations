#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 14:11:25 2023

@author: aurelasinanaj
"""


import os
import gzip

# From all matched files retrieved, obtaining a sample of 10 000 lines (retrieving the first line from all 
# files, then second and so on...)

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
                            if len(lines) > line_position: # checking there are enough lines
                                sample.write(lines[line_position])
                                line_count += 1

                    if line_count >= lines_to_retrieve:
                        break

            if line_count >= lines_to_retrieve:
                break

        line_position += 1

print("Extraction complete, lines saved.")
        
        


