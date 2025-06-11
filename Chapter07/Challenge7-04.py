answer = [8,23,24,35,65,77]

while True:
    num = input("'1~100'までの数字を入力してください。qで終了します。")
    try:
        if num == "q":
            break
        elif int(num) in  answer:
            print("正解！")
        elif int(num) not in answer:
            print("不正解")
    except ValueError:
        print("数字を入力するか、qを入力して終了してください。")
