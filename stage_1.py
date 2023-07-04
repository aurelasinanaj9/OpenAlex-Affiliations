#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 14:11:25 2023

@author: aurelasinanaj
"""


import os
import gzip
import json


# getting a random sample
folder_path = 'output'
lines_to_extract = 10000 # total number of lines (papers) to extract

output_file = 'output.json.gz'
output_file_path = os.path.join(folder_path, output_file)

with gzip.open(output_file_path, 'wt') as output:
    lines_written = 0

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.startswith('matched'):
                file_path = os.path.join(root, file)

                with gzip.open(file_path, 'rt') as f:
                    for line_num, line in enumerate(f):
                        if lines_written >= lines_to_extract:
                            break

                        line_data = json.loads(line)
                        output.write(json.dumps(line_data) + '\n')
                        lines_written += 1

                if lines_written >= lines_to_extract:
                    break

            if lines_written >= lines_to_extract:
                break

        if lines_written >= lines_to_extract:
            break

print("Extraction complete. Lines saved in:", output_file_path)



# creating the csv file with only the data we need
with gzip.open('output.json.gz', 'rt') as f,\
        gzip.open('sample.csv.gz', 'wt') as sample:
            
            writer = csv.writer(sample)
            writer.writerow(['oa_id', 'affiliation_string', 'ror_id'])  # Header
            
            for line in f:
                data = json.loads(line) 
                oa_id = data.get('id')
                 
                for authorship in data['authorships']:
                    for institution in authorship['institutions']:
                        ror = institution.get('ror')
                        if ror:
                            ror
                        else:
                            ror = 'NA'
                    
                    raw_affiliations = authorship.get('raw_affiliation_strings') or authorship.get(
                                'raw_affiliation_string')
                     
                    writer.writerow([oa_id, raw_affiliations, ror])       
                     
             
                     
        