def change_float(a):
    try:
       print(float(a))
    except ValueError:
        print("整数または、少数点数を入力してください。")
""""
受け取った引数をfloat型に変換し、ValueErrorが起こった際は(整数または、少数点数を入力してください。)と出力する関数
"""

change_float(8)
change_float("よん")
