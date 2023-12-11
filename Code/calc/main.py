import sys
from sys import argv
from div import get_div
from prod import get_prod
from sum import get_sum
from sub import get_sub


def runner(a, b, op):
    if op == "+":
        return get_sum(a, b)
    elif op == "-":
        return get_sub(a, b)
    elif op == "*":
        return get_prod(a, b)
    return get_div(a, b)


if __name__ == '__main__':
    if len(sys.argv) > 4 or len(sys.argv) < 4:
        print("Wrong number of args")
    else:
        result = runner(
            int(sys.argv[1]),
            int(sys.argv[2]),
            sys.argv[-1]
        )
        print(result)
