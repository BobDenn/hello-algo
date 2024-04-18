my_str = input('请输入至少七个字：')
#         01234567
# 容器[start:end:step] -> [start,end)
# start 开始位置 如果是0可以省略
# end 结束位置且不包含，若是最后一位，可以省略
# step 步长，如果是一可以省略
print('前三个字是：' + my_str[0:3:1])
print('全部的字是：' + my_str[:7], end=' ')
# python中的print自带换行，不想换行的话使用end=' '解决
# 2 4 6 -> c e g
print("此处承接上一行：" + my_str[2::2])
print(my_str[::2])
# 步长为-1时，反转数组
print("两级反转："+my_str[::-1])
