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


# so we have to problems: the compressed file is too big, and we had a problem
# with The error message "undefined entity á: line 14, column 44" indicates 
# that the XML parser encountered an undefined entity reference in the XML file. 
#In this case, the entity reference "á" is not defined in the XML file, which 
#is causing the parser to raise an error.

    
# Open the input file
with gzip.open('dblp.xml.gz', 'rt') as f:
    # Open the output compressed CSV file in write mode
    with gzip.open('dblp.csv.gz', 'wt', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        for line in f:
            line = line.strip() # Remove leading/trailing whitespaces
            if line.startswith('"') and line.endswith('"'):
                line = line[1:-1] 
            
            if line.startswith("<author>"):
                author = line.strip()
                writer.writerow([author])        
                
            if line.startswith("<title>"):
                title = line.strip()
                writer.writerow([title])  # Write the tag and value to CSV
            
            if line.startswith('<ee type="oa">https://doi.org'):
                ee = line.strip()
                writer.writerow([ee])  # Write the tag and value to CSV
            
            if line.startswith("<ee>https://doi.org/"):
                ee = line.strip()
                writer.writerow([ee])  # Write the tag and value to CSV

# modified code in order to eliminate some lines that had quotation marks, in
# order to get all tags

line_author=0
line_title=0
line_ee=0

with gzip.open('dblp.csv.gz', 'rt') as f:
    for line in f:
        if line.startswith("<author>"):
            line_author+=1
            
        if line.startswith("<title>"):
            line_title+=1
            
        if line.startswith("<ee>"):
            line_ee+=1


line_count=0
with gzip.open('dblp.csv.gz', 'rt') as f:
    for line in f:
        line_count+=1 
        
# line_count
# Out[64]: 35790715   
# found out that not all tags are equivalent        

# line_ee/line_title
# Out[138]: 0.5492263854625677
# a little over 50% of titles have doi link
