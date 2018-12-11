import csv

reader = csv.reader(open('people.csv', 'rb'))
for row in reader:
  print ','.join(row)
  
