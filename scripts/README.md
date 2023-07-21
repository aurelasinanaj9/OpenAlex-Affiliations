script|order|content|
---|---|---|
dblp_getfiles.py | 1 | Getting the relevant doi link from the dblp database and putting in the file output_dblp_ee.csv.gz |
oa_getfiles.py| 2 | Based on doi link in dblp matched with those in openAlex retrieving only relevant keys 'id','doi','title','authorships','publication_year' after some conditions are met. Diving the data dump in matched and unmatched. |
oa_statistics.py| 3 | Statistics on matched papers|
stage_1.py| 4 | Getting a sample of 10 000 papers to test affiliation matching from the matched files|
stage_2.py| 5 | Creating a table in format csv file from the json file with 10 000 papers with the relevant information needed |
stage_3.py| 6 | Testing the matching using the pretrained model from the s2aff repository|
statistics_5th_4th.py| 7 | Statistics on matched affiliations with matching ror in last two keys |
statistics_less5_mateched.py| 8 | Statistics on affiliations for which less than the expected 5 predictions are made |
statistics_matched.py| 9 | Statistics on matched affiliations |
