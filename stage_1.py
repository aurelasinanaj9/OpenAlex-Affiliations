#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 14:11:25 2023

@author: aurelasinanaj
"""

import os
import gzip
import json
import csv

folder_path = 'output'

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.startswith('matched'):
            file_path = os.path.join(root, file)

            with gzip.open(file_path, 'rt') as f:
                for line in f:
                    
                    
                    
                    
with gzip.open('matched_file.json.gz', 'rt') as f,\
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
                     
             
                     
                     
with gzip.open('matched_file.json.gz', 'rt') as f,\
        gzip.open('sample.csv.gz', 'wt') as sample:

             for line in f:
                 data = json.loads(line) 
                 id_oa = data.get('id')
                 sample.write(id_oa + '\n') 
                 
                 for authorship in data['authorships']:
                     for institution in authorship['institutions']:
                         ror = institution.get('ror')
                         if ror:
                             sample.write(ror + '\n')
                         else:
                             sample.write("not present" + '\n')
                    
                     raw_affiliations = authorship.get('raw_affiliation_strings') or authorship.get(
                                'raw_affiliation_string')
             write = {'id_oa': data.get('id'),
                      'doi': data.get('doi'),
                      'title': data.get('title'),
                      'authorships': data.get('authorships'),
                      'publication_year': data.get('publication_year')
             }
             matched_file.write(json.dumps(matched_entry) + '\n')        
                     
                     sample.write(raw_affiliations + '\n')                     
                     
             
# need to find way to save in columns