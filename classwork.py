motors = ["lexus", "Toyota", "Camry","Benz"]
motors[0]= 'GLK'
motors[2]= 'Lexus'
print(motors)

motors.append("Jeep")
print(motors)

motors.sort()
print(motors)

motors.sort(reverse=True)
print(motors)

motors = ["lexus", "Toyota", "Camry","Benz"]
print(motors[3])

motors = []
motors.append('LEXUS')
motors.append('CAMRY')
motors.append('GLK')
motors.append('GLK')
motors.append('TOYOTA')
print(motors)

fruits = ["apple", "apple", "banana", "cherry"]
fruits.remove('apple')
fruits.remove('banana')
#fruits.pop(3)
print(fruits)


fruits = ["apple", "apple", "banana", "cherry"]
for a in range (len(fruits)):
    print(fruits[a])


fruits = ["apple", "apple", "banana", "cherry"]
for fruit in range (len(fruits)):
    print(fruits[fruit])

fruits = ["apple", "apple", "banana", "cherry"]
myfruits = fruits.copy()
print(myfruits)