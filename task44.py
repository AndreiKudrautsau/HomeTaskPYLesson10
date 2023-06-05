class Dragon:
    def __init__(self, height, fireRisk, color):
        self.height = height
        self.fireRisk = fireRisk
        self.color = color
    
    def __gt__(self, other):                 
        return self.height > other.height or self.fireRisk > other.fireRisk or self.color > other.color
    
    def __ne__(self, other):
        return self.height != other.height or self.fireRisk != other.fireRisk or self.color != other.color        
    
    def __le__(self, other):
        return self.height <= other.height or self.fireRisk <= other.fireRisk or self.color <= other.color
            
    def __add__(self, other):
        if type(other) == Dragon:
            height_ch = int((self.height + other.height)/2)
            fireRisk_ch = int(max(self.fireRisk, other.fireRisk))
            color_ch = min(self.color, other.color)
            dr2 = Dragon(height_ch, fireRisk_ch, color_ch)
            return dr2
    
    def __sub__(self, number): 
        if type(number) == int or type(number) == float: 
            self.height =self.height - int(self.height/number)
            self.fireRisk = self.fireRisk + self.fireRisk % number
            return self

    def change_color(self, color):
        self.color = color
        return self
    
    def __repr__(self):
        return f'Dragon({self.height}, {self.fireRisk}, {self. color})'
        
    def __str__(self):
        return f'Dragon with height {self.height}, danger {self.fireRisk} and color {self.color}' 
    
    def __call__(self, string):
        if self.fireRisk !=0:
            return string * self.fireRisk

dr = Dragon(69, 5, 'brown')
dr1 = Dragon(69, 5, 'gray')
print (dr > dr1, dr != dr1, dr <= dr1)
print(dr, dr1, sep="\n")
print()
dr.change_color("white")
dr -= 23
dr1 -= 2
dr2 = dr + dr1
print(dr, dr1, dr2, sep="\n")
print(dr("Welcome"))

# Напишите класс Dragon (Дракон), экземпляр которого при инициализации принимaет аргументы: рост, огнеопасность, цвет.
# Класс обеспечивает выполнение методов (dr — экземпляр класса) экземпляры можно сравнивать: 
# сначала по росту, затем по огнеопасности, затем по цвету по алфавиту
# экземпляры класса можно складывать: dr2 =dr + dr1. при этом возвращается новый экземпляр со значениями атрибутов:
# цвет меньший по алфавиту; рост - среднее арифметическое из двух округлённое до целого вниз,
# огнеопасность - большее из двух;
# из экземпляра класса можно вычесть число: dr -= number, из роста вычитается целая часть от деления роста на число, к
# огнеопасности прибавляется остаток от деления огнеопасности на число;
# Экземпляр можно вызвать с аргументом-строкой - возвращается строка-аргумент, повторенная количество раз, равное
# значению атрибута огнеопасность;
# change_color() - вызывается c аргументом - цветом, на который нужно поменять имеющийся цвет
# str- возвращает строку:
# Dragon with height «рост», danger <огнеопасность> and color «цвет».
# repr- возвращaет строку:
# Dragon(‹рост>, <огнеопасность>, <цвет>)