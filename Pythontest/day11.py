class Bankaccount:
 def __init__(self,name,money):
    self.__name = name
    self.__balance=money
 def deposit(self,money):
    self.__balance += money
 def withdraw(self, money):
    if self.__balance > money:
        self.__balance -= money
        return money
    else:
            return "Insufficient funds"

 def checkbalance(self):
    return self.__balance

b1=Bankaccount('tim',400)
print (b1.withdraw(500))
b1.deposit(500)
print (b1.checkbalance())
print (b1.withdraw(800))
print (b1.checkbalance())







def sum(start,end):
    result=0
    for i in  range (start,end+1):
        result +=i
    print(result)
sum(1,100)


def sumreturn(start,end):
    result=0
    for i in range(start,end+1):
        result +=i
    return  result
a=sumreturn(1,5)
print (a)



def sum2(start,end):
    if (start > end):
        print ("start should be less than end")
        return
    result=0
    for i in range (start,end+1):
        result += i
    return result
s=sum2(1,10)
print (s,type(s))


# def sum(start,end):
#     result=0
#     for i in range(start,end+1):
#         result +=i
#     print(result)
# sum(1,5)

def sum(start,end):
    result=0
    for i in range(start,end+1):
        result +=i
    print(result)
sum(1,100)

def sum3(start,end):
    if(start>end):
        print("hello world")
        return
    result=0
    for i in range(start,end+1):
        result +=i
    return result
a=sum3(1,3)
print (a,type(a))



def sum4(start,end):
    if (start > end):
        print ("hello world")
        return
    result=0
    for i in range(start,end+1):
        result +=i
    return result
a=sum4(1,3)
print (a,type(a))





global_var =12
def func():
    local_var=100
    print (global_var)
    print (local_var)
func()



def bigger(a,b):
    if a>b:
        return a,b
    else:
        return b,a
s=bigger(12,100)
print (s,type(s))


def print_max(x,y):
    '''Prints the maximum of two numbers.
    The two values must be integers.'''
    x=int(x)
    y=int(y)
    if x>y:
        print (x,'is maximum')
    else:
        print (y,'is maximum')
print_max(3,5)
print (print_max.__doc__)

mylist=[1,2,3,4]
for i in mylist:
    print (i)










