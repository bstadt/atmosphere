import time
from multiprocessing import Process

from .resource_master import ResourceMaster
from .simulation_template import GridSimulationTemplate

class Dispatcher:

    def __init__(self, resources_masters, simulation_template):

        self.resource_masters = resource_masters
        self.simulation_template = simulation_template
        self.jobarg_generator = self.simulation_template.get_hyperparam_generator()

    def naive_dispatch(self):
        processes = [None for _ in self.resource_masters]

        #for every job that needs done
        for job_args in self.jobarg_generator:
            deployed = False
            #while you havent deployed it to a resource
            while not deployed:
                #check the state of all the resources
                for i, resource in enumerate(self.resource_masters):
                    #if the resource is able to accept the job
                    if processes[i] is None or not processes[i].isAlive():
                        #give the open resource the job
                        processes[i] = Process(target=resource.dispatch_job,
                                               args=(resource,),
                                               kwargs=job_args)
                        #record that the job has been assigned
                        deployed=True
                        #stop looking for someone to take the job
                        break
                time.sleep(1)
        return
