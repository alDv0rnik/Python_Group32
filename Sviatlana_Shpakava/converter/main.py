from converter_a import converter_usd
from converter_b import converter_eur
from converter_c import converter_rub


def convert_this(sum_byn, currency):
    if currency == 'usd':
        return converter_usd(sum_byn)
    elif currency == 'eur':
        return converter_eur(sum_byn)
    return converter_rub(sum_byn)


# if __name__ == '__main__':
#     import sys
#     from sys import argv
#     print(convert_this(int(sys.argv[1]), sys.argv[-1]))

print(convert_this(sum_byn=100, currency='usd'))
print(convert_this(sum_byn=100, currency='eur'))
print(convert_this(sum_byn=100, currency='rub'))
