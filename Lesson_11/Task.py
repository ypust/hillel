class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        discount_price = self._price - discount
        return discount_price


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(area=40, price=price)


class Human:
    default_name = "User"
    default_age = 25

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("House:", self.__house)
        print("Money:", self.__money)

    @staticmethod
    def default_info():
        print("Default Name:", Human.default_name)
        print("Default Age:", Human.default_age)

    def __make_deal(self, house: House, price: int):
        self.__money -= price
        self.__house = house

    def earn_money(self, amount):
        self.__money += amount

    def buy_house(self, house, discount):
        discounted_price = house.final_price(discount)
        if self.__money >= discounted_price:
            self.__make_deal(house, discounted_price)
        else:
            print('Not enough money for the purchase')


if __name__ == '__main__':
    """ Викличте довідковий метод default_info() для класу Human() """
    Human.default_info()

    """ Створіть об'єкт класу Human
    Виведіть довідкову інформацію про створений об'єкт (викличте метод info()). """
    human = Human('Liza', 30)
    human.info()

    """ Створіть об'єкт класу SmallHouse """
    house_obj = SmallHouse(400)

    """ Спробуйте купити створений будинок, переконайтеся в отриманні попередження. """
    human.buy_house(house_obj, 25)

    """ Виправте фінансове становище об'єкта - викличте метод earn_money() """
    human.earn_money(375)

    """Знову спробуйте купити будинок"""
    human.buy_house(house_obj, 25)

    """Подивіться, як змінилося стан об'єкта класу Human"""
    human.info()
