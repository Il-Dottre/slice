# 编写Python程序，压缩语句“我很是好好好好好好呀”内重复的字，结果为“我很是好呀”。

a='我很是好好好好好好呀'

a_1 = ""

for i in a:

    if i not in a_1:

        a_1 +=i

print(a_1)