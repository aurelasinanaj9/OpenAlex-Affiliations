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
import csv
        
# we get a dictionary seen as a string
# import json
# json.loads(line)["doi"]


# only few have authorships values
with gzip.open('part_001.gz','rt') as f:
    for line in f:
        if json.loads(line).get('authorships') !=[]:
            print(json.loads(line).get('authorships')) 
       
 
with gzip.open('part_001.gz','rt') as f:
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


#### 
input_file_path = 'part_000.gz'
output_file_path = 'output_oa_1.json.gz'
keys_to_extract = ['id', 'doi','title', 'authorships']

with gzip.open(input_file_path, 'rt') as input_file, gzip.open(output_file_path, 'wt') as output_file:
    for line in input_file:
        data = json.loads(line)
        extracted_data = {key: data[key] for key in keys_to_extract if key in data}
        if extracted_data.get('authorships') != []:
            output_file.write(json.dumps(extracted_data) + '\n')

count = 0
with gzip.open('output_oa_1.json.gz','rt') as f:
    for line in f:
        count +=1        
  
# count
# Out[149]: 22
# we checked that we have 22 values for authorships


# bigger file
input_file_path = 'part_001.gz'
output_file_path = 'output_oa_3.json.gz'
keys_to_extract = ['id', 'doi','title', 'authorships']

with gzip.open(input_file_path, 'rt') as input_file, gzip.open(output_file_path, 'wt') as output_file:
    for line in input_file:
        data = json.loads(line)
        
        extracted_data = {key: data[key] for key in keys_to_extract if key in data}
       
        if extracted_data.get('authorships') and isinstance(extracted_data['authorships'], list):
            for authorship in extracted_data['authorships']:
                raw_affiliations = authorship.get('raw_affiliation_strings') or authorship.get('raw_affiliation_string')
                if raw_affiliations:
                    output_file.write(json.dumps(extracted_data) + '\n')
                    break 
    
            
 
            
# with gzip.open('part_001.gz', 'rt') as f:
#     for line in f:
        
#         data = json.loads(line)
#         authorships = data.get('authorships')

#         if authorships and isinstance(authorships, list):
#             for authorship in authorships:
#                 raw_affiliations = authorship.get('raw_affiliation_strings') or authorship.get('raw_affiliation_string')

#                 if raw_affiliations:
#                     print(json.dumps(authorships))
#                     break    

 

  
# Step 1: Load DOI links from the second file into a set
input_csv_file = 'output_dblp_ee.csv.gz'
doi_set = set()
with gzip.open(input_csv_file, 'rt') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        doi_set.add(row[0])

# Step 2: Process the first file and split based on DOI matches

input_file_path = 'part_001.gz'
output_file_path = 'output_oa_4.json.gz'
keys_to_extract = ['id', 'doi','title', 'authorships']

output_matched_file = 'matched_file.json.gz'
output_unmatched_file = 'unmatched_file.json.gz'
  
matched_data = []
unmatched_data = []

# with gzip.open(input_file_path, 'rt') as input_file, gzip.open(output_file_path, 'wt') as output_file:
#     for line in input_file:
#         data = json.loads(line)

#         extracted_data = {key: data[key] for key in keys_to_extract if key in data}

#         if extracted_data.get('authorships') and isinstance(extracted_data['authorships'], list):
#             for authorship in extracted_data['authorships']:
#                 raw_affiliations = authorship.get('raw_affiliation_strings') or authorship.get('raw_affiliation_string')

#                 if raw_affiliations:
#                     output_file.write(json.dumps(extracted_data) + '\n')
#                     break
    
#         #switching to from writing to reading
#     #output_file = gzip.open(output_file_path, 'rt')
#     # Reset the file pointer to the beginning of the file
#     output_file.seek(0)

#     for line in output_file:
#         data = json.loads(line)
#         doi = data.get('doi')

#         if doi and doi.startswith('https://doi.org/'):

#             doi = doi[len('https://doi.org/'):]  # Remove the initial part

#             if doi in doi_set:
#                 matched_data.append(data)
#             else:
#                 unmatched_data.append(data)
                










with gzip.open(input_file_path, 'rt') as input_file, \
     gzip.open(output_matched_file, 'wt') as matched_file, \
     gzip.open(output_unmatched_file, 'wt') as unmatched_file:
    
    for line in input_file:
        data = json.loads(line)

        if data.get('authorships') and isinstance(data['authorships'], list):
            for authorship in data['authorships']:
                raw_affiliations = authorship.get('raw_affiliation_strings') or authorship.get('raw_affiliation_string')

                if raw_affiliations:
                    doi = data.get('doi')
                    if doi and doi.startswith('https://doi.org/'):
                        doi = doi[len('https://doi.org/'):]  # Remove the initial part
                        if doi in doi_set:
                            matched_entry = {
                                'id': data.get('id'),
                                'doi': data.get('doi'),
                                'title': data.get('title'),
                                'authorships': data.get('authorships')
                            }
                            matched_file.write(json.dumps(matched_entry) + '\n')
                        else:
                            unmatched_entry = {
                                'id': data.get('id'),
                                'doi': data.get('doi'),
                                'title': data.get('title'),
                                'authorships': data.get('authorships')
                            }
                            unmatched_file.write(json.dumps(unmatched_entry) + '\n')






















with gzip.open(input_file_path, 'rt') as input_file:
    for line in input_file:
        data = json.loads(line)

        #extracted_data = {key: data[key] for key in keys_to_extract if key in data}

        if data.get('authorships') and isinstance(data['authorships'], list):
            for authorship in data['authorships']:
                raw_affiliations = authorship.get('raw_affiliation_strings') or authorship.get('raw_affiliation_string')

                if raw_affiliations:
                    doi = data.get('doi')
                    if doi and doi.startswith('https://doi.org/'):
                        doi = doi[len('https://doi.org/'):]  # Remove the initial part
                        if doi in doi_set:
                            matched_entry = {
                                'id': data.get('id'),
                                'doi': data.get('doi'),
                                'title': data.get('title'),
                                'authorships': data.get('authorships')
                            }
                            matched_data.append(matched_entry)
                        else:
                            unmatched_entry = {
                                'id': data.get('id'),
                                'doi': data.get('doi'),
                                'title': data.get('title'),
                                'authorships': data.get('authorships')
                            }
                            unmatched_data.append(unmatched_entry)
                


# Step 3: Save the matched and unmatched data into separate files
with gzip.open(output_matched_file, 'wt') as matched_file:
    for data in matched_data:
        matched_file.write(json.dumps(data) + '\n')

with gzip.open(output_unmatched_file, 'wt') as unmatched_file:
    for data in unmatched_data:
        unmatched_file.write(json.dumps(data) + '\n') 

# # Step 2: Process the first file and split based on DOI matches
# matched_data = []
# unmatched_data = []

# with gzip.open(input_json_file, 'rt') as json_file:
#     for line in json_file:
#         data = json.loads(line)
#         doi = data.get('doi')
        
#         if doi and doi.startswith('https://doi.org/'):
            
#             doi = doi[len('https://doi.org/'):]  # Remove the initial part
        
#             if doi in doi_set:
#                 matched_data.append(data)
#             else:
#                 unmatched_data.append(data)
      

    
# Looking at matched and unmateched works
matched=0
with gzip.open('matched_file.json.gz', 'rt') as json_file:
    for line in json_file:
        matched+=1
#12492
         
unmatched=0
with gzip.open('unmatched_file.json.gz', 'rt') as json_file:
    for line in json_file:
        unmatched+=1
#206341         
         