
def factorial(num):
    result = 1
    if num == 0:
        return 1
    else:
        for idx in range(1,num +1):
            result = idx*result 
    return result
