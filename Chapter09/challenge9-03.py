import csv
title =[["Top Gun","Risky Buseness","Minority Report"],["Titanic","The Revenant","Inception"],["training Day","Man on Fire","Flight"]]
with open("list.csv","w",newline="") as f:
    w = csv.writer(f,delimiter=",")
    for i in title:
        w.writerow(i)
