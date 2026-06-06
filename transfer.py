#problem1:-
numbers=[25,30,20,40,15,25]
total_sum=0
i=0
while i<len(numbers):
    total_sum+=numbers[i]
    if total_sum>100:
        print("sum exceeded 100")
        break
    i+=1
    if total_sum<=100:
        print("sum of numbers:",total_sum)
    print(f"last iteration:{i}")
output:-
sum of numbers: 25
last iteration:1
sum of numbers: 55
last iteration:2
sum of numbers: 75
last iteration:3
sum exceeded 100


#problem2:-
for num in range(1,601):
    if num%2==0:
        continue
    print(num)

#problem3:-
num=int(input("enter a number:"))
if num%2==0:
    print("even")
else:
     pass

output:-
enter a number:12
even

#problem4:-
words=["cse","ece","eee","break","chem","mech","skip","mme"]
for word in words:
    if word=="break":
        break
    if word=="skip":
        continue
    print(word)
#task15:-
#break statement
for i in range(15):
    if i==8:
        break
    print(i)#0 1 2 3 4 5 6 7
print(f"last iteration:{i}")#last iteration:8
#continue statement
for i in range(10):
    if i==5:
        continue
    print(i)#0 1 2 3 4 6 7 8 9
print(f"last iteration:{i}")#last iteration:9
#pass statement
for i in range(10):
    pass#output null
#task16:-
#break statement
for i in range(10):
    if i==5:
        break
    print(i)#0 1 2 3 4
print(f"last iteration:{i}")#last iteration 5
#continue statement
for i in range(8):
    if i==4:
        continue
    print(i)#0 1 2 3 5 6 7
print(f"last iteration:{i}")#last iteration:7
#pass statement
for i in range(10):
    pass
#task17:-
fruits=["apple","grapes","watermelon","papaya"]
#positive indexing
print(fruits[0])
print(fruits[1])
#negative indexing
print(fruits[-1])
print(fruits[-4])
#forward positive slicing
print(fruits[0:4])
print(fruits[0:3:1])
print(fruits[0:4:2])
#backward positive slicing
print(fruits[4:0:-1])
#backward negative slicing
print(fruits[::-1])
#forward negative slicing
print(fruits[-4:])
print(fruits[-4:-1])

output:-
apple
grapes
papaya
apple
['apple', 'grapes', 'watermelon', 'papaya']
['apple', 'grapes', 'watermelon']
['apple', 'watermelon']
['papaya', 'watermelon', 'grapes']
['papaya', 'watermelon', 'grapes', 'apple']
['apple', 'grapes', 'watermelon', 'papaya']
['apple', 'grapes', 'watermelon']
