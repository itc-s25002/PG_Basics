fav_sports = input("好きなスポーツを教えてください: ")

with open("sports.txt","w") as f:
    f.write(fav_sports)
