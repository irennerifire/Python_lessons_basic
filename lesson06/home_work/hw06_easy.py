# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
print("Task 1: ")
import math as m

class Triangle:
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2=2, x3 = 0, y3=0):
        self.a1 = [x1, y1]
        self.a2 = [x2, y2]
        self.a3 = [x3, y3]

    def dlina_storon(self):
        a1a2 = m.sqrt(abs(pow((self.a2[0]-self.a1[0]), 2)-pow((self.a2[1]-self.a1[1]), 2)))
        a2a3 = m.sqrt(abs(pow((self.a3[0]-self.a2[0]), 2)-pow((self.a3[1]-self.a2[1]), 2)))
        a1a3 = m.sqrt(abs(pow((self.a3[0]-self.a1[0]), 2)-pow((self.a3[1]-self.a1[1]), 2)))
        return a1a2, a2a3, a1a3

    def perimetr(self):
        storona1, storona2, storona3 = Triangle.dlina_storon(self)
        p = storona1 + storona2 + storona3
        return p

# Площадь вычисляем по формуле Герона через периметр
    def square(self):
        storona1, storona2, storona3 = Triangle.dlina_storon(self)
        p = Triangle.perimetr(self)
        S = m.sqrt(p*(p - storona1)*(p - storona2)*(p - storona3))
        return S

    def height(self):
        storona1, storona2, storona3 = Triangle.dlina_storon(self)
        S = Triangle.square(self)
        h1 = 2*S/storona1
        h2 = 2*S/storona2
        h3 = 2*S/storona3
        #print(f"For adge with length {storona} height is   {h}")
        return h1, h1, h3

tr1 = Triangle(x1 = 3, y1 = 4, x2 = 1, y2 = 3, x3 = 4, y3 = 7)
length = tr1.dlina_storon()
perimetr = tr1.perimetr()
square = tr1.square()
heights = tr1.height()
print(f"Length is: {length}")
print(f"Perimeter: {perimetr}")
print(f"Square is: {square}")
print(f"Heights for 3 adges are: {heights}")


# Задача-2: Написать Класс "Равнобедренная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
print("Task 2: ")

class Trapecia:
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2=2, x3 = 0, y3=0, x4 = 0, y4=0):
        self.a1 = [x1, y1]
        self.a2 = [x2, y2]
        self.a3 = [x3, y3]
        self.a4 = [x4, y4]

    def dlina(self):
        a1a2 = m.sqrt(abs(pow((self.a2[0]-self.a1[0]), 2)-pow((self.a2[1]-self.a1[1]), 2)))
        a2a3 = m.sqrt(abs(pow((self.a3[0]-self.a2[0]), 2)-pow((self.a3[1]-self.a2[1]), 2)))
        a3a4 = m.sqrt(abs(pow((self.a4[0]-self.a3[0]), 2)-pow((self.a4[1]-self.a3[1]), 2)))
        a4a1 = m.sqrt(abs(pow((self.a1[0]-self.a4[0]), 2)-pow((self.a1[1]-self.a4[1]), 2)))
        return a1a2, a2a3, a3a4, a4a1

    def per(self):
        storona1, storona2, storona3, storona4 = Trapecia.dlina(self)
        p = storona1 + storona2 + storona3
        return p

# Площадь трапеции по четырем сторонам - нужно знать, какие стороны параллельны
#S = (b+d)/2*sqrt(a**2 - (((d-b)**2+a**2-c**2)/2*(d-b))**2)     b || d
    def sq(self):
        osn = Trapecia.parall(self)
        dlina = Trapecia.dlina(self)
        osn_value = []
        for el in osn:
            if el == "a1a2":
                osn_value.append(dlina[0])
            elif el == "a2a3":
                osn_value.append(dlina[1])
            elif el == "a3a4":
                osn_value.append(dlina[2])
            elif el == "a4a1":
                osn_value.append(dlina[3])
        print("Значения длин параллельных оснований:     ", osn_value)
        print(dlina)
        ocn_b = osn_value[0]
        ocn_d = osn_value[1]
        notparal = []
        for el2 in dlina:
            if el2 != ocn_b and el2 != ocn_d:
                notparal.append(el2)
        ocn_a = notparal[0]
        ocn_c = notparal[1]
        print(notparal)
        S_trap = (ocn_b+ocn_d)/2*(m.sqrt(abs(pow(ocn_a,2) - pow((pow((ocn_d-ocn_b), 2)+pow(ocn_a, 2)-pow(ocn_c, 2)/2*(ocn_d-ocn_b)), 2))))
        return S_trap

#Трапеция - фигура, у которой 2 стороны параллельны
#Параллельность можно определеить по угловым коэффициентам k = (y2 - y1)/(x2 - x1)
    def coeff(a, b):
        coef = abs((b[1]-a[1])/(b[0]-a[0]))
        return coef

    def parall(self):
        ca1a2 = Trapecia.coeff(self.a1, self.a2)
        ca3a4 = Trapecia.coeff(self.a3, self.a4)
        ca2a3 = Trapecia.coeff(self.a2, self.a3)
        ca4a1 = Trapecia.coeff(self.a4, self.a1)

        listcoeff = [ca1a2, ca3a4, ca2a3, ca4a1]
        equal = []
        osn_a = ""
        osn_b = ""
        a = ""
        b = ""
        print("Угловые коэффициенты:     ", listcoeff)
        for i in range(len(listcoeff)-1):
            for j in range(i+1, len(listcoeff)):
                if listcoeff[i] == listcoeff[j]:
                    equal.append(listcoeff[i])
                    equal.append(listcoeff[j])
                    print(f"Есть одинаковые коэффициенты {listcoeff[i]} с индексом {i} и коэффициент {listcoeff[j]} с индексом {j}")
                    a = i
                    b = j
                else:
                    pass
        print(equal)
        if not equal:
            print("Нет равных коэффициентов, а значит, нет параллельных сторон. Т.е. данный четырехугольник не трапеция")
        else:
            if a == 0:
                osn_a = "a1a2"
            elif a == 1:
                osn_a = "a3a4"
            elif a == 2:
                osn_a = "a2a3"
            elif a == 3:
                osn_a = "a4a1"

        if not equal:
            print("Нет равных коэффициентов, а значит, нет параллельных сторон. Т.е. данный четырехугольник не трапеция")
        else:
            if b == 0:
                osn_b = "a1a2"
            elif b == 1:
                osn_b = "a3a4"
            elif b == 2:
                osn_b = "a2a3"
            elif b == 3:
                osn_b = "a4a1"
            else:
                pass
        return osn_a, osn_b

trap = Trapecia(x1 = 1, y1 = 1, x2 = 2, y2 = 4, x3 = 4, y3 = 4,  x4 = 6, y4 = 1)
osnov = trap.parall()
print(osnov)
trap.sq()
S_trap = trap.sq()
print("S = ", S_trap)
