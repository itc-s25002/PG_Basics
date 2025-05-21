def half(x):
    return x // 2
""""
整数を引数として受け取り２で割る関数
必須引数----x
"""
def four(num):
    return num * 4
""""
整数を引数として受け取り４を掛ける関数
必須引数----num(half(x)の出力結果)
"""
num = half(4)
result = four(num)
print(result)
