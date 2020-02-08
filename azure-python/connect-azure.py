import os
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
import logging
logger = logging.getLogger(__name__)



# method to read the config info value
def getConfigInfoValues(configName,configKey,infoFileLocation=".",separator="="):
  try:
    fileName=infoFileLocation+"/"+configName
    configValueDict = {}
    with open(fileName,'r') as configFile:
        for line in configFile:
            sKey, sValue = line.partition(separator)[::2]
            configValueDict[sKey.strip()] = sValue.strip()
        return configValueDict[configKey]
  except FileNotFoundError :
    logger.exception("getConfigInfoValues : "+configName+" file not found error encountered ")
    exit(1)
  except Exception  :
    logger.exception("getConfigInfoValues : "+configName+" file not found error encountered ")
    exit(1)


# read the location and file name for the subscription id
subscriptionFileName='EnvDetails.info'
print("Info files are available at : "+ infoFileLocation)

# Usage - get the details from the info file 
subscriptionId=getConfigInfoValues(subscriptionFileName,'subscriptionID',infoFileLocation).strip('"')
client_id=getConfigInfoValues(subscriptionFileName,'clientID',infoFileLocation).strip('"')
client_secret=getConfigInfoValues(subscriptionFileName,'secret',infoFileLocation).strip('"')
tenant=getConfigInfoValues(subscriptionFileName,'tenantID',infoFileLocation).strip('"')

print("Client Id: "+client_id +" Secret : " + client_secret+" tenantID : "+tenant)

# login using service principle
credentials = ServicePrincipalCredentials(
    client_id=client_id,
    secret=client_secret,
    tenant=tenant
)
client = ResourceManagementClient(credentials, subscriptionId)

# Print out all the resource group presents in the subscription
for item in client.resource_groups.list():
    print(item)