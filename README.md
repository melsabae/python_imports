# python_imports

a python program that imports other python programs as its own modules
the program consumes CLI args via argparse, and forwards any unknown/unconsumed parameters to the module to load
the module is expected to declare a function

exports :: [string] -> dict

where the parameter is the list of unknown/unconsumed arguments from argparse

the function returns a dict of arbitrary data
    in this case, the dictionary has key "f" with value: function of 2 parameters
        this is example code, so that is not required via this project, it is for demonstrationing

the use of config files here is also for demonstration, the parameters can be whatever, im just partial to putting things into config files
    the program itself needs a config file, and the module_2 needs a config file


module_1 and module_2 require different parameters

