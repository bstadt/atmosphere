import itertools

def dictionary_product(kwargs):
    keys = kwargs.keys()
    vals = kwargs.values()
    for instance in itertools.product(*vals):
        yield dict(zip(keys, instance))

class GridSimulationTemplate:
    def __init__(self, hyperparams={}):
        '''
        A class that defines an abstract notion of a simulation
        :param hyperparams: a list of all values for each hyperparameter
        '''
        self.hyperparams = hyperparams
        return



    def get_hyperparam_generator(self):
        '''
        Returns a generator of all hyperparameter assignments to be run
        :return: a generator of all hyperparameter assignments to be run
        '''

        return dictionary_product(self.hyperparams)
