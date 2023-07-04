#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 19:27:16 2023

@author: aurelasinanaj
"""

import os
import gzip
import json

from s2aff.ror import RORIndex
from s2aff.model import NERPredictor, PairwiseRORLightGBMReranker

#creating the path to access each file
folder_path = 'output'

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.startswith('matched'):
            file_path = os.path.join(root, file)

            with gzip.open(file_path, 'rt') as f:
                for line in f:
                    data = json.loads(line)
                    
                    for authorship in data['authorships']:
                            raw_affiliation = authorship.get('raw_affiliation_strings') or authorship.get(
                                'raw_affiliation_string')
                            
                            ner_predictor = NERPredictor(use_cuda=False)
                            ror_index = RORIndex()  
                            pairwise_model = PairwiseRORLightGBMReranker(ror_index)
                            candidates, scores = ror_index.get_candidates_from_raw_affiliation(raw_affiliation, ner_predictor)
                            reranked_candidates, reranked_scores = pairwise_model.predict(raw_affiliation, candidates[:100], scores[:100])

                            # print out the top 5 candidates and scores from the second stage
                            for i, j in zip(reranked_candidates[:5], reranked_scores[:5]):
                                print(ror_index.ror_dict[i]["id"], j)
    
    
    
    