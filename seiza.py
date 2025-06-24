seiza = ["山羊","水瓶","魚","牡羊","牡牛","双子","蟹","獅子","乙女","天秤","蠍","射手","山羊"]
manth = input("生まれた月を入力してください")
manth = int(manth)
day = input("生まれた日にちを入力してください")
day = int(day)
if manth == 1 or 4:
    if int(day) >= 20:
        print(seiza[manth])
    else:
        print(seiza[manth-1])

elif manth == 2:
    if int(day) >= 19:
        print(seiza[manth])
    else:
        print(seiza[manth-1])

elif manth == 3 or 5:
    if int(day) >= 21:
        print(seiza[manth])
    else:
        print(seiza[manth-1])

elif manth == 6 or 12:
    if int(day) >= 22:
        print(seiza[manth])
    elif int(day) < 21:
        print(seiza[manth-1])

elif manth == 7 or 8 or 9 or 11:
    if int(day) >= 23:
        print(seiza[manth])
    else:
        print(seiza[manth-1])

elif manth == 10:
    if int(day) >= 24:
        print(seiza[manth])
    else:
        print(seiza[manth-1])

