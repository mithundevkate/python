from zeep import Client
import base64
## define source and target pods

source_client = Client(wsdl ="https://ekww-test.fa.us6.oraclecloud.com/xmlpserver/services/v2/CatalogService?wsdl")
target_client = Client(wsdl ="https://ekww.fa.us6.oraclecloud.com/xmlpserver/services/v2/CatalogService?wsdl")

## Check if folder exists on target POD

try :
    folder_exists =  source_client.service.getFolderContents('/~CASEY.BROWN/Drafts/','CASEY.BROWN','zklAO/aa1s{38T<U')
    print(folder_exists)
    if folder_exists:
        print("Update the folder contents with source pod data")
        print("------------------------- Get Source POD Folder Contents --------------------------------------")
        try:
             get_source_pod_data = source_client.service.getFolderContents('/~CASEY.BROWN/Drafts/','CASEY.BROWN','zklAO/aa1s{38T<U')

             ## get objects from folder
             for j in get_source_pod_data.values():
                 for i in j: ## fetch absolute path
                     download_object = source_client.service.downloadObject('%s','CASEY.BROWN','zklAO/aa1s{38T<U') % i['absolutePath']
                     ## check if object is downloaded
                     print(download_object)
                     ## check if object exists on target pod
                     target_object_exists = target_client.service.objectExist('%s','CASEY.BROWN','zklAO/aa1s{38T<U') % i['absolutePath']

                     if target_object_exists == False:
                     ##upload object
                        upload_object_to_destination = target_client.service.uploadObject('/~CASEY.BROWN/Drafts/Person Profile','xdoz',download_object,'CASEY.BROWN','zklAO/aa1s{38T<U')
                        print(upload_object_to_destination)
                        #print(i['absolutePath'])
        except Exception as e :
            print(e)

except Exception as e :
    print(e)

check_folder_contents_source = source_client.service.getFolderContents('/~CASEY.BROWN/Drafts/','CASEY.BROWN','zklAO/aa1s{38T<U')
print(check_folder_contents_source)

print (set(check_folder_contents_source)-set(folder_exists))
'''
## download report / any other object from source pod
download_object = source_client.service.downloadObject('/Human Capital Management/Career/Profiles/Person Profile.xdo','CASEY.BROWN','zklAO/aa1s{38T<U')

## check if object is downloaded
print(download_object)

## check if object exists on target pod
target_object_exists = target_client.service.objectExist('/~CASEY.BROWN/Drafts/Person Profile.xdo','CASEY.BROWN','zklAO/aa1s{38T<U')

if target_object_exists == False:
    ##upload object
    upload_object_to_destination = target_client.service.uploadObject('/~CASEY.BROWN/Drafts/Person Profile','xdoz',download_object,'CASEY.BROWN','zklAO/aa1s{38T<U')
    print(upload_object_to_destination)

## get folder contents

getFolderContents1 =  source_client.service.getFolderContents('/~CASEY.BROWN/Drafts/','CASEY.BROWN','zklAO/aa1s{38T<U')
print(getFolderContents1)

'''
