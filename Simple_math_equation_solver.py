from itertools import permutations
from typing import List, Union, Iterable

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
allowed = ["-", "+", "*"]

def eq_order(operator_path, nb):
    available_nb = nb.copy()
    available_op = operator_path.copy()
    while "*" in available_op:
        mul_poz = available_op.index("*")
        available_op.pop(mul_poz)
        mul_result = available_nb[mul_poz] * available_nb.pop(mul_poz+1)
        available_nb[mul_poz] = mul_result
    while available_op != []:
        if available_op[0] == "-":
            available_op.pop(0)
            sub_res = available_nb[0] - available_nb.pop(1)
            available_nb[0] = sub_res
        elif available_op[0] == "+":
            available_op.pop(0)
            add_res = available_nb[0] + available_nb.pop(1)
            available_nb[0] = add_res
    return available_nb[0]

def find_all_solutions(operator_path: List[str], expected_result: int) -> Union[List[List[int]], Iterable[List[int]]]:
    for op in operator_path:
        if op not in allowed:
            raise ValueError("Wrong operator")
    if type(expected_result) is not int:
        raise ValueError("Expected result is not int")
    if len(operator_path) > len(numbers):
        raise ValueError("Too much operators!")
    perm = permutations(numbers, len(operator_path) + 1)
    result = []
    for i in perm:
        if eq_order(operator_path, list(i)) == expected_result:
            result.append(list(i))
    return result


#find_all_solutions(["+", "+"], 12)
#find_all_solutions(["-"], 5))
#find_all_solutions(["*", "*", "+"], 20))
#find_all_solutions(["+", "*", "*", "+", "*", "-"],528)
