import os
import rpyc
from rpyc.utils import server

class ResourceSlave(rpyc.Service):

    def on_connect(self, conn):
        #get current simulation code
        os.system('wget https://github.com/orbital-satellite/relay_point/raw/master/payload.zip')
        os.system('unzip payload.zip')

    def on_disconnect(self, conn):
        os.system('rm -r payload/__pycache__')
        os.system('rm payload/*')
        os.system('rmdir payload')
        os.system('rm payload.zip')
        return

    def exposed_execute_simulation(self, hyperparams):
        print('Slave copy: ', hyperparams)
        '''
        from payload.test import test_fn
        res = test_fn(**hyperparams)
        '''
        return hyperparams['arg']
