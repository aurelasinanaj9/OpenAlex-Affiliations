#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 22:06:51 2023

@author: aurelasinanaj
"""
import csv
import gzip
import json



# creating the csv file with only the data we need
with gzip.open('output/output.json.gz', 'rt') as f,\
        gzip.open('sample.csv.gz', 'wt') as sample:
            
            writer = csv.writer(sample)
            writer.writerow(['oa_id', 'oa_count', 'affiliation_string', 'ror_id'])  # header

            for line in f:
                unique_combinations = set()
                z= 0
                data = json.loads(line) 
                oa_id = data.get('id')

                for authorship in data['authorships']:

                    ror_list = []  # list to store ror values

                    for institution in authorship['institutions']:
                        ror = institution.get('ror')
                        if ror:
                            ror_list.append(ror)
                        else:
                            ror_list.append('NA')


                    raw_affiliations = authorship.get('raw_affiliation_strings') or authorship.get(
                                'raw_affiliation_string')


                    for ror in ror_list:
                        combination = (ror, raw_affiliations)
                        if combination not in unique_combinations:
                            unique_combinations.add(combination)
                            z+= 1
                            writer.writerow([oa_id,z, raw_affiliations, ror])
                        
                        
                        
                        
    
