import csv

all_articles = []
liked = []
not_liked = []


with open("articles.csv",encoding = "utf-8") as f:
    csvr = csv.reader(f)
    data = list(csvr)
    all_articles.append(data[1:])
