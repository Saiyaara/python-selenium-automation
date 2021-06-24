def sumOfDigitsFrom1ToN(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def max_number(x,y,z):
    if(x >= y) and (x >= z):
        max = x
    elif(y >= x) and (y >= z):
        max = y
    else:
        max = z
    return max

def countOddEven(n):
    odd = 0
    even = 0
    while n > 0:
        digit = n % 10
        n = n // 10
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
    return (odd, even)

n = 5
print("Sum from 1 to ", n,"is:", sumOfDigitsFrom1ToN(n))

x = 124
y = 21
z= 32
print("Max of", x,y,z, "is:", max_number(x,y,z))

(odd, even) = countOddEven(34560)
print("Odd = ", odd, "even = ", even)