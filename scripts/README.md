script|order|content|
---|---|---|
dblp_getfiles.py | 1 | Getting the relevant doi link from the dblp database and putting in the file output_dblp_ee.csv.gz |
oa_getfiles.py| 2 | Based on doi link in dblp matched with those in openAlex retrieving only relevant keys 'id','doi','title','authorships','publication_year' after some conditions are met. Diving the data dump in matched and unmatched. |
oa_statistics.py| 3 | Statistics on matched papers|
percentages.py|4|Obtaining data from dblp website on total records + matched records from oa data dump. Obtaining percentages of coverage and plotting|
stage_1.py| 5 | Getting a sample of 10 000 papers to test affiliation matching from the matched files|
stage_2.py| 6 | Creating a table in format csv file from the json file with 10 000 papers with the relevant information needed |
stage_3.py| 7  | Testing the matching using the pretrained model from the s2aff repository|
statistics_5th_4th.py| 8 | Statistics on matched affiliations with matching ror in last two keys |
statistics_less5_mateched.py| 9 | Statistics on affiliations for which less than the expected 5 predictions are made |
statistics_matched.py| 10 | Statistics on matched affiliations |
check.py |11| Checking anomalous data in mached papers (in this case wrong date)|
