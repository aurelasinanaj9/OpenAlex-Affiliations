#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 22:06:51 2023

@author: aurelasinanaj
"""
import csv
import gzip
import json

# creating the csv file with only the data we need
with gzip.open('output/output.json.gz', 'rt') as f,\
        gzip.open('sample.csv.gz', 'wt') as sample:
            
            writer = csv.writer(sample)
            writer.writerow(['oa_id', 'oa_count', 'affiliation_string', 'ror_id'])  # Header

            for line in f:
                z = 0
                data = json.loads(line) 
                oa_id = data.get('id')

                for authorship in data['authorships']:

                    ror_list = []  # List to store multiple ror values

                    for institution in authorship['institutions']:
                        ror = institution.get('ror')
                        if ror:
                            ror_list.append(ror)
                        else:
                            ror_list.append('NA')


                    raw_affiliations = authorship.get('raw_affiliation_strings') or authorship.get(
                                'raw_affiliation_string')


                    for ror in ror_list:
                        z+=1
                        writer.writerow([oa_id,z, raw_affiliations, ror])
                        
                        
                        
                        
                        
                        
                        
# data1 = {"id": "https://openalex.org/W2740742622", "doi": "https://doi.org/10.1016/j.cor.2018.04.013", "title": "A shortest-path-based approach for the stochastic knapsack problem with non-decreasing expected overfilling costs", "authorships": [{"author_position": "first", "author": {"id": "https://openalex.org/A2136675481", "display_name": "Troels Martin Range", "orcid": "https://orcid.org/0000-0002-5183-6778"}, "institutions": [{"id": "https://openalex.org/I204778367", "display_name": "Norwegian University of Science and Technology", "ror": "https://ror.org/05xg72x27", "country_code": "NO", "type": "education"}, {"id": "https://openalex.org/I4210134581", "display_name": "Hospital South West Jutland", "ror": "https://ror.org/03pzgk858", "country_code": "DK", "type": "healthcare"}], "is_corresponding": None, "raw_affiliation_string": "Department of Industrial Economics and Technology Management, Norwegian University of Science and Technology, Alfred Getz veg 3, Trondheim, NO-7491, Norway; Hospital of South West Jutland and Institute of Regional Health Research, Centre of South West Jutland, University of Southern Denmark, Finsensgade 35, Esbjerg DK-6700, Denmark"}, {"author_position": "middle", "author": {"id": "https://openalex.org/A2668814171", "display_name": "Dawid Kozlowski", "orcid": None}, "institutions": [{"id": None, "display_name": "Institut for Virksomhedsledelse og \u00d8konomi", "ror": None, "country_code": None, "type": None}], "is_corresponding": None, "raw_affiliation_string": "Institut for Virksomhedsledelse og \u00d8konomi"}, {"author_position": "last", "author": {"id": "https://openalex.org/A2156506640", "display_name": "Niels Petersen", "orcid": "https://orcid.org/0000-0001-6272-6059"}, "institutions": [{"id": "https://openalex.org/I177969490", "display_name": "University of Southern Denmark", "ror": "https://ror.org/03yrrjy16", "country_code": "DK", "type": "education"}], "is_corresponding": None, "raw_affiliation_string": "Department of Business and Economics, and COHERE, University of Southern Denmark, Campusvej 55, Odense M, DK-5230, Denmark"}], "publication_year": 2018}

# data2 = {"id": "https://openalex.org/W2740742623", "doi": "https://doi.org/10.1016/j.cor.2018.04.013", "title": "A shortest-path-based approach for the stochastic knapsack problem with non-decreasing expected overfilling costs", "authorships": [{"author_position": "first", "author": {"id": "https://openalex.org/A2136675481", "display_name": "Troels Martin Range", "orcid": "https://orcid.org/0000-0002-5183-6778"}, "institutions": [{"id": "https://openalex.org/I204778367", "display_name": "Norwegian University of Science and Technology", "ror": "https://ror.org/05xg72x27", "country_code": "NO", "type": "education"}, {"id": "https://openalex.org/I4210134581", "display_name": "Hospital South West Jutland", "ror": "https://ror.org/03pzgk858", "country_code": "DK", "type": "healthcare"}], "is_corresponding": None, "raw_affiliation_string": "Department of Industrial Economics and Technology Management, Norwegian University of Science and Technology, Alfred Getz veg 3, Trondheim, NO-7491, Norway; Hospital of South West Jutland and Institute of Regional Health Research, Centre of South West Jutland, University of Southern Denmark, Finsensgade 35, Esbjerg DK-6700, Denmark"}, {"author_position": "middle", "author": {"id": "https://openalex.org/A2668814171", "display_name": "Dawid Kozlowski", "orcid": None}, "institutions": [{"id": None, "display_name": "Institut for Virksomhedsledelse og \u00d8konomi", "ror": None, "country_code": None, "type": None}], "is_corresponding": None, "raw_affiliation_string": "Institut for Virksomhedsledelse og \u00d8konomi"}, {"author_position": "last", "author": {"id": "https://openalex.org/A2156506640", "display_name": "Niels Petersen", "orcid": "https://orcid.org/0000-0001-6272-6059"}, "institutions": [{"id": "https://openalex.org/I177969490", "display_name": "University of Southern Denmark", "ror": "https://ror.org/03yrrjy16", "country_code": "DK", "type": "education"}], "is_corresponding": None, "raw_affiliation_string": "Department of Business and Economics, and COHERE, University of Southern Denmark, Campusvej 55, Odense M, DK-5230, Denmark"}], "publication_year": 2018}


# # Concatenate the dictionaries
# concatenated_data = {}
# concatenated_data.update(data1)
# concatenated_data.update(data2)                        
                        
# with gzip.open("sample_strange.json.gz", "wt") as gz_file:
#     json.dump(concatenated_data, gz_file)                        


    
# with gzip.open('sample_strange.json.gz', 'rt') as f,\
#         gzip.open('sample_strange_output.csv.gz', 'wt') as sample:

#             writer = csv.writer(sample)
#             writer.writerow(['oa_id', 'oa_count', 'affiliation_string', 'ror_id'])  # Header

#             for line in f:
#                 z = 0
#                 data = json.loads(line) 
#                 oa_id = data.get('id')

#                 for authorship in data['authorships']:

#                     ror_list = []  # List to store multiple ror values

#                     for institution in authorship['institutions']:
#                         ror = institution.get('ror')
#                         if ror:
#                             ror_list.append(ror)
#                             z+=1
#                         else:
#                             ror_list.append('NA')
                            

#                     raw_affiliations = authorship.get('raw_affiliation_strings') or authorship.get(
#                                 'raw_affiliation_string')
    

#                     for ror in ror_list:
#                         print(ror)
#                         writer.writerow([oa_id,z, raw_affiliations, ror])
                        


    
    
