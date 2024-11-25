def sum_list(lst: list[int]) -> int:
    sum = 0
    for num in lst:
        sum += num
    return sum


print(sum_list([1,2,3,4,5,6,7,8,9,10]))

def sum_list2(lst: list[list[int]]) -> int:
    sum = 0
    for num in lst:
        sum += sum_list(num)
    return sum

print(sum_list2([[1,2,5],[4,5,6],[7,8,9],[10]]))


def sum_list3(lst: list[list[list[int]]]) -> int:
    sum = 0
    for num in lst:
        sum += sum_list2(num)
    return sum

print(f"Sum list 3d array =", sum_list3([[[1,2,5],[4,5,6],[7,8,9],[10]],[[1,2,5],[4,5,6],[7,8,9],[10]],[[1,2,5],[4,5,6],[7,8,9],[10]]]))

def sum_nested(obj: int | list) -> int:
    if isinstance(obj,int):
        return obj
    else:
        s = 0
        for sublist in obj:
            s += sum_nested(sublist)
        return s

print(sum_nested([[1,2,5],[4,5,6],[7,8,9],[10]]))
