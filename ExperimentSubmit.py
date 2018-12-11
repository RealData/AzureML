from azureml.core import ScriptRunConfig, RunConfiguration
from azureml.core import Workspace, Experiment 



ws = Workspace.from_config() 
exp = Experiment(name = 'NewExperiment', workspace = ws) 



run_config=RunConfiguration(framework = 'Python') 
run_config.environment.python.user_managed_dependencies = True 
run_config.save(name = 'local', path = '.') # Also writes conda_dependencies.yml 
#run_config.save(name = 'local', path = '.', separate_environment_yaml = True) # Also writes environment.yml 
run_config = RunConfiguration.load(name = 'local', path = '.')

print('RunConfiguration') 
print(run_config, '\n') 
print(run_config.environment, '\n') 


script_run_config = ScriptRunConfig(source_directory = '.', script = 'train.py', run_config = run_config)
print('ScriptRunConfig') 
print(script_run_config, '\n') 



run = exp.submit(script_run_config) # Creates project.json in aml_config 

print(run.get_portal_url())
print('RUN ')
print(run) 
print(type(run))

run.log('START', 'Starting Script Via Submit')

run.wait_for_completion(show_output = True) 

