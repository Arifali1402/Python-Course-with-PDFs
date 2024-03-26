# Addition of Two Complex Numbers
# (a+bi)+(c+di) = (a+c)+(b+d)i

# Multiplication of Two Complex Numbers
# (a+bi)*(c+di) = (ac-bd) + (ad+bc)i

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def __str__(self):
        if(self.img<0):
            return f"{self.real}-{-self.img}i"
        else:
            return f"{self.real}+{self.img}i"

    def __add__(self,c):
        print("ADDING TWO COMPLEX NUMBERS...")
        return Complex(self.real+c.real,self.img+c.img)

    def __mul__(self,p):
        mulReal = self.real * p.real - self.img * p.img
        mulImg = self.real * p.img + self.img * p.real
        print("MULTIPLYING TWO COMPLEX NUMBERS...")
        return Complex(mulReal,mulImg)
        

c1 = Complex(1 , 4)
c2 = Complex(8 , -35)
print(c1)
print(c2)
add = c1 + c2
print(add)
mul = c1 * c2
print(mul)