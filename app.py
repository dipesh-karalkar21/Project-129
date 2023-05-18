import pandas as pd
import csv

df = pd.read_csv("brown_dwarf.csv")
df = df[df["distance"].notna()]
df = df[df["mass"].notna()]
df = df[df["radius"].notna()]

del df["Unnamed: 0"]

df.to_csv('brown_dwarf1.csv')

rows1 = []

f = open("brown_dwarf1.csv","r")
csvreader = csv.reader(f)
for row in csvreader:
    rows1.append(row)

data1 = rows1[1:]

for i in data1:
    i[3] = float(i[3])*0.102763
    i[4] = float(i[4])*0.000954588

rows2 = []

f = open("bright_stars.csv","r")
csvreader = csv.reader(f)
for row in csvreader:
    rows2.append(row)

data2 = rows2[1:]
header = ["","Name","Distance","Mass","Radius"]

with open("final.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(data2)
    csvwriter.writerows(data1)
