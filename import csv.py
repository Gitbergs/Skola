import csv
import random

with open('csvrandom.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Random number'])
    
    for x in range (50):
        random_number = random.randint(0,1000)
        writer.writerow ([random_number])
f.close()
