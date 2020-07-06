from zeep import Client
import base64
## define source and target pods

source_client = Client(wsdl ="https://ekww-test.fa.us6.oraclecloud.com/xmlpserver/services/v2/CatalogService?wsdl")
target_client = Client(wsdl ="https://ekww.fa.us6.oraclecloud.com/xmlpserver/services/v2/CatalogService?wsdl")

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

#getFolderContents1 =  source_client.service.getFolderContents('/~CASEY.BROWN/Drafts/','CASEY.BROWN','zklAO/aa1s{38T<U')
#print(getFolderContents1)


