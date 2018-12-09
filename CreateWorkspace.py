import azureml.core 
from azureml.core import Workspace 
SUBSCRIPTION_ID = 'f0ead8e9-14fb-4521-b2cb-4378927736a8' 
ws = Workspace.create(
    name = 'NewWorkspace', 
    #auth = AUTH, 
    subscription_id = SUBSCRIPTION_ID, 
    resource_group = 'ML_RESOURCE_GROUP', 
    location = 'eastus2', 
    create_resource_group = True, 
    exist_ok = True
) 

print(ws.get_details()) 

ws.write_config() 