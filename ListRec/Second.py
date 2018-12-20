List = [1, [2, [3], [1, 2]], 4]
print(List)

def suma(List):
    result = 0
    for i in List:
        if isinstance(i,List):
            res += suma(i)
        else:
            result +=i

    return result

print(suma(List))