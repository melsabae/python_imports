def the_function(param1, param2):
    print("we dont do stuff with this")
    return 5


def exports(argv):
    return { "f": the_function }


if "__main__" == __name__:
    exit(-1)

