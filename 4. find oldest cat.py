#OOP!

class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        

# 1 Instantiate the Cat object with 3 cats

mark = Cat('mark', 2)
bale = Cat('bale', 3)
selby = Cat('selby', 1)


# 2 Create a function that finds the oldest cat

def find_old_cat(*args):
    oldest_cat = args[0]
    for cat in args:
        if cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat


oldest_cat = find_old_cat(mark, bale, selby)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f'the oldest cat {oldest_cat.name} is {oldest_cat.age} years old')
