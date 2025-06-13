dict1 = {
    'value': 11
}

dict2 = dict1

print("Values of dict1 and dict2")
print("Value of dict1:", dict1)
print("Value of dict2:", dict2)

print("\nlocation of dict1:", id(dict1))
print("location of dict2:", id(dict2))

dict2['value'] = 20

print("After updating dict2")
print("Value of dict1:", dict1)
print("Value of dict2:", dict2)

print("\nlocation of dict1:", id(dict1))
print("location of dict2:", id(dict2))


dict3 = {'value': 30}
dict2 = dict3
print("After updating dict2 to dict3")
print("Value of dict1:", dict1)
print("Value of dict2:", dict2)
print("Value of dict3:", dict3)

print("\nlocation of dict1:", id(dict1))
print("location of dict2:", id(dict2))
print("location of dict3:", id(dict3))