#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 13:08:41 2023

@author: aurelasinanaj
"""

import gzip
import csv
import ast
from tabulate import tabulate
import os


matching_ror = 0
lines = 0
lines_ror = 0
no_matching_ror = 0

matching_ror_fourth = 0
matching_ror_fifth = 0




lines = 0
count_ror_pred_09 = 0  # Counter for occurrences with value >= 0.9
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

        # Check if the first key's value is >= 0.9
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



             
with gzip.open('cases_matched_4th_5th.csv.gz', 'rt') as file:
    reader = csv.reader(file)
    header = next(reader)

    # column indices
    ror_oa_index = header.index('ror_id')
    ror_pred_index = header.index('s2aff_prediction')

    #iterating over each row in csv file
    for line in reader:
        lines +=1
        ror_oa = line[ror_oa_index]
        ror_pred = line[ror_pred_index]
        ror_pred_dict = ast.literal_eval(ror_pred)
        
        
                
                if ror_oa in ror_pred_dict:
                    c +=1
                    #print('matched:')
                    #print(line)
                else:
                    no +=1



# NOW LOOKING INTO CASES IN WHICH THE 4TH AND 5TH KEY ARE THE RIGHT ROR ID
with gzip.open('cases_matched_4th_5th.csv.gz', 'rt') as new_file:
    reader = csv.reader(new_file)
    header = next(reader)  # skip first row, it is header

    # column indices
    ror_oa_index = header.index('ror_id')
    ror_pred_index = header.index('s2aff_prediction')

    # iterating over each row in the CSV file
    for line in reader:
        lines += 1

        ror_oa = line[ror_oa_index]
        ror_pred = line[ror_pred_index]
        ror_pred_dict = ast.literal_eval(ror_pred)
        
        keys = list(ror_pred_dict.keys())
        
        if len(keys) == 4 or  len(keys) == 5:

            if ror_oa != 'NA':
                
                if ror_oa in keys[2]:
                    matching_ror_third += 1
                    matching_ror += 1
                
                elif ror_oa in keys[3]:
                    matching_ror_fourth += 1
                    matching_ror += 1
        
                else:
                    no_matching_ror += 1
                    
            else:
                no_ror +=1
                
                
no_matching_ror_p = ( no_ror / lines ) * 100
lines_ror_p = ( lines_ror / lines ) * 100
matching_ror_p = ( matching_ror / lines_ror ) * 100
matching_ror_first_p = ( matching_ror_first / matching_ror ) * 100
matching_ror_second_p = ( matching_ror_second / matching_ror ) * 100
matching_ror_third_p = ( matching_ror_third / matching_ror ) * 100
matching_ror_fourth_p = ( matching_ror_fourth / matching_ror ) * 100


# table
table = [
    ["Total affiliations without ror value", no_ror,  "{:.2f}%".format(no_matching_ror_p)],
    ["Total affiliations with ror value", lines_ror, "{:.2f}%".format(lines_ror_p)],
    ["Affiliations with matching ror", matching_ror, "{:.2f}%".format(matching_ror_p)],
    ["Affiliations with matching ror (First key)", matching_ror_first, "{:.2f}%".format(matching_ror_first_p)],
    ["Affiliations with matching ror (Second key)", matching_ror_second, "{:.2f}%".format(matching_ror_second_p)],
    ["Affiliations with matching ror (Third key)", matching_ror_third, "{:.2f}%".format(matching_ror_third_p)],
    ["Affiliations with matching ror (Fourth key)", matching_ror_fourth, "{:.2f}%".format(matching_ror_fourth_p)],
    ["Total affiliations", lines]
]

# Print and save
table_match = tabulate(table, headers=["Count", "Percentage"], tablefmt="pipe")
table_match_2 = tabulate(table, headers=["Count", "Percentage"], tablefmt="latex")
print(table_match)

output_file_matched = "statistics_matched_less_5.tex"
output_path_matched = os.path.join(output_file_matched)

with open(output_path_matched, "w") as f:
    f.write(table_match_2) 