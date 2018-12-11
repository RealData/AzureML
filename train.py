from azureml.core import Run 
print('TRAIN') 


run = Run.get_context(allow_offline = True) 
print(run) 
print(type(run))
run.log('INFO', 'Logging Via Run Context') # This will be printed to output if OfflineRun 

#print(run.get_properties()) # ERROR if OfflineRun 

def get_AMLRun(): 
    try: 
        run = Run.get_context(allow_offline = False) 
        return run 
    except: 
        return None 

#run = get_AMLRun() 

import pickle

with open('outputs/model.pickle', 'wb') as handle:
    pickle.dump({'MODEL': 'HHHHHH'}, handle, protocol=pickle.HIGHEST_PROTOCOL)

run.register_model(model_name = 'SimpleModel', model_path = 'model.pickle')

print(run)