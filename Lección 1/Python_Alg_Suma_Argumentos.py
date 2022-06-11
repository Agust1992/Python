def suma_val(*args):
    result = 0
    for i in args:
        result = (result + i)
    return result

print(suma_val(3, 5, 9))


def multi_val(*args2):
    result = 1
    for i in args2:
        result = (result * i)
    return result

print(multi_val(2,3,9))
