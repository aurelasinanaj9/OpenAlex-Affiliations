#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 10:33:13 2023

@author: aurelasinanaj
"""

# open compressed file and read line line by line
# to get json object 
# look at record
# line by line
# write compact form
# entire author block (object)
# json renderer
# print line by linne author and doi


# DBLP
import xml.sax
import gzip


# so we have to problems: the compressed file is too big, and we had a problem
# with The error message "undefined entity á: line 14, column 44" indicates 
# that the XML parser encountered an undefined entity reference in the XML file. 
#In this case, the entity reference "á" is not defined in the XML file, which 
#is causing the parser to raise an error.



class MyHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_tag = None
        self.csv_data = []

    def startElement(self, name, attrs):
        self.current_tag = name

    def characters(self, content):
        if self.current_tag == "ee":
            self.csv_data.append(content)

    def save_to_csv(self, filename):
        import csv
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for row in self.csv_data:
                writer.writerow([row])



with gzip.open('dblp.xml.gz', 'rb') as f:
    parser = xml.sax.make_parser()            
    # Set the ContentHandler of the parser to our custom handler
    handler = MyHandler()
    parser.setContentHandler(handler)

    # Parse the XML file incrementally
    context = iter(lambda: f.read(1024*1024), b'')
    for chunk in context:
        parser.feed(chunk)

    # Clear the parser to prevent memory leaks
    parser.close()


handler.save_to_csv('data.csv')

with gzip.open('dblp.xml.gz', 'rt') as f:
    for line in f:
        if line.startswith("<ee>"):
            print(line)
    
    

#22 approx in original file author_position
# PUT IN output
# id , authorships records and doi 
#  wirte again in a compressed file

# read linne,  parse ons extract data and dwrite it (incnrementally)
#add title too
# if no doi do not write out
# display  name adn  title
# versiion control system

