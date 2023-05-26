#!/usr/bin/env python3


import importlib.util
import configparser
import sys
import os
import argparse


def import_module(module_path):
    module_name = os.path.basename(module_path)
    name, ext = os.path.splitext(module_name)
    spec = importlib.util.spec_from_file_location(name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=argparse.FileType('r'), help="The configuration file for this program")
    parser.add_argument("module", type=argparse.FileType('r'), help="The module to import")
    known, unknown = parser.parse_known_args()
    args = known.__dict__

    module = import_module(args["module"].name)
    exports = module.exports(unknown)
    print(exports["f"](0, 1))


if "__main__" == __name__:
    exit(main())

