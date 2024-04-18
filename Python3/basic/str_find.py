# 在一段字符串中查找某段字符，并返回其所在位置
my_str = '黑马程序员'
sub_str = '马'
res = my_str.find(sub_str)
# 若没有找到会返回-1
if res != -1:
    print(f'{sub_str}存在，它在{res}位置')
else:
    print(f"{sub_str}不存在")
