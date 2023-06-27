#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 10:27:55 2023

@author: aurelasinanaj
"""


import os
import gzip
import json
import csv
  
# Step 1: Load DOI links from the dblp file into a set
input_csv_file = 'output_dblp_ee.csv.gz'
doi_set = set()
with gzip.open(input_csv_file, 'rt') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        doi_set.add(row[0])

# # Step 2: Process the compressed file from OA and split based on DOI matches
         
         
input_folder_path = '/tempdata/openalex-snapshot/data/works'
output_folder_path = 'output'

# Recursively iterate over files in the input folder and its subfolders
for root, dirs, files in os.walk(input_folder_path, followlinks=True):
    # Get the relative path of the current folder
    relative_path = os.path.relpath(root, input_folder_path)
    relative_path = relative_path.strip('')
    
    # Create the corresponding subfolder in the output directory
    output_subfolder = os.path.join(output_folder_path, relative_path)
    os.makedirs(output_subfolder, exist_ok=True)

    for filename in files:
        if filename.endswith('.gz'):
            input_file_path = os.path.join(root, filename)
            
            # Get the name of the file without the extension
            file_name = os.path.splitext(filename)[0]
            
            # Create the output file paths with the original file name in the subfolder
            output_matched_file = os.path.join(output_subfolder, f'matched_{file_name}.json.gz')
            output_unmatched_file = os.path.join(output_subfolder, f'unmatched_{file_name}.json.gz')

            with gzip.open(input_file_path, 'rt') as input_file, \
                    gzip.open(output_matched_file, 'wt') as matched_file, \
                    gzip.open(output_unmatched_file, 'wt') as unmatched_file:

                for line in input_file:
                    data = json.loads(line)
            with gzip.open(input_file_path, 'rt') as input_file, \
                    gzip.open(output_matched_file, 'wt') as matched_file, \
                    gzip.open(output_unmatched_file, 'wt') as unmatched_file:

                for line in input_file:
                    data = json.loads(line)

                    if data.get('authorships') and isinstance(data['authorships'], list):
                        
                        contains_raw_affiliation = False
                        
                        for authorship in data['authorships']:
                            raw_affiliations = authorship.get('raw_affiliation_strings') or authorship.get(
                                'raw_affiliation_string')
                            if raw_affiliations:
                                contains_raw_affiliation = True

                        if contains_raw_affiliation:
                            doi = data.get('doi')
                            if doi and doi.startswith('https://doi.org/'):
                                doi = doi[len('https://doi.org/'):]  # Remove the initial part
                                if doi in doi_set:
                                    # Step 3: Save the matched and unmatched data into separate files
                                    matched_entry = {
                                        'id': data.get('id'),
                                        'doi': data.get('doi'),
                                        'title': data.get('title'),
                                        'authorships': data.get('authorships'),
                                        'publication_year': data.get('publication_year')
                                    }
                                    matched_file.write(json.dumps(matched_entry) + '\n')
                                else:
                                    unmatched_entry = {
                                        'id': data.get('id'),
                                        'doi': data.get('doi'),
                                        'title': data.get('title'),
                                        'authorships': data.get('authorships'),
                                        'publication_year': data.get('publication_year')
                                    }
                                    unmatched_file.write(json.dumps(unmatched_entry) + '\n')




# def process_file(input_file_path, output_subfolder):
#     # Get the name of the file without the extension
#     file_name = os.path.splitext(os.path.basename(input_file_path))[0]

#     # Create the output file paths with the original file name in the subfolder
#     output_matched_file = os.path.join(output_subfolder, f'matched_{file_name}.json.gz')
#     output_unmatched_file = os.path.join(output_subfolder, f'unmatched_{file_name}.json.gz')

#     with gzip.open(input_file_path, 'rt') as input_file, \
#             gzip.open(output_matched_file, 'wt') as matched_file, \
#             gzip.open(output_unmatched_file, 'wt') as unmatched_file:

#         for line in input_file:
#             data = json.loads(line)

#             if data.get('authorships') and isinstance(data['authorships'], list):
#                 for authorship in data['authorships']:
#                     raw_affiliations = authorship.get('raw_affiliation_strings') or authorship.get(
#                         'raw_affiliation_string')

#                     if raw_affiliations:
#                         doi = data.get('doi')
#                         if doi and doi.startswith('https://doi.org/'):
#                             doi = doi[len('https://doi.org/'):]  # Remove the initial part
#                             if doi in doi_set:
#                                 # Step 3: Save the matched and unmatched data into separate files
#                                 matched_entry = {
#                                     'id': data.get('id'),
#                                     'doi': data.get('doi'),
#                                     'title': data.get('title'),
#                                     'authorships': data.get('authorships')
#                                 }
#                                 matched_file.write(json.dumps(matched_entry) + '\n')
#                             else:
#                                 unmatched_entry = {
#                                     'id': data.get('id'),
#                                     'doi': data.get('doi'),
#                                     'title': data.get('title'),
#                                     'authorships': data.get('authorships')
#                                 }
#                                 unmatched_file.write(json.dumps(unmatched_entry) + '\n')

# # Recursively iterate over files in the input folder and its subfolders
# for root, dirs, files in os.walk(input_folder_path):
#     # Get the relative path of the current folder
#     relative_path = os.path.relpath(root, input_folder_path)

#     # Create the corresponding subfolder in the output directory
#     output_subfolder = os.path.join(output_folder_path, relative_path)
#     os.makedirs(output_subfolder, exist_ok=True)

#     for filename in files:
#         if filename.endswith('.gz'):
#             input_file_path = os.path.join(root, filename)
            
#             # Process the file and save the result in the output subfolder
#             process_file(input_file_path, output_subfolder)




# def process_file(input_file_path, output_subfolder):
#     # Get the name of the file without the extension
#     file_name = os.path.splitext(os.path.basename(input_file_path))[0]

#     # Create the output file paths with the original file name in the subfolder
#     output_matched_file = os.path.join(output_subfolder, f'matched_{file_name}.json.gz')
#     output_unmatched_file = os.path.join(output_subfolder, f'unmatched_{file_name}.json.gz')

#     with gzip.open(input_file_path, 'rt') as input_file, \
#             gzip.open(output_matched_file, 'wt') as matched_file, \
#             gzip.open(output_unmatched_file, 'wt') as unmatched_file:

#         for line in input_file:
#             data = json.loads(line)

#             if data.get('authorships') and isinstance(data['authorships'], list):
#                 for authorship in data['authorships']:
#                     raw_affiliations = authorship.get('raw_affiliation_strings') or authorship.get(
#                         'raw_affiliation_string')

#                     if raw_affiliations:
#                         doi = data.get('doi')
#                         if doi and doi.startswith('https://doi.org/'):
#                             doi = doi[len('https://doi.org/'):]  # Remove the initial part
#                             if doi in doi_set:
#                                 # Step 3: Save the matched and unmatched data into separate files
#                                 matched_entry = {
#                                     'id': data.get('id'),
#                                     'doi': data.get('doi'),
#                                     'title': data.get('title'),
#                                     'authorships': data.get('authorships')
#                                 }
#                                 matched_file.write(json.dumps(matched_entry) + '\n')
#                             else:
#                                 unmatched_entry = {
#                                     'id': data.get('id'),
#                                     'doi': data.get('doi'),
#                                     'title': data.get('title'),
#                                     'authorships': data.get('authorships')
#                                 }
#                                 unmatched_file.write(json.dumps(unmatched_entry) + '\n')

# # Recursively iterate over files in the input folder and its subfolders
# for root, dirs, files in os.walk(input_folder_path):
#     # Get the relative path of the current folder
#     relative_path = os.path.relpath(root, input_folder_path)

#     # Remove the quotation marks from the relative path
#     relative_path = relative_path.strip('"')

#     # Create the corresponding subfolder in the output directory
#     output_subfolder = os.path.join(output_folder_path, relative_path)
#     os.makedirs(output_subfolder, exist_ok=True)

#     for filename in files:
#         if filename.endswith('.gz'):
#             input_file_path = os.path.join(root, filename)
            
#             # Process the file and save the result in the output subfolder
#             process_file(input_file_path, output_subfolder)








