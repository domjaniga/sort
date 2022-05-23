import random

numbers=[]

def generateNumbers():
    global numbers

    for i in range(10):
        num=random.randint(1,100)
        numbers.append(num)

def bubbleSort():
    a=0
    
    for i in range(len(numbers)):
        for j in range(len(numbers)-1):
            if numbers[j]>numbers[j+1]:
                a=numbers[j]
                numbers[j]=numbers[j+1]
                numbers[j+1]=a
            
generateNumbers()
print(numbers)
bubbleSort()
print(numbers)