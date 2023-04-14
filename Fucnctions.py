def contact_card(name, age, car_model): #name age and car_model are parameters=(variables that we define when we are defining the function)
    
    return f"{name} is {age} and drives a {car_model}"
    
contact_card("Keith", 29, "Honda Civic")

contact_card(age=29, car_model="Honda Civic", name="Keith") #using keyword arguments. gets the same results as contact_card("Keith", 29, "Honda Civic")

contact_card("Keith", car_model="Honda Civic", age=29)

#contact_card(age=29, "Keith", car_model="Honda Civic") #positional argument follows keyword argument: You can put positional arguments first and then
#use keyword arguments, You can use all positional or you can use all keyword. These are the three ways you can go about calling functions and keywords. 


def can_drive(age, driving_age=16):
    return age >= driving_age
    
can_drive(29)
#True

can_drive(16, driving_age=18)
#false

can_drive(16, 18) #This is positional arguments.




    
    