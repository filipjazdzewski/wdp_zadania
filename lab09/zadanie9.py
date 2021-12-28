def euclid(num1, num2):
    if num1 == num2:
        return num1
    if num1 > num2:
        return euclid(num1-num2, num2)
    else:
        return euclid(num1, num2-num1)


result = euclid(12, 75)
print(result)
