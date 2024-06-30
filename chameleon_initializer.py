
#I used the same class but you can use a different classes

class BBB():pass
 
def custom_init(self, **kwargs):   #variable custom initializer created (chameleon initializer)
    for key, value in kwargs.items():
        setattr(self, key, value)
        
setattr(BBB, '__init__', custom_init)    #variable added to custom initializer class

print("-----------Example 1-------------------------------")

bbb = BBB(name="Jully", age=21, city="kalifornia",fatherAge=48)  #Add four features

print("bbb.name---------->",bbb.name)
print("bbb.age----------->",bbb.age)
print("bbb.city---------->",bbb.city)
print("bbb.fatherAge----->",bbb.fatherAge)


print("----------Example 2------------------------------")

bbb = BBB(name="Jully", age=21, city="kalifornia")  #Add three features

print("bbb.name---------->",bbb.name)
print("bbb.age----------->",bbb.age)
print("bbb.city---------->",bbb.city)
try:
    print(bbb.fatherAge)
except Exception as e:
    print(e)

print("-----------Example 3------------------------------")

bbb = BBB(name="Jully", age=21)  #Add two features

print("bbb.name---------->",bbb.name)
print("bbb.age----------->",bbb.age)
try:
    print(bbb.city)
except Exception as e:
    print(e)
    
try:
    print(bbb.fatherAge)
except Exception as e:
    print(e)

