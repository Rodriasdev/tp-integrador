import csv
from datetime import datetime 

with open('edades.csv', newline='') as file:
    lector_csv = csv.reader(file, delimiter=',',quotechar='"')

    personas=[]
    now = datetime.now()

    for row in lector_csv:

        barra = 0
        fecha = ''

        for i in range(len(row[0])):
            if (row[0])[i]  == '/':
                barra = barra + 1

            if barra == 2:
                fecha = fecha + (row[0])[i]
        
        # if now.year - int(fecha.replace('/', '')) >= 25:
        a = fecha.replace('/', '')
        print(a)



