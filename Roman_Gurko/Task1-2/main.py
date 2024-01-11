from convertToEUR import *
from convertToUSD import *
from convertToRUB import *
import sys


def convert(byn, currency):
    res = None
    match currency:
        case 'usd':
            res = convertToUSD(byn)
        case 'eur':
            res = convertToEUR(byn)
        case 'rub':
            res = convertToRUB(byn)
    return res


if __name__ == '__main__':
    print(convert(int(sys.argv[1]), sys.argv[-1]))
