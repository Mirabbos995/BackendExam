# 1-masala

fuction = [1, 2, 3, 4, 6, 7, 8, 9, 10]
a = []

def missed(funtion, a):
    for b in range(1, 10 + 1):
        if b not in funtion:
            a.append(b)
            print(b)
missed(fuction, a)


# 2- masala

def car(people):
    seats_per_car = 5
    cars_needed = people // seats_per_car
    return cars_needed + 1

c = int(input("Enter the number: "))
cars = car(c)

print(f"There will be {cars} car for {c} people ")


#3 - masala

d = [2, 4, 6, 7, 8, 11]
dis = 1/2

def discount():
    for a in d:
        h = a * dis
        print(f"50% discount of {d} is {h}")
discount()


# d = [2, 4, 6, 7, 8, 11]
# dis = 3/4
#
# def discount():
#     for a in d:
#         h = a * dis
#         print(f"50% discount of {d} is {h}")
# discount()


# d = [2, 4, 6, 7, 8, 11]
# dis = 9/20
#
# def discount():
#     for a in d:
#         h = a * dis
#         print(f"50% discount of {d} is {h}")
# discount()