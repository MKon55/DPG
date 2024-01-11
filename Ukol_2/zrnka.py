import pandas as pd


#Vytvoření prázdného seznamu
seznam = []

#Generování hodnot pro sloupec 'Výsledky'
for i in range(65):
    x = 2**i
    seznam.append(x)

#Vytvoření DataFrame
x = pd.DataFrame(data=seznam, columns=['Výsledky'])

#Výpis prvních 5 řádků
print(x.head())

#Výpis posledních 5 řádků
print(x.tail())

#Uložení výsledků do souboru vysledky.txt
x.to_csv('vysledky.txt', index=False, header=True)
