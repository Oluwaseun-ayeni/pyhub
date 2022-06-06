from collections import Counter
import operator


def list_with_module():
    lst = ['Apple', 'Mango', 'Orange', 'Apple', 'Boy', 'Orange', 66, 'eat', 3, 9, 'Mango']
    return Counter(lst)


print(list_with_module())


def list_without_module():
    lst = ['Apple', 'Mango', 'Orange', 'Apple', 'Boy', 'Orange', 66, 'eat', 3, 9, 'Mango']

    count = operator.countOf(lst)
    return count


