#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 20:23:11 2023

@author: aurelasinanaj
"""

# Obtaining data from dblp website on total records + matched records from oa data dump. Obtaining
# percentages and plotting

import matplotlib.pyplot as plt

# data from dblp website
data = [
    (2024, 104),
    (2023, 211340),
    (2022, 465098),
    (2021, 455139),
    (2020, 432093),
    (2019, 416748),
    (2018, 373795),
    (2017, 338707),
    (2016, 314043),
    (2015, 302045),
    (2014, 291752),
    (2013, 280180),
    (2012, 262828),
    (2011, 250306),
    (2010, 228829),
    (2009, 222492),
    (2008, 203352),
    (2007, 189362),
    (2006, 176261),
    (2005, 158118),
    (2004, 135448),
    (2003, 116300),
    (2002, 97619),
    (2001, 86673),
    (2000, 80859),
    (1999, 71054),
    (1998, 64132),
    (1997, 56767),
    (1996, 52757),
    (1995, 47638),
    (1994, 45185),
    (1993, 40542),
    (1992, 34851),
    (1991, 31062),
    (1990, 28141),
    (1989, 23987),
    (1988, 21577),
    (1987, 17494),
    (1986, 16439),
    (1985, 13852),
    (1984, 12294),
    (1983, 10826),
    (1982, 9913),
    (1981, 8634),
    (1980, 7763),
    (1979, 6876),
    (1978, 6753),
    (1977, 5930),
    (1976, 5650),
    (1975, 5213),
    (1974, 4983),
    (1973, 4393),
    (1972, 3707),
    (1971, 3093),
    (1970, 2183),
    (1969, 2089),
    (1968, 2163),
    (1967, 1747),
    (1966, 1481),
    (1965, 1274),
    (1964, 1087),
    (1963, 1017),
    (1962, 1171),
    (1961, 893),
    (1960, 610),
    (1959, 707),
    (1958, 455),
    (1957, 338),
    (1956, 349),
    (1955, 205),
    (1954, 216),
    (1953, 171),
    (1952, 111),
    (1951, 41),
    (1950, 28),
    (1949, 52),
    (1948, 41),
    (1947, 10),
    (1946, 31),
    (1945, 9),
    (1944, 5),
    (1943, 8),
    (1942, 13),
    (1941, 13),
    (1940, 10),
    (1939, 18),
    (1938, 11),
    (1937, 16),
    (1936, 12)
]

# convert the list into dictionary
count_dblp = dict(data)

# from output in script oa_statistics (year_counts variable)
count_oa = {2107: 1, 1800: 1, 1900: 2, 1936: 8, 1937: 7, 1938: 3, 1939: 13, 1940: 6, 1941: 5, 1942: 10, 1943: 5, 1944: 4, 1945: 8, 1946: 6, 1947: 7, 1948: 12, 1949: 16, 1950: 19, 1951: 50, 1952: 51, 1953: 50, 1954: 80, 1955: 72, 1956: 129, 1957: 161, 1958: 257, 1959: 337, 1960: 302, 1961: 418, 1962: 454, 1963: 498, 1964: 496, 1965: 487, 1966: 665, 1967: 686, 1968: 706, 1969: 824, 1970: 776, 1971: 1012, 1972: 1269, 1973: 1363, 1974: 1794, 1975: 1956, 1976: 2278, 1977: 2373, 1978: 2479, 1979: 2527, 1980: 2965, 1981: 3082, 1982: 3378, 1983: 3818, 1984: 4190, 1985: 4653, 1986: 5303, 1987: 6599, 1988: 9166, 1989: 10645, 1990: 9515, 1991: 10745, 1992: 10142, 1993: 12967, 1994: 17271, 1995: 17665, 1996: 18889, 1997: 17122, 1998: 19390, 1999: 22659, 2000: 25989, 2001: 28834, 2002: 29313, 2003: 31666, 2004: 50005, 2005: 67763, 2006: 75596, 2007: 79271, 2008: 82800, 2009: 95148, 2010: 97876, 2011: 107283, 2012: 107559, 2013: 113617, 2014: 122402, 2015: 122405, 2016: 126398, 2017: 134689, 2018: 144136, 2019: 159653, 2020: 165918, 2021: 190896, 2022: 160302, 2023: 10715, 2032: 1}


# extract matching years from both dictionaries and calculate the percentages
percentage = {}
for year in count_dblp:
    if year in count_oa:
        percentage[year] = (count_oa[year] / count_dblp[year]) * 100
    else:
        percentage[year] = 0




years = list(percentage.keys())
percentages = list(percentage.values())

# Create the bar plot year 1936 to 1970
plt.figure(figsize=(12, 6))
plt.bar(years[55:], percentages[55:], color='red', edgecolor='black')
plt.xlabel('Year')
plt.ylabel('Percentage')
plt.title('Percentage of Counts in count_oa relative to count_dblp for each Year')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(years[55::1], rotation=90)
plt.tight_layout()
plt.show()


# Create the bar plot year 1971 to 2023
plt.figure(figsize=(12, 6))
plt.bar(years[:55], percentages[:55], color='skyblue', edgecolor='black')
plt.xlabel('Year')
plt.ylabel('Percentage')
plt.title('Percentage of Counts in count_oa relative to count_dblp for each Year')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(years[:55:1], rotation=90)
plt.tight_layout()
plt.show()



