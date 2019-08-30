#!/usr/bin/env python3
import sys, os, ast

VERSION = "0.2.0"
COPYRIGHT = "Ryuichi Ueda"
LICENSE = "MIT license"

f = []

def usage():
    print("py " + VERSION, file=sys.stderr)
    print("Copyright 2019 " + COPYRIGHT, file=sys.stderr)
    print("Released under " + LICENSE, file=sys.stderr)

def Fs(n, m=0):
    if m == 0:
       m = n

    return " ".join(str(x) for x in f[n:m+1])

def to_number(lst):
    ans = []
    for e in lst:
        try:
            a = int(e)
        except:
            try:    a = float(e)
            except: a = e

        ans.append(a)

    return ans

def parse(arg):
    if arg[-1] != "]":
        return arg, ""

    for n in range(len(arg)):
        try:
            ast.parse(arg[-n-1:])
            return arg[:-n-1], arg[-n-1:]
        except:
            pass
    
    print("parse error", file=sys.stderr)
    sys.exit(1)

def split_fields(line):
    line = line.rstrip('\n')
    return [line] + to_number( line.split(' ') )

def exec_line(pattern, action):
    for line in sys.stdin:
        f = split_fields(line)
        for n, e in enumerate(f):
            exec("F" + str(n) + " = e ")

        lst = eval(action) if action else f[1:]

        if pattern == "" or eval(pattern):
            print( " ".join([ str(e) for e in lst]) )

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        usage()
        sys.exit(1)

    if len(sys.argv) > 2 and sys.argv[1] == "-m":
        exec(sys.argv[2])
        command_pos = 3
    else:
        command_pos = 1

    pattern, action = parse(sys.argv[command_pos])
    exec_line(pattern, action)
