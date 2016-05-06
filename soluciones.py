## Ingresos

for ingreso in ingresos:
    if int(ingreso[1]) < 100:
        print(ingreso[0], "tiene un ingreso de", ingreso[1], "y es sospechoso.")
    if int(ingreso[1]) > 100000:
        print(ingreso[0], "tiene un ingreso de", ingreso[1], "y es sospechoso.")

## Better solution
%matplotlib inline

import pandas as pd
df = pd.read_csv('ingresos.csv', names=['name', 'income'], header=None)
df[(df['income'] < 100) | (df['income'] > 100000)]

## Escritora

def parse_escritora(escritora):
    '''
    Devuelve Nombre y Apellido de la escritora
    '''
    arr = escritora.split(",")
    return arr[1].strip(), arr[0]

for escritora in escritoras:
    print(parse_escritora(escritora))
