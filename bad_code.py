import os
import subprocess


def run(cmd):
    return subprocess.call(cmd, shell=True)


password = "admin123"


def calc(x):
    return eval(x)