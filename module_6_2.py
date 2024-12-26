class Vehicle: # класс ТРАНСПОРТ

    __COLOR_VARIANTS = ["black", "white", "red", "blue", "green"]  # список неизменяемых цветов (атрибутов) класса ТРАНСПОРТ

    def __init__(self,owner,model,color,engine_power,):  # функция создания объекта
        self.owner = owner  # изменяемый атрибут ВЛАДЕЛЕЦ
        self.__model = model  # неизменяемый атрибут МОДЕЛЬ
        self.__color = color  # неизменяемый атрибут ЦВЕТ
        self.__engine_power = engine_power  # неизменяемый атрибут МОЩНОСТЬ

    def get_model(self):  # функция возвращения МОДЕЛИ
        return(f"Модель: {self.__model}")  #

    def get_horsepower(self):  # функция возвращения МОЩНОСТЬ
        return(f"Мощность двигателя: {self.__engine_power}")  #

    def get_color(self):  # функция возвращения ЦВЕТА
        return (f"Цвет: {self.__color}")  #

    def print_info(self):  # Функция вывода ХАРАКТЕРИСТИК
        print(self.get_model())  # МОДЕЛЬ
        print(self.get_horsepower())  # МОЩНОСТЬ
        print(self.get_color())  # ЦВЕТ
        print(f"Владелец: {self.owner}")  # ВЛАДЕЛЕЦ

    def set_color(self, new_color):  # функция смены ЦВЕТА
        if new_color.lower() in map(str.lower, self.__COLOR_VARIANTS): #  если новый ЦВЕТ (приводим цвета в нижний регистр) содержится в списке ВАРИАНТЫ ЦВЕТОВ
            self.__color = new_color #  заменить ЦВЕТ на НОВЫЙ ЦВЕТ
        else:  # иначе
            print(f"Нельзя сменить цвет на {new_color}")  # вывести ...

class Sedan(Vehicle): # класс СЕДАН

    __PASSENGERS_LIMIT = 5 # неизменяемый атрибут класса СЕДАН

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()