def example_function(*args, **kwargs):
    print("args:", args)      # tuple
    print("kwargs:", kwargs)  # dict

example_function(1, 2, 3, name="Alice", age=25, city="New York")


def add(a=3, b=2):
    print(a + b)
    
    
add(10)           
# add(10, 5)        #
# add(a=10)     
add(b=5)          
# add(a=10, b=5)    
# add(10, b=5)
# add(b=5, 10)       
add(10, b=5)      # = paxi bina = rakhna payena
# add(a=10, a=20)


def sub (a,b,c):
    return a-b-c
sub(10,5,2)   # 3
sub(a=10,b=5,c=2)  # 3
sub(1,2,3)
sub(1,2,c=3)
sub(1,b=2,c=3)
sub(a=1,b=2,c=3)
#sub(1,b=2,3) # yesma run hudaina
