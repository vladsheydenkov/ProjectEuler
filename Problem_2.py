"""Each new term in the Fibonacci sequence is generated 
by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence 
whose values do not exceed four million, 
find the sum of the even-valued terms."""

#var 1
su = 0
x = 0
y = 1
while x < 4000000 and y < 4000000:
    x += y
    if not x % 2:
        su +=  x
    y += x
    if not y % 2:
        su +=  y

print (su)

#var 2
m = [1,2]
while m[-1] < 4000000:
    m.append(m[-2] + m[-1])
def filt(a):
    if not a%2:
        return a
b = filter(filt, m)
print (sum(b))

#var 3
m = [1,2]
while m[-1] < 4000000:
    m.append(m[-2] + m[-1])
b = filter(lambda a: not a%2, m)
print (sum(b))


