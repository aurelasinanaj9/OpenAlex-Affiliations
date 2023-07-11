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

    

# Open the input CSV file and create an output CSV file
input_file = 'sample.csv.gz'
output_file = 'predicted_values.csv.gz'

with gzip.open(input_file, 'rt') as csv_in, gzip.open(output_file, 'wt', newline='') as csv_out:
    reader = csv.DictReader(csv_in)
    writer = csv.DictWriter(csv_out, fieldnames=reader.fieldnames + ['s2aff_perdiction'])

    writer.writeheader()  # Write the header to the output file

    for row in reader:
        # checking non-empty raw affiliation string
        if row['affiliation_string']:
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
                    
                    
                    
                    
                    
                    
                    