import json
import os
import csv

# Найдите информацию об организациях:
# Получите список ИНН из файла «traders.txt»;
# Найдите информацию об организациях с этими ИНН в файле «traders.json»;
# Сохраните информацию об ИНН, ОГРН и адресе организаций из файла «traders.txt» в файл «traders.csv».

trInn = []

f = open("traders.txt", "r")
for i in f:
    trInn.append(f.readline())







l = open("traders.json", "r")
data = json.load(l)



c = 0
p= 0

os.remove("D:/Studying/Uni/traders.csv")

while(c <= len(trInn)-1):
    for i in data:

        if int(i["inn"])  == int(trInn[c]):
            csvF = []
            csvF.append(i["inn"])
            csvF.append(i["ogrn"])
            csvF.append(i["address"])
            with open('D:/Studying/Uni/traders.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow(csvF)


            p += 1

    c += 1

with open("D:/Studying/Uni/traders.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    print(row)

