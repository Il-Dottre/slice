# 求100~999之间所有的水仙花数。
# 水仙花数是指一个n位数（n>=3），它的每个位上的数值的n次幂之和等于它本身。
# 例如：1**3+5**3+3**3=153。
for i in range(100,1000):
    sum = 0
    temp = i


#编写一个Python程序，设定输入的单词个数，并返回其中长度最长的单词。
def find_longest_length(my_list):
    max_length = len(my_list[0])
    temp = my_list[0]
    for element in my_list:
        if(len(element) > max_length):
            max_length = len(element)
            temp = elementtemp
count
    return =int(input("请输入单词个数："))
my_list=[]
for i in range(count):
    print("请输入第%d个单词："%(i+1))
    my_list.append(input())
print(find_longest_length(my_list))