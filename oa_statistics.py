#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 17:22:16 2023

@author: aurelasinanaj
"""

import json
import gzip
import matplotlib.pyplot as plt

from collections import Counter
from tabulate import tabulate


# STATISTICS

# Looking at matched and unmateched works
matched=0
with gzip.open('matched_file.json.gz', 'rt') as json_file:
    for line in json_file:
        matched+=1
#27784
         
unmatched=0
with gzip.open('unmatched_file.json.gz', 'rt') as json_file:
    for line in json_file:
        unmatched+=1
#617806         



file = 'matched_file.json.gz'


total_papers = 0
total_authors = 0
count_papers_without_ror = 0
ror_counts = Counter()
has_orcid=0
count_papers_with_only_one_ror = 0
ror_count_per_author=0
affiliation_count = 0
no_affiliation = 0
at_least_one_missing_ror = 0
same_ror_count_author = 0
at_least_1_missing_ror=0
no_ror = 0


with gzip.open(file, 'rt') as f:
    for line in f:
        data = json.loads(line)

        total_papers += 1

        has_ror = False
        author_count = 0
        ror_count = 0
        single_ror=0

        for authorship in data['authorships']:
            if 'author' in authorship:
                total_authors += 1
                author_count += 1
                
            if 'orcid' in authorship['author'] and authorship['author']['orcid']:
                has_orcid += 1
                

            for institution in authorship['institutions']:
                if 'ror' in institution and institution['ror']:
                    has_ror = True
                    
                    ror = institution['ror']
                    ror_counts[ror] += 1
                    
                    ror_count += 1
           
            if ror_count > 1: 
                single_ror += 1         

        if not has_ror:
            count_papers_without_ror += 1
            #print(data)
            
        if ror_count >=1:
            ror_count_per_author += 1
            
        if ror_count == 1 and author_count > 1:
            count_papers_with_only_one_ror += 1 
            
        if single_ror == author_count:
            same_ror_count_author +=1
            
        elif single_ror == 0 :
            no_ror +=1
        else:
            at_least_1_missing_ror +=1



same_ror_count_author = 0
at_least_1_missing_ror=0
no_ror = 0
pap = 0
with gzip.open(file, 'rt') as f:
    for line in f:
        data = json.loads(line)

        has_ror = False
        author_count=0
        single_ror=0
        pap += 1

        for authorship in data['authorships']:
            if 'author' in authorship:
                author_count += 1

                for institution in authorship['institutions']:
                    if 'ror' in institution and institution['ror']:
                        has_ror = True
                        break  # Break the loop once a single "ror" key is found for an author
            single_ror += 1 if has_ror else 0
                
        if single_ror == author_count:
            same_ror_count_author +=1
        elif single_ror == 0 :
            no_ror +=1
        else:
            at_least_1_missing_ror +=1




    



u = 0
with gzip.open(file, 'rt') as f:
    for line in f:
        data = json.loads(line)

        has_ror = 0  # Counter for 'ror' keys in each authorship

        for authorship in data['authorships']:
            if 'author' in authorship:
                for institution in authorship['institutions']:
                    if 'ror' in institution and institution['ror']:
                        has_ror += 1

        if has_ror > 1:
            u += 1

print(f"Number of authorships with more than one 'ror' key: {u}")



with gzip.open(file, 'rt') as f:
    for line in f:
        data = json.loads(line)

        for authorship in data['authorships']:
            if 'raw_affiliation_string' in authorship and authorship['raw_affiliation_string']:
                affiliation_count +=1
            else: 
                no_affiliation +=1

        
            
            
# with gzip.open(file, 'rt') as f:
#     for line in f:
#         data = json.loads(line)

#         total_papers += 1

#         has_ror = False
#         author_count = 0
#         ror_count = 0

#         for authorship in data['authorships']:
#             if 'author' in authorship:
#                 total_authors += 1
#                 author_count += len(authorship['author'])
                
#             if 'orcid' in authorship['author'] and authorship['author']['orcid']:
#                 has_orcid += 1
                
#             if 'raw_affiliation_string' in authorship and authorship['raw_affiliation_string']:
#                 count_authors_with_affiliation += 1

#             ror_found = False  # Flag to track if "ror" key is found for an author

#             for institution in authorship['institutions']:
#                 if 'ror' in institution and institution['ror']:
#                     count_authors_with_ror += 1
#                     has_ror = True
#                     ror_found = True
#                     ror_count += 1  # Increment ror_count for each "ror" key found

#             if ror_found:
#                 break  # Break the loop if a "ror" key is found for the current author

#         if not has_ror:
#             count_papers_without_ror += 1
#             #print(data)
            
#         if ror_count == 1 and author_count > 1:
#             count_papers_with_only_one_ror += 1

#         ror_counts += ror_count  # Increment ror_counts by ror_count

# # Get the top 10 "ror" keys based on absolute count
# top_10_ror_keys = ror_counts.most_common(10)            
            

            
            
            
            
            


file_t = 'matched_file_time.json.gz'    
        
publication_years = []

with gzip.open(file_t, 'rt') as f:
    for line in f:
        data = json.loads(line)
        publication_year = data.get('publication_year')
        if publication_year:
            publication_years.append(publication_year)

 
# LINE PLOT
year_counts = {year: publication_years.count(year) for year in set(publication_years)}
sorted_years = sorted(year_counts.keys())



plt.plot(sorted_years, [year_counts[year] for year in sorted_years])
plt.xlabel('Publication Year')
plt.ylabel('Number of Papers')
plt.title('Distribution of Published Papers over Years')
plt.show()
        
       
# BAR PLOT
plt.bar(sorted_years, [year_counts[year] for year in sorted_years])
plt.xlabel('Publication Year')
plt.ylabel('Number of Papers')
plt.title('Distribution of Published Papers over Years')
plt.show()

        
    

# Calculate the average number of authors per paper
average_authors_per_paper = total_authors / total_papers

# Calculate the percentages
percentage_author_ror = (ror_count_per_author / total_authors) * 100
percentage_paper_noror = (count_papers_without_ror / total_papers) * 100
percentage_author_affiliation = (affiliation_count / total_authors) * 100
percentage_author_orcid = (has_orcid / total_authors) * 100
percentage_papers_with_only_one_ror = ( count_papers_with_only_one_ror / total_papers) * 100
percentage_no_affiliation  = ( no_affiliation / total_authors ) * 100

# Prepare the table data
table_data = [
    ["Total number of matched papers:",matched],
    ["Total number of unmatched papers:",unmatched],
    ["Total number of authors", total_authors],
    ["Average number of authors per paper", "{:.2f}".format(average_authors_per_paper)],
    ["Number of authors with at least one 'ror' key", ror_count_per_author],
    ["Percentage of authors with at least one matching non-empty 'ror' key", "{:.2f}%".format(percentage_author_ror)],
    ["Papers with only one 'ror' but more than one 'author':", count_papers_with_only_one_ror],
    ["Percentage of papers with only one 'ror' but more than one 'author':", "{:.2f}%".format(percentage_papers_with_only_one_ror)],
    ["Percentage of authors with a non-empty 'orcid'", "{:.2f}%".format(percentage_author_orcid)],
    ["Number of papers without any 'ror' key", count_papers_without_ror],
    ["Percentage of papers without any 'ror' key", "{:.2f}%".format(percentage_paper_noror)],
    ["Number of authors with a non-empty 'raw_affiliation_string'", affiliation_count],
    ["Percentage of authors with a non-empty 'raw_affiliation_string'", "{:.2f}%".format(percentage_author_affiliation)],
    ["Number of authors with an empty 'raw_affiliation_string'", no_affiliation],
    ["Percentage of authors with a non-empty 'raw_affiliation_string'", "{:.2f}%".format(percentage_no_affiliation)],
]




# Generate the table
table = tabulate(table_data, headers=["Metric", "Value"], tablefmt="pipe")

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
print(table_rors)










