from azureml.core import Workspace 
ws = Workspace.from_config() 
print('Workspace.from_config')
print(ws.get_details()) 
ws = Workspace.get(name = 'NewWorkspace', subscription_id = 'f0ead8e9-14fb-4521-b2cb-4378927736a8', resource_group = 'ML_RESOURCE_GROUP') 
print('Workspace.get') 
print(ws.get_details()) 

ws = Workspace(workspace_name = 'NewWorkspace', subscription_id = 'f0ead8e9-14fb-4521-b2cb-4378927736a8', resource_group = 'ML_RESOURCE_GROUP') 
print('Workspace') 
print(ws.get_details()) 
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
print('Workspace.Create') 
print(ws.get_details()) 