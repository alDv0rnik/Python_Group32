import mod
import argparse
from sys import argv


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version')
    parser.add_argument('--x', required=True)
    parser.add_argument('--y', required=True)
    return parser.parse_args()


if __name__ == '__main__':
    print(f"The example4_main_explanation file name is {__name__}")
    args = parse_args()
    print(args)
    x = args.x
    y = args.y
    print(x + y)

