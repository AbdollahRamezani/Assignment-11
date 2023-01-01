class Fraction:
   #properties
    def __init__(self, s, m):
        self.s=s
        self.m=m

    #methods
    def sum(self, f1):
        s=self.s*f1.m+f1.s*self.m
        m=self.m*f1.m
        f=Fraction(s, m)
        return f

    def mul(self, f1):
        s=self.s*f1.s
        m=self.m*f1.m
        f=Fraction(s, m)
        return f
    
    def sub(self, f1):
        s=self.s*f1.m-f1.s*self.m
        m=self.m*f1.m
        f=Fraction(s, m)
        return f
    
    def div(self, f1):
        s=self.s*f1.m
        m=self.m*f1.s
        f=Fraction(s, m)
        return f
    def fraction_to_number(self):
        number=self.s/self.m
        return number
    def show(self):
        print(self.s, "/", self.m)


a=Fraction(2, 3)    
b=Fraction(7, 5)
             
sum=b.sum(a)
sum.show()

mul=b.mul(a)
mul.show()

sub=b.sub(a)
sub.show()

div=b.div(a)
div.show()

number=b.fraction_to_number()
print(number)

