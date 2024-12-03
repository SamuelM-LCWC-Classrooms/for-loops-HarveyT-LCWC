from random import randrange

def task_1(): # Lottery ticket generator

    ticket = []

    # Code here
    import random
    for i in range (6):
     number = randrange (1, 49)
     ticket.append(number)
     print("lottery numbers are:", ticket)
    return ticket

def task_2(): # Countdown

    output = []
   
    # Code here
    
    user = int(input("please enter a number from 1 to 100: "))
        
    for i in range(100, user - 1, -1):
        output.append(i)

    return output

def task_3():
    people_cars = {
        "Adam": "Volvo",
        "Kate": "BMW",
        "Mark": "BMW",
        "Hannah": "Ford",
        "Max": "Volvo",
        "Celine": "Fiat"
    }

    car_make_lengths = ()

    # Code here
    for car_make in people_cars.values:
       car_make_lengths.add(len(car_make))

    num_size = len(car_make_lengths)

    print(f"There will be {num_size} different sizes of key rings.")
    return # Code the sentence here

print(task_3())