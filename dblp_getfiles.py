#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 10:33:13 2023

@author: aurelasinanaj
"""

# open compressed file and read line line by line
# to get json object 
# look at record
# line by line
# write compact form
# entire author block (object)
# json renderer
# print line by linne author and doi


# DBLP
#import xml.sax
import gzip
import csv
import re


output_file = 'output_dblp_ee.csv.gz'

with gzip.open('/www/xml/dblp.xml.gz', 'rt') as f, gzip.open(output_file, 'wt') as csvfile:
    writer = csv.writer(csvfile)

    for line in f:
        if line.startswith('<ee>https://doi.org/'):
            match = re.search(r'<ee>https://doi.org/(.+)</ee>', line)
            if match:
                extracted_string = match.group(1)
                writer.writerow([extracted_string])        
        
        if line.startswith('<ee type="oa">https://doi.org'):
            match = re.search(r'<ee type="oa">https://doi.org/(.+)</ee>', line)
            if match:
                extracted_string = match.group(1)
                writer.writerow([extracted_string])
                
print(f"Extraction complete. Output saved to {output_file}")









