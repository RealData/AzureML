from azureml.core import Run 
print('TRAIN') 


run = Run.get_context(allow_offline = True) 
print(run) 
print(type(run))
print(run.get_properties())
run.log('INFO', 'Logging Via Run Context') 
