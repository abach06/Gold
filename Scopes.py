
#if 1 < 2:
    #x = 5
    
#while x < 6:
 #   print(x)
  #  x += 1
    
#print(x)

y = 5

def set_x(y):
    print("inner y:", y)
    x = y
    y = x
    
set_x(10)

print("Outer y:", y)
    
