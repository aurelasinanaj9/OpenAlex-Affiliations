# OpenAlex Affiliations
 
The main goal is to create a system that reads and selects relevant data from the openAlex data dump obtaining a relevant dataset (in this case all the information on the works have been narrowed down and selected based on the doi link matches with those present in the dblp database). After this is done, the system goes through each file created (more specifically only looking into the matched papers) and looks into the matching of the affiliation strings in the openAlex data dump by comparing these to a pretrained model that enables to give ror id predictions given raw affiliation strings (s2aff repository).

In the folder scripts there are the scripts used in this project.
