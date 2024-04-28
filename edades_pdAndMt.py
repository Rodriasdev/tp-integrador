import csv
from datetime import datetime 
import pandas as pd
import matplotlib.pyplot as plt

with open('edades.csv', newline='') as file:
    lector_csv = csv.reader(file, delimiter=',',quotechar='"')

    edades=[]
    now = datetime.now()

    for row in lector_csv:
        barra = 0
        fecha = row[0][-4:]
        if fecha != 'age':
            if now.year - int(fecha) > 25:
                edades.append(now.year - int(fecha))

    
edades.sort()
    
data = pd.Series(edades)
df = pd.DataFrame({'edades':dict(data.value_counts()).keys(),'fi': dict(data.value_counts()).values()})


plt.plot(df['edades'], df['fi'])
plt.ylabel('fi')
plt.xlabel('edades')
plt.show()




