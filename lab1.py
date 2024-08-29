import math


def circ_area(r):
   return math.pi*(r**2)

def sphere_volume(r):
    return (4/3)*math.pi*(r**3)

def pythagorean_theorem(a,b):
    return math.sqrt(a**2+b**2)


print('The area of the circle is',circ_area(5))
print('The volume of the sphere is', sphere_volume(3))
print('The hypotenuse of the triangle is', pythagorean_theorem(3,4))



myname = 'Dylan'+'McGuffey'


print ('The length of my name is', len(myname), 'characters.')
print(myname.upper())
print(myname.lower())

myAge = 32
myHeight = 6
myWeight = 165

def bmi_calc(h,w):
    return (w/((h*12)+2)**2)*703


print('The Variable "My Age" is', type(myAge))
print('The Variable "My Height" is', type(myHeight))
print('The Variable "My Weight" is', type(myWeight))
print('My BMI is', bmi_calc(6,165))




