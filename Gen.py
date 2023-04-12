#Generators

def gen_range(stop, start=1, step=1):
    num = start
    while num <= stop:
        yield num 
        num += step

for num in gen_range(10, step=2):
    print(num)
    
    #python3.7 -i gen.py
#generator = gen_range(10)
#ist(generator)

def gen_fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a
        
[next(fib) for _ in range(50)] [-1]# This will calculate the fibinachi sequence out to 12586269025


#Lab for a cloud guru


