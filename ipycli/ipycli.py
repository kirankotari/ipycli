#!/usr/bin/env ipython
import os
import sys
import logging
import subprocess
import IPython as ipy
from IPython.terminal.interactiveshell import TerminalInteractiveShell as ipy_shell


class Ipycli:
    name = 'ipycli'
    command = ['ipython']
    options = []

    __stdout = subprocess.PIPE
    __stderr = subprocess.PIPE

    def __init__(self, log_level=logging.INFO, log_format=None, *args, **kwargs):
        # logger setup
        self.__format = log_format
        self.logger = self.__set_logger_level(log_level)
    
    def __set_logger_level(self, log_level):
        if self.__format is None:
            self.__format = '[ %(levelname)s ] :: [ %(name)s ] :: %(message)s'
        logging.basicConfig(stream=sys.stdout, level=log_level,
                            format=self.__format, datefmt=None)
        logger = logging.getLogger(self.name)
        logger.setLevel(log_level)
        return logger

    def __run_command(self, command):
        self.logger.debug("command `{}` running on terminal".format(' '.join(command)))
        p = subprocess.Popen(command, stdout=self.__stdout, stderr=self.__stderr)
        out, err = p.communicate()
        out, err = out.decode('utf-8'), err.decode('utf-8')
        if err == '':
            self.logger.debug("`{}` ran successfully".format(' '.join(command)))
            return out
        self.logger.error("command issue: {}".format(err))
        self.__exit

    @property
    def __exit(self):
        sys.exit()

    def _create_profile(self):
        self.command += ['profile', 'create']
        self.logger.info('creating ipython profile')
        out = self.__run_command(self.command)
        if out is None or out == '':
            self.logger.info("couldn't able to create an ipython instance.")
            self.__exit

    def _get_shell(self):
        if ipy.get_ipython() is None:
            shell = ipy_shell.instance()
            if shell is None:
                self._create_profile()
                self._get_shell()
            shell.user_ns['shell'] = shell
        return ipy.get_ipython()

    def initialize(self):
        shell = self._get_shell()
        print(f"ipycli shell {shell}")
        shell.define_macro('x', 'a,b=1,2')
        shell.define_macro('y', 'a,b=3,4')
        a, b = 0, 0
        x, y = shell.user_ns['x'], shell.user_ns['y']
        print("This is Banner..!")
        ipy.embed(display_banner=False, config=shell.config)

def run():
    obj = Ipycli()
    obj.initialize()


if __name__ == '__main__':
    run()
