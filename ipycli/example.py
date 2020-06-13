import IPython as ipy
from IPython.terminal.interactiveshell import TerminalInteractiveShell

# from IPython.testing import tools
# config = tools.default_config()
# config.TerminalInteractiveShell.simple_prompt = True


def run():
    shell = TerminalInteractiveShell.instance()
    shell.user_ns['shell'] = shell
    shell.define_macro('x', 'a,b=1,2')
    shell.define_macro('y', 'a,b=3,4')
    shell.config['using'] = True
    a, b = 0, 0
    x, y = shell.user_ns['x'], shell.user_ns['y']
    ipy.embed(display_banner=False, config=shell.config)

if __name__ =="__main__":
    run()
    # shell = TerminalInteractiveShell.instance()
    # shell.user_ns['shell'] = shell
    # shell.define_macro('x', 'a,b=1,2')
    # shell.define_macro('y', 'a,b=3,4')
    # shell.config['using'] = True
    # a, b = 0, 0
    # ipy.embed(display_banner=False, config=shell.config)



