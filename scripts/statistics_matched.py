#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:16:43 2023

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
matching_ror_first = 0
matching_ror_second = 0
matching_ror_third = 0
matching_ror_fourth = 0
matching_ror_fifth = 0

with gzip.open('predicted_values.csv.gz', 'rt') as file:
    reader = csv.reader(file)
    header = next(reader)  #skip first row, it is header

    # column indices
    ror_oa_index = header.index('ror_id')
    ror_pred_index = header.index('s2aff_prediction')

    #iterating over each row in csv file
    for line in reader:
        lines += 1
        
        ror_oa = line[ror_oa_index]
        ror_pred = line[ror_pred_index]
        ror_pred_dict = ast.literal_eval(ror_pred)
        
        if ror_oa != 'NA':
            lines_ror += 1

            for key in ror_pred_dict:
                if ror_oa in key:
                    matching_ror += 1

                    if key == list(ror_pred_dict.keys())[0]:
                        matching_ror_first += 1
                    elif key == list(ror_pred_dict.keys())[1]:
                        matching_ror_second += 1
                    elif key == list(ror_pred_dict.keys())[2]:
                        matching_ror_third += 1
                    elif key == list(ror_pred_dict.keys())[3]:
                        matching_ror_fourth += 1
                    elif key == list(ror_pred_dict.keys())[4]:
                        matching_ror_fifth += 1
        else:
            no_matching_ror +=1

# Percentages
no_matching_ror_p = ( no_matching_ror / lines ) * 100
lines_ror_p = ( lines_ror / lines ) * 100
matching_ror_p = ( matching_ror / lines_ror ) * 100
matching_ror_first_p = ( matching_ror_first / matching_ror ) * 100
matching_ror_second_p = ( matching_ror_second / matching_ror ) * 100
matching_ror_third_p = ( matching_ror_third / matching_ror ) * 100
matching_ror_fourth_p = ( matching_ror_fourth / matching_ror ) * 100
matching_ror_fifth_p = ( matching_ror_fifth / matching_ror ) * 100

# table
table = [
    ["Total affiliations without ror value", no_matching_ror,  "{:.2f}%".format(no_matching_ror_p)],
    ["Total affiliations with ror value", lines_ror, "{:.2f}%".format(lines_ror_p)],
    ["Affiliations with matching ror", matching_ror, "{:.2f}%".format(matching_ror_p)],
    ["Affiliations with matching ror (First key)", matching_ror_first, "{:.2f}%".format(matching_ror_first_p)],
    ["Affiliations with matching ror (Second key)", matching_ror_second, "{:.2f}%".format(matching_ror_second_p)],
    ["Affiliations with matching ror (Third key)", matching_ror_third, "{:.2f}%".format(matching_ror_third_p)],
    ["Affiliations with matching ror (Fourth key)", matching_ror_fourth, "{:.2f}%".format(matching_ror_fourth_p)],
    ["Affiliations with matching ror (Fifth key)", matching_ror_fifth, "{:.2f}%".format(matching_ror_fifth_p)],
    ["Total affiliations", lines],
]

# Print and save
table_match = tabulate(table, headers=["Metric", "Count","Percentage"], tablefmt="pipe")
table_match_2 = tabulate(table, headers=["Metric", "Count"], tablefmt="latex")
print(table_match)

output_file_matched = "statistics_matched.tex"
output_path_matched = os.path.join("output", output_file_matched)

with open(output_path_matched, "w") as f:
    f.write(table_match_2)


