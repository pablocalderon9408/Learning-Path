import time

def fibo_gen():
    pass

if __name__ == '__main__':
    fibo_gen()


lst = [2,4,1,3]
new=lst
lst[0]=9
print(new)

name = [(1,2),(2,3),(4,5)]
name = str(name)
print(name.replace('', ']').replace(']', '').split(','))

async def prueba():
    print("hello")

print(prueba())