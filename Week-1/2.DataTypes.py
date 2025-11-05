#Integer 
x = 10
print(type(x))

#Float
y = 3.67
print(type(y))

#complex
z = 1 + 2j
print(type(z))
print(z.real, z.imag)

#string
name = "Parag"
print("Hello" + name)

#list -> ordered, Mutable
nums = [1,2,3,4]
nums.append(5)
print(nums)

#tuple -> Ordered , immutable
a = (10,20,30)
print(a[0])

#Dictionary -> key - value pairs
survey = {"name": "Parag", "age": 22, "country":"Bangladesh"}
print(survey["name"])
print(survey.keys())
print(survey.values())

#Bool
he_is_active = True
he_is_not_active = False
print(type(he_is_active))
print(type(he_is_not_active))

#NoneType -> Null Reference
b = None
print(type(x))

#Type Casting
c = 367
print(float(c))
print(str(c))
print(list("Parag")) # ['P', 'a', 'r', 'a', 'g']
