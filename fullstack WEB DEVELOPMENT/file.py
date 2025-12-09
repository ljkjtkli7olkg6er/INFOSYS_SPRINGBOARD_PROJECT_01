class student:
    def __init__(self,name,marks):#class
        self.name=name
        self.marks=marks
     #create object using classes
s2=student("jay kumar",89)
s3=student("vijay mahotra",90)
print(s3.name,[s3.marks])
print(s2.name,[s2.marks])

## abstration in python: hiding unessesary details

class car:
    def __int__(self):#define car that car has that properties
        self.accl=False
        self.brek=False
        self.clutch=False
    def start(self):# when we start a car we make changes but we are not able to see acc,clutch;
        self.accl=True
        self.clutch=True
        print("car started ......")
c1=car()
c1.start()


# encapsulation: wrapping data and function into one unit

# create a class account with attribute-balance & account no.
# create method for debit , credit and print balance
class account:
    def __init__(self,bal ,acc):
        self.balance=bal
        self.account_no=acc
    #Debit
    def credit(self,amount):
        self.balance-=amount
        print("Rs" ,amount  ," credit to your account ")
        print("total balance " ,self.get_balance())
    def debit(self,amount):
        self.balance+=amount
        print("Rs" ,amount ," debit to your account ")
        print("total balance ", self.get_balance())
    def get_balance(self):
        return self.balance

acc1 = account(1000,970094)
print(acc1.balance)  
print(acc1.account_no)
acc1.debit(2000)
acc1.credit(500)

    



    
    