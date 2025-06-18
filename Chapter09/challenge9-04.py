import csv
title =[["トップガン","卒業白書","マイノリティーリポート"],["タイタニック","レヴェナント","インセプション"],["トレーニング デイ","マイ・ボディーガード","フライト"]]
with open("movie.csv","w",newline="",encoding="utf-8") as f:
    w = csv.writer(f,delimiter=",")
    for i in title:
        w.writerow(i)
