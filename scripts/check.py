#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 21:36:36 2023

@author: aurelasinanaj
"""

# checking anomalous data in mached papers (in this case wrong date)

import os
import gzip
import json

folder_path = 'output'

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.startswith('matched'):
            file_path = os.path.join(root, file)

            with gzip.open(file_path, 'rt') as f:
                    for line in f:
                        data = json.loads(line)
                        if 'publication_year' in data:
                            publication_year = data['publication_year']
                            if publication_year == 1951:
                                print(f"File: {file}\nSubfolder: {os.path.basename(root)}\nLine: {line}")



