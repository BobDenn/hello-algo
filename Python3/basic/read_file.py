# 按行读取
"""
with open('../test.txt') as b:
    while True:
        buf = b.readline()
        if buf:
            print(buf, end='')
        else:
            break
"""
import json


with open('test.json', encoding='utf-8') as j:
    look = json.load(j)
    print(type(look))
    print(look)
    # 姓名
    print(look.get('name'))  # 获得一个属性值
info = {'name': '邓阔', 'age': '24'}
with open('write.json', 'w', encoding='utf-8') as jn:
    json.dump(info, jn, ensure_ascii=False, indent=2)   # ensure_ascii直接显示中文,indent缩进2格
