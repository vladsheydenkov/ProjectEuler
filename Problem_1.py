"""If we list all the natural numbers below 10 
that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000
"""

#var 1
x = 0
for i in range (1,1001):
    if not i % 3 or not i % 5:
        x += i
print(x)

#var 2
y = [s for s in range(1001) if not s % 3 or not s % 5]
print(sum(y))

#end