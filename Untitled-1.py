shuji = "万过薪月,员序程马黑来,nohtyp学"
jiguo = shuji[ ::-1 ]
print(jiguo)
jiguo2 = jiguo[9:14:1]
print(jiguo2)
jiguo3 = shuji.split(",")[1]
jiguo4 = jiguo3.replace("来", " ")
jiguo5 = jiguo4[ : : -1]
print(jiguo5)
my_list = {"黑马程序员","传智播客","黑马程序员","传智播客","itheima","itcast","itheima","itcast","best"}
shui = set()
for shuie in my_list:
    shui.add(shuie[::1])
    print(shui)
    
