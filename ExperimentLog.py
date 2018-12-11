from azureml.core import Workspace, Experiment 
ws = Workspace.from_config() 
 
 
exp = Experiment(name = 'NewExperiment', workspace = ws) 
run = exp.start_logging() 
run.log('Logging NewExperiment', '') 
run.log('RunNumber', 1) 

print('RUN ') 
print(run) 
print(type(run)) 



import pickle

with open('outputs/model.pickle', 'wb') as handle:
    pickle.dump({'MODEL': 'HHHHHH'}, handle, protocol=pickle.HIGHEST_PROTOCOL)

run.register_model(model_name = 'SimpleModel', model_path = 'model.pickle') 


run.complete() 