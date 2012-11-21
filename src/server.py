#!/usr/bin/env python
# File: server.py
# Author: Junfeng Li <li424@mcmaster.ca>
# Description: interprete and evalulate plot commands
# Created: November 20, 2012

## ref
# * http://stackoverflow.com/questions/9977446/connecting-to-a-remote-ipython-instance
# * https://github.com/ivanov/vim-ipython
# * https://github.com/ipython/ipython/blob/master/IPython/frontend/terminal/console/interactiveshell.py


from IPython.lib.kernel import find_connection_file
from IPython.zmq.blockingkernelmanager import BlockingKernelManager

infofile = "/Users/ljunf/Documents/Projects/JuliaLab/src/kernel.info"

# evalutate code
def run_cell(code):
    # now we can run code. This is done on the shell channel
    shell = km.shell_channel
    # execution is immediate and async, returning a UUID
    msg_id = shell.execute(code)
    # get_meg can block for a reply
    reply = shell.get_msg()

    if reply['content']['status'] == 'error':
        print 'Error occured!'
        for line in reply['content']['traceback']:
            print line

with open(infofile, 'r') as f:
    cf = f.readline()
cf = cf[0:-2]
cf = find_connection_file(cf)
km = BlockingKernelManager()
km.connection_file = cf
km.load_connection_file()
km.start_channels()


import argparse
parser = argparse.ArgumentParser()
parser.add_argument('cmd')
cmd = parser.parse_args().cmd
#print cmd
run_cell(cmd)