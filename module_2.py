import itertools
import argparse


def do_the_stuff(args, param1, param2):
    print("we got {} and {} and {}".format(args, param1, param2))

    # return some data
    return itertools.product(range(3), range(5))


def exports(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=argparse.FileType('r'), help="The configuration file for this module")
    args = parser.parse_args(argv).__dict__

    return { "f": lambda p1, p2: do_the_stuff(args, p1, p2) }


if "__main__" == __name__:
    exit(-1)

