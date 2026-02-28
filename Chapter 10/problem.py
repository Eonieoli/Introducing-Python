# 1
class Thing:
    pass

thing_a = Thing()
thing_b = Thing()

print(thing_a)
print(thing_b)
# 다르다.


# 2
class Thing2:
    letters = 'abc'

print(Thing2.letters)


# 3
class Thing3:
    pass

thing3 = Thing3()
thing3.letters = 'xyz'
print(thing3.letters)
# 생성해야 한다.


# 4
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    
hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen.name)
print(hydrogen.symbol)
print(hydrogen.number)


# 5
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(**el_dict)
print(hydrogen.name)
print(hydrogen.symbol)
print(hydrogen.number)


# 6
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    
    def dump(self):
        print(self.name)
        print(self.symbol)
        print(self.number)

hydrogen = Element('Hydrogen', 'H', 1)
hydrogen.dump()


# 7
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    
    def __str__(self):
        return f"name: {self.name}, symbol: {self.symbol}, number: {self.number}"
    
hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen)


# 8
class Element():
    def __init__(self, input_name, input_symbol, input_number):
        self.hidden_name = input_name
        self.hidden_symbol = input_symbol
        self.hidden_number = input_number
    
    @property
    def name(self):
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        self.hidden_name = input_name
    
    @property
    def symbol(self):
        return self.hidden_symbol
    @symbol.setter
    def symbol(self, input_symbol):
        self.hidden_symbol = input_symbol
    
    @property
    def number(self):
        return self.hidden_number
    @number.setter
    def number(self, input_number):
        self.hidden_number = input_number
    
    def __str__(self):
        return f"name: {self.hidden_name}, symbol: {self.hidden_symbol}, number: {self.hidden_number}"

hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen)


# 9
class Bear:
    def eats(self):
        return 'berries'

class Rabbit:
    def eats(self):
        return 'clover'

class Octothope:
    def eats(self):
        return 'campers'

bear = Bear()
rabbit = Rabbit()
octothope = Octothope()

print(bear.eats())
print(rabbit.eats())
print(octothope.eats())


# 10
class Laser:
    def does(self):
        return 'disintegrate'

class Claw:
    def does(self):
        return 'crush'

class SmartPhone:
    def does(self):
        return 'ring'

class Robot(Laser, Claw, SmartPhone):
    def __init__(self, laser, claw, smartphone):
        self.laser = laser
        self.claw = claw
        self.smartphone = smartphone
    
    def does(self):
        print(f"Laser does {self.laser.does()}")
        print(f"Claw does {self.claw.does()}")
        print(f"SmartPhone does {self.smartphone.does()}")
    
laser = Laser()
claw = Claw()
smartphone = SmartPhone()
robot = Robot(laser, claw, smartphone)
robot.does()