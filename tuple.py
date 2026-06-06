tuple_1=("Naveena",20,"green")
print(tuple_1)

tuple_2=(1,3,5)
tuple_3=(2,4,6)
tuple_4=tuple_2+tuple_3
print(tuple_4)

dimensions=(20,10)
length,width=dimensions
area=length*width
print(area)

numbers=(1,2,3,4)
element=int(input("enter number:"))
if element in numbers:
    print("element exist in numbers")
else:
    print("element doesn't exist in numbers")
    