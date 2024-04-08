class HouseItem:
    def __init__(self, name, area):
        """带有名字和面积的家具"""
        self.name = name
        self.area = area

    def __str__(self):
        return f"{self.name}占地{self.area}平米"


class House:
    def __init__(self, h_type, area):
        """户型，总面积，剩余面积，家具列表"""
        self.h_type = h_type
        self.total_area = area
        self.free_area = area
        self.list = []

    def add_item(self, item):
        # 形参item是家具对象，self是房子本身
        if self.free_area > item.area:
            print(f'添加家具：{item.name}')
            self.list.append(item.name)
            self.free_area -= item.area
        else:
            print("请尽快换个大房子吧！")

    def __str__(self):
        return (f"{self.h_type}总面积为{self.total_area}平米，"
                f"剩余面积{self.free_area}平米，家具有：{self.list}")


if __name__ == '__main__':
    # 定义家具
    bed = HouseItem('席梦思', 4)
    chest = HouseItem('衣柜', 2)
    table = HouseItem('餐桌', 1.5)
    # 定义房子
    my_house = House('我的房子', 100)
    # print(my_house)
    my_house.add_item(bed)
    my_house.add_item(table)
    print(my_house)
