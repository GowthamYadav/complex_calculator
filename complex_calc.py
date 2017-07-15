import math,sys

#class for arithmetic operations of complex numbers

class Complex:
    def __init__(self):
        try:
            print("input format-> real part<space>imaginary part")
            num1=input("Enter the first number: ")
            self.a,self.b=num1.split(" ")
            self.a,self.b=float(self.a),float(self.b)
            num2=input("Enter the second number: ")
            self.c,self.d=num2.split(" ")
            self.c,self.d=float(self.c),float(self.d)
        except:
            print("Follow input format.")
            main()
    def add(self):
        sum1=self.a+self.c
        sum2=self.b+self.d
        if sum1==0 and sum2==0:
            return str(sum1)
        
        if sum1==0:
            return str(sum2)+'i'
        
        if sum2>0:
            return str(sum1)+" + "+ str(sum2)+'i'
        elif sum2<0:
            return str(sum1)+" - "+ str(abs(sum2))+'i'
        else:
            return str(sum1)
    def sub(self):
        dif1=self.a-self.c
        dif2=self.b-self.d
        if dif1==0:
            return str(dif2)+'i'
            
        if dif2>0:
            return str(dif1)+" + "+str(dif2)+'i'
        elif dif2<0:
            return str(dif1)+" - "+str(abs(dif2))+'i'
        else:
            return str(dif1)
    def mul(self):
        rel=(self.a*self.c)-(self.b*self.d)
        img=(self.c*self.b)+(self.a*self.d)
        if rel==0:
            return str(img)+'i'
            
        if img>0:
            return str(rel)+" + "+str(img)+'i'
        elif img<0:
            return str(rel)+" - "+str(abs(img))+'i'
        else:
            return str(rel)
    def div(self):
        nr1=(self.a*self.c)-(self.b*(-self.d))
        nr2=(self.c*self.b)+(self.a*(-self.d))
        dr=(self.c*self.c)+(self.d*self.d)
        if nr1==0:
            return str(round(nr2/dr,2))+'i'
            
        if nr2>0:
            return str(round(nr1/dr,2) )+" + "+str(round(nr2/dr,2))+'i'
        elif nr2<0:
            return str(round(nr1/dr,2) )+" - "+str(round(abs(nr2/dr),2))+'i'
        else:
            return str(round(nr1/dr,2))
        
    def mod(self):
        n1=math.sqrt((self.a*self.a)+(self.b*self.b))
        n2=math.sqrt((self.c*self.c)+(self.d*self.d))
        print(round(n1,2))
        print(round(n2,2))

    def exit(self):
        sys.exit()

#main function
        
def main():
    c=Complex()
    print("Select what to do?")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modulo")
    print("6.Exit")
    ch=int(input("Enter the id: "))
    if ch==1:
        print(c.add())
    elif ch==2:
        print(c.sub())
    elif ch==3:
        print(c.mul())
    elif ch==4:
        print(c.div())
    elif ch==5:
        print(c.mod())
    else:
        c.exit()
    choice=input("want to continuoue?..(y/n):")
    if choice=='y':
        main()
    else:
        c.exit()

if __name__=='__main__':
    main()
    
