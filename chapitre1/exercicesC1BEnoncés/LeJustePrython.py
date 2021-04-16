price=150
#1
print(price)

#2
def ChangePrice():
    prix=300
    print(prix)
    
ChangePrice()

#3
print(price)

#4
def SayPrice():
    print(price)
    
SayPrice()

#5
def ChangePriceTwo():
    global price 
    price = 30
    print(price)
    
print(price)

#6
ChangePriceTwo()

#7
print(price)

#8

def ChangePriceThree(_price):
    _price = 70
    print(_price)
    
ChangePriceThree(price)

#9
print(price)

#10
#print(_price)

#11
def SayPriceTwo(_price):
    print(_price)
    
SayPriceTwo(price)

#12
#SayPriceTwo(_price)

#13
def ReturnPrice(_price):
    return 15

print(ReturnPrice(price))

#14
print(price)

#15
price = ReturnPrice(1000)

print(price)

#16
def ReturnPriceTwo(_price):
    return _price + 5

print(ReturnPriceTwo(price))

#17
print(ReturnPriceTwo(1000))

#18
print(price)

#19
price = ReturnPriceTwo(price)
print(price)

#20
price = ReturnPriceTwo(444719)
print(price)

