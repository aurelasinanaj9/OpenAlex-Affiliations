#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 13:03:33 2023

@author: aurelasinanaj
"""

# Statistics on affiliations for which less than the expected 5 predictions are made

import gzip
import csv
import ast
import os
from tabulate import tabulate

matching_ror = 0
lines = 0
lines_ror = 0
no_matching_ror = 0
matching_ror_first = 0
matching_ror_second = 0
matching_ror_third = 0
matching_ror_fourth = 0
matching_ror_fifth = 0
four_pred = 0
three_pred =  0
two_pred  = 0
one_pred = 0
no_ror = 0
lines_less_than_5 = 0


# looking into the less than 5 predictions made
with gzip.open('cases_less_than_5.csv.gz', 'rt') as new_file:
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
        
        if len(keys) == 1:
            one_pred+=1

            if ror_oa != 'NA':
                lines_ror += 1
                
                if ror_oa in keys[0]:
                    matching_ror_first += 1
                    matching_ror += 1
            
                else:
                    no_matching_ror += 1
            else:
                no_ror +=1
            
        elif len(keys) == 2:
            two_pred+=1

            if ror_oa != 'NA':
                lines_ror += 1
                
                if ror_oa in keys[0]:
                    matching_ror_first += 1
                    matching_ror += 1
                
                elif ror_oa in keys[1]:
                    matching_ror_second += 1
                    matching_ror += 1
        
                else:
                    no_matching_ror += 1
            else:
                no_ror +=1
            
        elif len(keys) == 3:
            three_pred+=1

            if ror_oa != 'NA':
                lines_ror += 1
                
                if ror_oa in keys[0]:
                    matching_ror_first += 1
                    matching_ror += 1
                
                elif ror_oa in keys[1]:
                    matching_ror_second += 1
                    matching_ror += 1
                
                elif ror_oa in keys[2]:
                    matching_ror_third += 1
                    matching_ror += 1
        
                else:
                    no_matching_ror += 1
            else:
                no_ror +=1
            
            
        elif len(keys) == 4:
            four_pred+=1

            if ror_oa != 'NA':
                lines_ror += 1
                
                if ror_oa in keys[0]:
                    matching_ror_first += 1
                    matching_ror += 1
                
                elif ror_oa in keys[1]:
                    matching_ror_second += 1
                    matching_ror += 1
                
                elif ror_oa in keys[2]:
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
    ["Total affiliations", lines],
    ["Only one prediction", one_pred],
    ["Only two predictions", two_pred],
    ["Only three predictions", three_pred],
    ["Only four predictions", four_pred]
]

# Print and save
table_match = tabulate(table, headers=["Count", "Percentage"], tablefmt="pipe")
table_match_2 = tabulate(table, headers=["Count", "Percentage"], tablefmt="latex")
print(table_match)

output_file_matched = "statistics_matched_less_5.tex"
output_path_matched = os.path.join(output_file_matched)

with open(output_path_matched, "w") as f:
    f.write(table_match_2)                
                
                
                
                