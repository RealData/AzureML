from azureml.core.runconfig import RunConfiguration
from azureml.core.conda_dependencies import CondaDependencies


from azureml.core import ScriptRunConfig
from azureml.core import Workspace, Experiment 



ws = Workspace.from_config() 
exp = Experiment(name = 'NewExperiment', workspace = ws) 


run_config_system_managed = RunConfiguration(framework = 'Python')

run_config_system_managed.environment.python.user_managed_dependencies = False
run_config_system_managed.auto_prepare_environment = True
conda_dependencies = CondaDependencies.create(conda_packages=['azure'])
run_config_system_managed.environment.python.conda_dependencies = conda_dependencies  
#run_config_system_managed.save(name = 'local_system_managed_environment', path = '.')  # Also writes conda_dependencies.yml  
run_config_system_managed = RunConfiguration.load(name = 'local_system_managed_environment', path = '.') 

print('RunConfiguration') 
print(run_config_system_managed, '\n') 
print(run_config_system_managed.environment, '\n') 


script_run_config = ScriptRunConfig(source_directory = '.', script = 'train.py', run_config = run_config_system_managed)
print('ScriptRunConfig') 
print(script_run_config, '\n') 

run = exp.submit(script_run_config) # Creates project.json in aml_config 

print(run.get_portal_url())
print('RUN ')
print(run) 
print(type(run))

run.log('START', 'Starting Script Via Submit With System Managed Environment')

run.wait_for_completion(show_output = True) 
