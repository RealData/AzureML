from azureml.core import Workspace, Experiment 
ws = Workspace.from_config() 


exp = Experiment(name = 'NewExperiment', workspace = ws) 
run = exp.start_logging() 
run.log('Logging NewExperiment', '') 
run.log('RunNumber', 1) 

print('RUN ') 
print(run) 
print(type(run)) 
run.complete() 