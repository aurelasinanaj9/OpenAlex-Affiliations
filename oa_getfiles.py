#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 10:27:55 2023

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

# reading line by line the gz file
import gzip
import json

        
# we get a dictionary seen as a string
# import json
# json.loads(line)["doi"]


# only few have authorships values
with gzip.open('part_000.gz','rt') as f:
    for line in f:
        if json.loads(line).get('authorships') !=[]:
            print(json.loads(line).get('authorships')) 
 
with gzip.open('part_000.gz','rt') as f:
   for line in f:
       print(line)
 

oa_file2 = []
with gzip.open('part_000.gz','rt') as f:
    for line in f:
        a = {"doi":[],"authorships":[]}
        a["doi"].append(json.loads(line).get('doi'))
        a["authorships"].append(json.loads(line).get('authorships'))
        oa_file2.append(a)

oa_final = open("oa_data.json","w")
json.dump(oa_file2,oa_final,indent=6)