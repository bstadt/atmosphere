class SimulationResult:
    def __init__(self, results, hyperparams, signature, execution_time):
        self.results = results
        self._metadata = {'signature':signature,
                          'execution_time':execution_time,
                          'hyperparams':hyperparams}
