a = input()

a = a.replace("c=", "ㄱ")
a = a.replace("c-", "ㄴ")
a = a.replace("dz=", "ㄷ")
a = a.replace("d-", "ㄹ")
a = a.replace("lj", "ㅁ")
a = a.replace("nj", "ㅂ")
a = a.replace("s=", "ㅅ")
a = a.replace("z=", "ㅇ")

b = len(a)
print(b)
