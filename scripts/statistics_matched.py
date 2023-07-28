#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:16:43 2023

@author: aurelasinanaj
"""

# Statistics on ror ids (those outputted from the model and present ones in openAlex)

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
four_pred = 0
three_pred =  0
two_pred  = 0
one_pred = 0
no_ror = 0
lines_less_than_5 = 0



# General statistics

with gzip.open('predicted_values.csv.gz', 'rt') as file:
    reader = csv.reader(file)
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
            lines_less_than_5 +=1
            #cases_less_than_5.append(line)
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
            lines_less_than_5 +=1
            #cases_less_than_5.append(line)
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
            lines_less_than_5 +=1
            #cases_less_than_5.append(line)
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
            lines_less_than_5 +=1
            #cases_less_than_5.append(line)
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
                    #cases_4_5_key.append(line)
        
                else:
                    no_matching_ror += 1
                    
            else:
                no_ror +=1
            
        elif len(keys) == 5:
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
                    #cases_4_5_key.append(line)
                    
                elif ror_oa in keys[4]:
                    matching_ror_fifth += 1
                    matching_ror += 1
                    #cases_4_5_key.append(line)
        
                else:
                    no_matching_ror += 1
            else:
                no_ror +=1
                
            
                  
                    
# Percentages
no_matching_ror_p = ( no_ror / lines ) * 100
lines_ror_p = ( lines_ror / lines ) * 100
matching_ror_p = ( matching_ror / lines_ror ) * 100
matching_ror_first_p = ( matching_ror_first / matching_ror ) * 100
matching_ror_second_p = ( matching_ror_second / matching_ror ) * 100
matching_ror_third_p = ( matching_ror_third / matching_ror ) * 100
matching_ror_fourth_p = ( matching_ror_fourth / matching_ror ) * 100
matching_ror_fifth_p = ( matching_ror_fifth / matching_ror ) * 100
lines_less_than_5_p = ( lines_less_than_5 / lines ) * 100

# table
table = [
    ["Total affiliations without ror value", no_ror,  "{:.2f}%".format(no_matching_ror_p)],
    ["Total affiliations with ror value", lines_ror, "{:.2f}%".format(lines_ror_p)],
    ["Affiliations with matching ror", matching_ror, "{:.2f}%".format(matching_ror_p)],
    ["Affiliations with matching ror (First key)", matching_ror_first, "{:.2f}%".format(matching_ror_first_p)],
    ["Affiliations with matching ror (Second key)", matching_ror_second, "{:.2f}%".format(matching_ror_second_p)],
    ["Affiliations with matching ror (Third key)", matching_ror_third, "{:.2f}%".format(matching_ror_third_p)],
    ["Affiliations with matching ror (Fourth key)", matching_ror_fourth, "{:.2f}%".format(matching_ror_fourth_p)],
    ["Affiliations with matching ror (Fifth key)", matching_ror_fifth, "{:.2f}%".format(matching_ror_fifth_p)],
    ["Affiliations for which less than five predictions has been made", lines_less_than_5, "{:.2f}%".format(lines_less_than_5_p)],
    ["Total affiliations", lines]
]

# Print and save
table_match = tabulate(table, headers=["Count", "Percentage"], tablefmt="pipe")
table_match_2 = tabulate(table, headers=["Count", "Percentage"], tablefmt="latex")
print(table_match)

output_file_matched = "statistics_matched.tex"
output_path_matched = os.path.join(output_file_matched)

with open(output_path_matched, "w") as f:
    f.write(table_match_2)


