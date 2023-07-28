#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 13:08:41 2023

@author: aurelasinanaj
"""

# Statistics on matched affiliations with matching ror id in last two keys 

import gzip
import csv
import ast
from tabulate import tabulate
import os


lines = 0
count_ror_pred_09 = 0  # cases with value >= 0.9
count_ror_pred_05_09 = 0
count_ror_pred_00__05 = 0

with gzip.open('cases_matched_4th_5th.csv.gz', 'rt') as file:
    reader = csv.reader(file)
    header = next(reader)

    # column indices
    ror_oa_index = header.index('ror_id')
    ror_pred_index = header.index('s2aff_prediction')

    # iterating over each row in the CSV file
    for line in reader:
        lines += 1
        ror_oa = line[ror_oa_index]
        ror_pred = line[ror_pred_index]
        ror_pred_dict = ast.literal_eval(ror_pred)

        # check if first key's value is >= 0.9
        first_key = list(ror_pred_dict)[0]
        if ror_pred_dict[first_key] >= 0.9:
            count_ror_pred_09 += 1
            
        if ror_pred_dict[first_key] < 0.9 and ror_pred_dict[first_key] > 0.5:
            count_ror_pred_05_09 += 1
            
        if ror_pred_dict[first_key] < 0.5:
            count_ror_pred_00__05 += 1
        


ror_pred_09_p = ( count_ror_pred_09 / lines ) * 100
ror_pred_05_09_p = ( count_ror_pred_05_09 / lines ) * 100
ror_pred_00__05_p = ( count_ror_pred_00__05 / lines ) * 100


table = [
    ["First predictions with value >= 0.9:", count_ror_pred_09,  "{:.2f}%".format(ror_pred_09_p)],
    ["First predictions with value > 0.5 and < 0.9:", count_ror_pred_05_09, "{:.2f}%".format(ror_pred_05_09_p)],
    ["First predictions with value < 0.5:", count_ror_pred_00__05, "{:.2f}%".format(ror_pred_00__05_p)],
    ["Total affiliations:", lines]
]

# Print and save
table_match = tabulate(table, headers=["Count", "Percentage"], tablefmt="pipe")
table_match_2 = tabulate(table, headers=["Count", "Percentage"], tablefmt="latex")
print(table_match)

output_file_matched = "statistics_matched_4_5_keys.tex"
output_path_matched = os.path.join(output_file_matched)

with open(output_path_matched, "w") as f:
    f.write(table_match_2) 

