#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 19:27:16 2023

@author: aurelasinanaj
"""

import gzip
from datetime import datetime
import csv

from s2aff.ror import RORIndex
from s2aff.model import NERPredictor, PairwiseRORLightGBMReranker

    

# open the input CSV file and create an output csv file
input_file = 'cropped.csv.gz'
output_file = 'predicted_values_cropped.csv.gz'
            

ner_predictor = NERPredictor(use_cuda=False)
ror_index = RORIndex()
pairwise_model = PairwiseRORLightGBMReranker(ror_index)

                   
with gzip.open(input_file, 'rt') as csv_in, gzip.open(output_file, 'wt', newline='') as csv_out:
    reader = csv.DictReader(csv_in)
    writer = csv.DictWriter(csv_out, fieldnames=reader.fieldnames + ['s2aff_prediction'])

    writer.writeheader()  # write the header for the output file

    line_count = 0
    print_count = 100  # count for printing date and time, every 100 lines

    for row in reader:
        # checking non-empty raw affiliation string
        affiliation_string = row['affiliation_string'].strip() # if there is a space at beginning of string the code does not work
        if affiliation_string:

            try:
                candidates, scores = ror_index.get_candidates_from_raw_affiliation(affiliation_string, ner_predictor)
                reranked_candidates, reranked_scores = pairwise_model.predict(affiliation_string, candidates[:100], scores[:100])

                # process the computed values and update the corresponding row
                s2aff_prediction = {}
                for i, j in zip(reranked_candidates[:5], reranked_scores[:5]):
                    s2aff_prediction[ror_index.ror_dict[i]['id']] = j

                row['s2aff_prediction'] = s2aff_prediction
                writer.writerow(row)

            except ValueError:
                # Handle the ValueError and continue to the next iteration
                continue


        line_count += 1

        if line_count % print_count == 0:
            print(f"Lines written: {line_count} - date and time: {datetime.now()}")

print("End.")                


                    
