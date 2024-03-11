nianling=["21","25","21","23","22","20"]
nianling.append(31)
print(nianling)
shuzi=["29","33","30"]
nianling.extend(shuzi)
print(nianling)
jiegu=nianling.pop(0)
print(f"从列表中取出的元素为{jiegu}")
jiegu2=nianling.pop(8)
print(f"取出的最后一个元素为{jiegu2}")
xiabiao=nianling.index(31)
print(xiabiao)
mingzi=0
while mingzi<len(nianling):
    zuiho= nianling [mingzi]
    print(f"{zuiho}")
    mingzi+=1





