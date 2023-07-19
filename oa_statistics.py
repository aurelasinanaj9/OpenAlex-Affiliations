#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 17:22:16 2023

@author: aurelasinanaj
"""

import json
import gzip
import matplotlib.pyplot as plt
import os

from collections import Counter
from tabulate import tabulate


# STATISTICS

# Looking at all present papers
# original = 'part_001.gz'
# all_papers=0
# with gzip.open(original, 'rt') as json_file:
#     for line in json_file:
#         all_papers+=1      
        
        
# unmatched=0
# with gzip.open('unmatched_file.json.gz', 'rt') as json_file:
#     for line in json_file:
#         unmatched+=1        



folder_path = 'output'

matched=0
# unmatched=0
total_papers = 0
total_authors = 0
count_papers_without_ror = 0
ror_counts = Counter()
has_orcid=0
count_papers_with_only_one_ror = 0
ror_count_per_author=0
same_ror_count_author = 0
at_least_1_missing_ror=0
no_ror = 0
publication_years = []
affiliation_yes=0
no_affiliation=0
affiliation_different = 0


for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.startswith('matched'):
            file_path = os.path.join(root, file)

            with gzip.open(file_path, 'rt') as f:
                for line in f:
                    data = json.loads(line)

                    total_papers += 1

                    affiliation_count=0
                    author_count = 0
                    ror_count = 0
                    single_ror=0
        
                    affiliation_count = 0
        
                    publication_year = data.get('publication_year')
                    if publication_year:
                        publication_years.append(publication_year)

                    for authorship in data['authorships']:
                        if 'author' in authorship:
                            total_authors += 1
                            author_count += 1
                
                        if 'orcid' in authorship['author'] and authorship['author']['orcid']:
                            has_orcid += 1
                
                        raw_affiliations = authorship.get('raw_affiliation_strings') or authorship.get(
                                'raw_affiliation_string')
                        if raw_affiliations:
                            affiliation_count +=1 

                        for institution in authorship['institutions']:
                            if 'ror' in institution and institution['ror']:
                    
                                ror = institution['ror']
                                ror_counts[ror] += 1
                    
                                ror_count += 1
                    
                        if ror_count >=1:
                            ror_count_per_author += 1
           
                        if ror_count >= 1: 
                            single_ror += 1         
                
                    if author_count == affiliation_count:
                        affiliation_yes +=1
                    elif affiliation_count == 0:
                        no_affiliation +=1
                    else:
                        affiliation_different +=1        

            
                    if single_ror == 1 and author_count > 1:
                        count_papers_with_only_one_ror += 1 
            
                    if single_ror == author_count:
                        same_ror_count_author +=1
            
                    elif single_ror == 0 :
                        count_papers_without_ror += 1
                    else:
                        at_least_1_missing_ror +=1

# print(f"Number of authorships with more than one 'ror' key: {single_ror}")



year_counts = {year: publication_years.count(year) for year in set(publication_years)}
sorted_years = sorted(year_counts.keys())
print('Sorted years:')
print(sorted_years)
print('\n')
print('Years counts:')
print(year_counts)
print('\n')
max_year = max(year_counts, key=lambda x: year_counts[x])
print("year with the highest count:", max_year)


for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.startswith('matched'):
            file_path = os.path.join(root, file)
            #if os.path.getsize(file_path) == 0:
               #     continue

            with gzip.open(file_path, 'rt') as f:
                    for line in f:
                        data = json.loads(line)
                        if 'publication_year' in data:
                            publication_year = data['publication_year']
                            if publication_year == 1936 or publication_year == 1937 or publication_year == 1938 or publication_year == 1939  or publication_year == 1940 or publication_year == 1941:
                                print(f"File: {file}\nSubfolder: {os.path.basename(root)}\nLine: {line}")




# LINE PLOT
plt.plot(sorted_years, [year_counts[year] for year in sorted_years])
plt.xlabel('Publication Year')
plt.ylabel('Number of Papers')
plt.title('Distribution of Published Papers overt the Years')
plt.xlim(1950,2024)
plt.show()
plt.savefig('plot_1.png')
        
       
# BAR PLOT
plt.bar(sorted_years, [year_counts[year] for year in sorted_years])
plt.xlabel('Publication Year')
plt.ylabel('Number of Papers')
plt.title('Distribution of Published Papers over the Years')
plt.xlim(1950,2024)
plt.show()
plt.savefig('plot_2.png')

        
    

# Calculate the average number of authors per paper
average_authors_per_paper = total_authors / total_papers

# Calculate the percentages
percentage_author_ror = (ror_count_per_author / total_authors) * 100
percentage_paper_noror = (count_papers_without_ror / total_papers) * 100
percentage_affiliation = (affiliation_yes / total_papers) * 100
percentage_author_orcid = (has_orcid / total_authors) * 100
percentage_papers_with_only_one_ror = ( count_papers_with_only_one_ror / total_papers) * 100
percentage_no_affiliation  = ( no_affiliation / total_papers ) * 100
percentage_at_least_1_missing_ror = ( at_least_1_missing_ror / total_papers ) * 100
percentage_same_ror_count_author = ( same_ror_count_author / total_papers ) * 100
percentage_affiliation_different = ( affiliation_different / total_papers ) * 100

# Prepare the table data
table_data = [
    ["Total number of matched papers:",total_papers],
   # ["Total number of unmatched papers:",unmatched],
    ["Total number of authors", total_authors],
    ["Average number of authors per paper:", "{:.2f}".format(average_authors_per_paper)],
    ["Number of authors with at least one 'ror' key:", ror_count_per_author],
    ["Percentage of authors with at least one matching non-empty 'ror' key:", "{:.2f}%".format(percentage_author_ror)],
    ["Papers with no 'ror' key:",count_papers_without_ror],
    ["Percentage of papers without any 'ror' key:", "{:.2f}%".format(percentage_paper_noror)],
    ["Papers with only one 'ror' but more than one 'author':", count_papers_with_only_one_ror],
    ["Percentage of papers with only one 'ror' but more than one 'author':", "{:.2f}%".format(percentage_papers_with_only_one_ror)],
    ["Count of papers with at least one missing 'ror' key:",at_least_1_missing_ror],
    ["Percentage of papers with at least one missing 'ror' key:", "{:.2f}%".format(percentage_at_least_1_missing_ror)],
    ["Count of papers with non missing ror keys (each author has ror key):",same_ror_count_author],
    ["Percentage of papers with non missing ror keys (each author has ror key):", "{:.2f}%".format(percentage_same_ror_count_author)],
    ["Percentage of authors with a non-empty 'orcid':", "{:.2f}%".format(percentage_author_orcid)],
    ["Number of papers for which each author has a 'raw_affiliation_string':", affiliation_yes],
    ["Percentage of papers for which each author has a 'raw_affiliation_string':", "{:.2f}%".format(percentage_affiliation)],
    ["Percentage of papers with no 'raw affiliation string':","{:.2f}%".format(percentage_no_affiliation)],
    ["Count of papers with at least one missing 'raw affiiliation string':",affiliation_different],                                                                                              
    ["Percentage of papers with at least one missing 'raw affiiliation string':","{:.2f}%".format(percentage_affiliation_different)],
    
    # ["Percentage of authors with a non-empty 'raw_affiliation_string'", "{:.2f}%".format(percentage_author_affiliation)],
    # ["Number of authors with an empty 'raw_affiliation_string'", no_affiliation],
    # ["Percentage of authors with an empty 'raw_affiliation_string'", "{:.2f}%".format(percentage_no_affiliation)],
]




# Generate the table
table = tabulate(table_data, headers=["Metric", "Value"], tablefmt="pipe")
table_2 = tabulate(table_data, headers=["Metric", "Value"], tablefmt="latex")

# Display the table
print(table)

# Display the top 10 most common 'ror' keys
top_10_rors = ror_counts.most_common(10)

print("Top 10 most common 'ror' keys:")
table_data_rors = []
for ror, count in top_10_rors:
    percentage = (count / total_authors) * 100
    table_data_rors.append([ror, count, "{:.2f}%".format(percentage)])

table_rors = tabulate(table_data_rors, headers=["ROR", "Count", "Percentage (authors)"], tablefmt="pipe")
table_rors_2 = tabulate(table_data_rors, headers=["ROR", "Count", "Percentage (authors)"], tablefmt="latex")
print("\n")
print(table_rors)


# Save the statistics to a file
output_file = "statistics.txt"
output_path = os.path.join("output", output_file)

output_file_2 = "statistics_2.tex"
output_path_2 = os.path.join("output", output_file_2)

output_file_ror = "statistics_ror.txt"
output_path_ror = os.path.join("output", output_file_ror)

output_file_ror_2 = "statistics_ror_2.tex"
output_path_ror_2 = os.path.join("output", output_file_ror_2)

with open(output_path, "w") as f:
    f.write(table)

    
with open(output_path_2, "w") as f:
    f.write(table_2)

    
with open(output_path_ror, "w") as f:
    f.write(table_rors)

    
with open(output_path_ror_2, "w") as f:
    f.write(table_rors_2)


print("statistics saved.")

