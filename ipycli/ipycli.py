#!/usr/bin/env ipython
from __future__ import print_function
import ncs
import IPython


def run():
    IPython.get_ipython().define_macro('var', """a=10
b=20
print("new variables created")
""")
    a = 10
    b = 20
    print("Your new variables are a=10, b=20")
    print("""This is my new Banner
don't change the banner..!
""")
    IPython.embed(display_banner=False)


if __name__ == '__main__':
    run()
