# 打开文件 放到变量f中
f = open('../test.txt', 'w', encoding='utf-8')
# 写入hello python
f.write('hello python')
f.close()
# 这种写法打开文件，会自动进行关闭，出了with的缩进，文件会自动关闭
with open('../test.txt', 'a') as i:
    i.write('!\n')
    i.write('!\n')
    i.write('aaaa\n')
    i.write('bbbb\n')
    i.write('cccc\n')
with open('../test.txt') as t:
    temp = t.read()
    # temp = t.readline() 依次逐个按行读取
    print(temp)
