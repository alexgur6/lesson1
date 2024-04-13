class Human:
    default_name = 'name'
    default_age = '18'
    def __init__(self, name, age, money, house):
        self.name = name
        self.age = age
        self.__money = money
        self.__house = house
    def info(self):
        print(f'Имя: {self.name}')
        print(f'Возраст: {self.age} ')
        print(f': {self.__house}')
        print(f': {self.__money}')
        @staticmethod
        def default_info():
            print(f'Имя: {self.default_name}')
            print(f'Возраст: {self.default_age} ')
    def __make_deal(self, house):

    def earn_money(self):
        self.zp = self.__money*2
    def buy_house(self):
        if self.ostatok >= 0:
            self.



