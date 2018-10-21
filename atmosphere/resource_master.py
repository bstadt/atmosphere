import time
import rpyc
import pickle

from .simulation_result import SimulationResult

class ResourceMaster:
    def __init__(self, path, port, outpath, signature):
        self.path = path
        self.port = port
        self.data_outpath = outpath
        self.signature = signature
        self.conn = rpyc.connect(self.path, self.port)
        self.expired = False
        return

    def dispatch_job(self, hyperparams):
        if self.expired:
            print('Connection has been closed! Operation NOT run')
            return

        start = time.time()
        results = self.conn.root.execute_simulation(hyperparams)
        end = time.time()
        execution_time = end-start

        to_write = SimulationResult(results,
                                    hyperparams,
                                    self.signature,
                                    execution_time)

        filename = ''
        for key, value in hyperparams.items():
            filename = filename + str(key) + '=' + str(value) + '_'
        #remove trailing underscore
        filename = filename[:-1]
        filename = filename + '.simulation'

        pickle.dump(to_write, open(self.data_outpath + filename, 'wb'))
        return

    def close(self):
        self.expired = True
        self.conn.close()
