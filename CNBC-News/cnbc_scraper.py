"""
File that will host your implementation for scraping CNN articles for today!
"""

import csv
from bs4 import BeautifulSoup
import requests

def generate_csv():
    link = 'https://www.cnbc.com/world/?region=world'
    page = requests.get(link)
    soup=BeautifulSoup(page.text,'html.parser')

    headline_news = soup.find_all("a", attrs={'class': 'LatestNews-headline'})

    words = []
    words = stripper(headline_news, words)

    freq = {}
    freq = dic(words, freq)

    create_csv(freq)

def stripper(provided, ret):
    stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 
    'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she',
    'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs'
    'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 
    'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have',  'has', 'had',
    'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'but', 'if', 'or',
    'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about',
    'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above',
    'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under',
    'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why',
    'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some',
    'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very',
    's', 't', 'can', 'will', 'just', 'don', 'should', 'now']
    
    for element in provided:
        for unmarked in element:
            string = str(unmarked).split()
            if (len(string) != 0 and string[0] != "<a"):
                for word in string:
                    word = word.strip(' ”,‘—\"\'[],?!1234567890$%-:')
                    word = word.lower()
                    if (len(word) > 1 and word not in stop_words):
                        ret.append(word)
                    
    return ret

def dic(provided, ret):
    for element in provided:
        if element not in ret:
            ret[element] = 1
        else:
            ret[element] += 1
    
    return ret

def create_csv(provided):
    fields = ['Word', 'Frequency']
    with open('/tmp/Frequencies.csv', 'w', newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()

        for word in provided:
            freq = provided[word]
            csvfile.write("%s,%s\n"%(word, freq))

if __name__ == '__main__':
    generate_csv()