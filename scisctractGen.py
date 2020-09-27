
# To data scrapped from https://arxiv.org/ API.
# Author: TristanCB

import time
import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
import argparse
import kerasCholetTextGenExample

def str2bool(v: str or bool) -> bool:
    """
    Taken from: https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse
    Function which handles string arguments given to argparse to work with bool logic in main program
    """
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

# Accept command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--topic', type=str, help='A topic of your choice', default='Fluids')
parser.add_argument('--outputData', type=str, help='Output filename. Should end with .csv', default='dataTrain.csv')
parser.add_argument('--queryAmnt', type=int, help='Amount of papers returned for single request made with API', default=50)
parser.add_argument('--totalAmnt', type=int, help='Total amount of papers we wish to scan', default=2000)
parser.add_argument('--fromSave', type=str2bool, help='starts example from previously generated .csv file', default=False)

args = parser.parse_args()

# Get vars
topic           = args.topic
outputData      = args.outputData
fromSave        = args.fromSave
amntPerQuery    = args.queryAmnt
total           = args.totalAmnt

# Generate appropriate start indices depending on amount of entries requested
linSpace = [i for i in range(1, total, amntPerQuery)]

# If we do not already have data, use the following loop to scrape data from arxiv.org using provided API
# For more info on API refer to the user manual: https://arxiv.org/help/api/user-manual
if fromSave != True:
    # Append the data to a csv file for future use. 
    with open(outputData, 'w', newline='', encoding="utf-8") as csvfile:
        
        def writeEntry(summary : str, abstract : str):
            """
            Small function to append data
            """
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow([summary,abstract])
        
        # Writes header:
        writeEntry('summary','abstract')

        # Get data in batches
        for start in linSpace:
            # Construct query.
            url = f'http://export.arxiv.org/api/query?search_query=all:{topic}&start={start}&max_results={amntPerQuery}'
            print(f"Extracting data using url: {url}")

            # Get text data from request
            request = requests.get(url).text
            # Soup object to parse out data obtained from the previously made request.
            soup = BeautifulSoup(request,'lxml')
            # Get all papers.
            entries =  soup.find_all('entry')
            # Extract titles and summaries using list comprehension and strip white space.
            titles = [i.title.string.strip("  ").lower() for i in entries]
            summaries = [i.summary.string.strip("  ").lower() for i in entries]

            # Make sure both lengths match
            assert len(titles) == len(summaries)
            
            # Iterates through both lists to append data to csv using function
            for title, summary in zip(titles,summaries):
                writeEntry(summary,title)

# Retrieve data from csv file.
dataTrain = pd.read_csv(outputData)
# Assemble all the text from web scrapped summaries
text = dataTrain[['summary']].sum()[0]

# Use keras example to generate text
kerasCholetTextGenExample.run(text)
