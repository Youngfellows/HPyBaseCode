#1. 询问是否皮肤是白的
a = input("媒婆，她皮肤怎么样(1:红润光泽  2：一般):")

#2. 询问是否够富有
b = input("媒婆，她家产过千万了么(1:是  2：不是):")

#3. 询问是否漂亮
c = input("媒婆，她漂亮么(1:是  2：不是):")

#4. 判断，是否是白富美
if not (a=="1" and b=="1" and c=="1"):
    print("不是白富美")
