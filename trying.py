#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 11:51:38 2023

@author: aurelasinanaj
"""
import csv
import gzip

links_string = "https://ror.org/03v4gjf40: 0.9642511140008722, https://ror.org/02dh8ja68: 0.3605064345581436, https://ror.org/046ak2485: 0.30996120985424835, https://ror.org/01hcx6992: 0.2570931984767241, https://ror.org/02kkvpp62: 0.12383823424942879"

links = links_string.split(",")  # Split the string using the comma delimiter

for link in links:
    link_parts = link.strip().split(":")  # Split each link into its parts using the colon delimiter
    if len(link_parts) == 2:
        url = link_parts[0].strip()
        value = float(link_parts[1].strip())
        print("URL:", url)
        print("Value:", value)
        print("---")
        
        
with gzip.open('predicted_values_old.csv.gz', 'rt') as file:
    reader = csv.reader(file)
    for row in reader:
        fourth_column_value = row[3]  # Access the fourth column (index 3)
        links = fourth_column_value.split(",")
        for link in links:
            link_parts = link.strip().split(":")  # Split each link into its parts using the colon delimiter
            
            url = link_parts[0].strip()
            value = float(link_parts[1].strip())
            print("URL:", url)
            print("Value:", value)
            print("---")        