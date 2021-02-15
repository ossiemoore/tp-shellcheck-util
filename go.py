#!/usr/bin/python3

import sys
import os
from os import path
import subprocess

def main():

    print("")
    print("start")
    print("")
    root = "."
    shellcheck = "shellcheck"

    if (len(sys.argv) > 1):
        root = sys.argv[1]
        print("base directory :", root)
        if (len(sys.argv) > 2):
            shellcheck = sys.argv[2]
            print("shellcheck path:", shellcheck)
        print("")
    
    root = path.realpath(root)
    stack = []
    stack.append(root)
    while(len(stack) > 0):
        next = stack.pop()
        print("crawl:", next)
        isdir = path.isdir(next)
        if (isdir):
            children = os.listdir(next)
            for child in children:
                child = next + '/' + child
                if (path.isdir(child)):
                    stack.append(child)
                else:
                    root, ext = os.path.splitext(child)
                    extlower = str.lower(ext)
                    if (".sh" == extlower):
                        print("found:", child)
                        f = open(child, "r")
                        first = f.readline().replace('\n','').replace('\r','')
                        f.close()
                        if("#!/bin/sh" == first):
                            print("check:", child)
                            subprocess.run([shellcheck,child])

    print("done")


if __name__ == "__main__":
  main()
