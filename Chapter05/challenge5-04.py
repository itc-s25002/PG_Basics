body_shape = {"height":"164cm",
           "weight":"secret"}
like = {"color":"blue",
     "writer":"住野よる"}
sports = {"basketball":"河村勇輝"}

x = input("入力してください ")

if x in body_shape:
    body_shape = body_shape[x]
    print(body_shape)
elif x in like:
    like = like[x]
    print(like)
elif x in sports:
    sports = sports[x]
    print(sports)
else:
    print("見つかりません")
