#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 19:27:16 2023

@author: aurelasinanaj
"""

import os
import gzip
import json
import csv

from s2aff.ror import RORIndex
from s2aff.model import NERPredictor, PairwiseRORLightGBMReranker

# #creating the path to access each file
# folder_path = 'output'

# for root, dirs, files in os.walk(folder_path):
#     for file in files:
#         if file.startswith('matched'):
#             file_path = os.path.join(root, file)

#             with gzip.open(file_path, 'rt') as f:
#                 for line in f:
#                     data = json.loads(line)
                    
#                     for authorship in data['authorships']:
#                             raw_affiliation = authorship.get('raw_affiliation_strings') or authorship.get(
#                                 'raw_affiliation_string')
                            
#                             ner_predictor = NERPredictor(use_cuda=False)
#                             ror_index = RORIndex()  
#                             pairwise_model = PairwiseRORLightGBMReranker(ror_index)
#                             candidates, scores = ror_index.get_candidates_from_raw_affiliation(raw_affiliation, ner_predictor)
#                             reranked_candidates, reranked_scores = pairwise_model.predict(raw_affiliation, candidates[:100], scores[:100])

#                             # print out the top 5 candidates and scores from the second stage
#                             for i, j in zip(reranked_candidates[:5], reranked_scores[:5]):
#                                 print(ror_index.ror_dict[i]["id"], j)
    
    
    

# Open the input CSV file and create an output CSV file
input_file = 'sample.csv.gz'
output_file = 'predicted_values.csv.gz'

with gzip.open(input_file, 'rt') as csv_in, gzip.open(output_file, 'wt', newline='') as csv_out:
    reader = csv.DictReader(csv_in)
    writer = csv.DictWriter(csv_out, fieldnames=reader.fieldnames + ['s2aff_perdiction'])

    writer.writeheader()  # Write the header to the output file

    for row in reader:
        affiliation_string = row['affiliation_string'] 
        ner_predictor = NERPredictor(use_cuda=False)
        ror_index = RORIndex()  
        pairwise_model = PairwiseRORLightGBMReranker(ror_index)
        candidates, scores = ror_index.get_candidates_from_raw_affiliation(affiliation_string, ner_predictor)
        reranked_candidates, reranked_scores = pairwise_model.predict(affiliation_string, candidates[:100], scores[:100])

        # Process the computed values and update the corresponding row
        s2aff_perdiction = []
        for i, j in zip(reranked_candidates[:5], reranked_scores[:5]):
            s2aff_perdiction.append(f"{ror_index.ror_dict[i]['id']}: {j}")

        row['s2aff_perdiction'] = ', '.join(s2aff_perdiction)
        writer.writerow(row)
                    
                    
                    
                    
                    
                    
                    