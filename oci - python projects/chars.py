import oci
import requests
import logging
import base64
from oci.identity.models.create_idp_group_mapping_details import CreateIdpGroupMappingDetails


config = oci.config.from_file("~/.oci/config", "Non-Federation")
# print (config)
# def getIDCSAccessToken():
IDCS_HOST = "https://idcs-806d3cca94db49c9b8d1aeacc7d889e0.identity.oraclecloud.com"
encodedCreds = "MGU0NDE3YTEwYmRlNGIwY2JjYjJjYTgzMzViNTg2ODM6MjczZWZlOTYtNDUzOC00Zjk5LTg1YzUtOTVjZmE3OGI2YTg5"

# def getIDCSAccessToken():
try:
    # config = oci.config.from_file()
    idcs_encoded_client_id_secret = str(config.get("idcs_encoded_client_id_secret"))

    # PRODUCTION: For python 2.7 comment out follwoing one. it works only in python 3.6
    idcs_admin_username = str(base64.b64decode(config.get("idcs_admin_username")), "utf-8")
    idcs_admin_password = str(base64.b64decode(config.get("idcs_admin_password")), "utf-8")

    logging.debug(
        "IDCS username-password-encoded_client id_secret: " + idcs_admin_username + "-" + idcs_admin_password + "-" + encodedCreds)

    # get OAuth token
    url = IDCS_HOST + '/oauth2/v1/token'
    headers = {'Authorization': 'Basic ' + idcs_encoded_client_id_secret + ''}
    body = {'grant_type': 'password', 'scope': 'urn:opc:idm:__myscopes__', 'username': idcs_admin_username,
            'password': idcs_admin_password}
    atReq = requests.post(url, headers=headers, data=body)
    print('IDCS OAuth Access token retrieved')
    # print(atReq.json())
    accessToken = atReq.json()['access_token']
    # print("Access token fetched====== \n " + accessToken)
    # return accessToken

    headers = {'Authorization': 'Bearer ' + accessToken, 'Content-Type': 'application/scim+json'}

    #logging.debug("IDP group "+idp_group_name)
    #logging.debug("OCI group ID "+oci_group_id)
    #config = oci.config.from_file()
   # config = oci.config.from_file("~/.oci/config","Non-Federation")

    identity = oci.identity.IdentityClient(config)
    request = CreateIdpGroupMappingDetails()
    request._group_id="ocid1.group.oc1..aaaaaaaaesxcwcfrvidh46tqoabaotlyrqqmvery3is7geun2rapm2tvezca"
    request._idp_group_name="OCI_Administrators"
    request.compartment_id = "ocid1.tenancy.oc1..aaaaaaaadymht6gout6mc5yhsqo4syry4inm2kc44s5o4s7c3re2ylgs66xa"
    response = identity.create_idp_group_mapping(request, identity_provider_id="ocid1.saml2idp.oc1..aaaaaaaaqx5kbnmuzddw3gxzu6ycshcxhwoik7bee7ycvrm5mp2hrw6yaqkq")
    print("mapping status "+str(response.status))
    #return response.data.id
    print("mapping data "+str(response.data))
except Exception as e:
    print("Exception while trying to get access token \n" + str(e))



    '''
    group_id = "8ce489009369432f88b04767a3ab6aa5"
    displayName = "test-mdev"
    seacrh_group_id_idcs = IDCS_HOST + '/admin/v1/Groups?attributes=displayName,id&filter=displayName+eq+%22{}%22'.format(displayName)
    # print (delete_group_url)
    response = ""
    response_1 = ""
    try:
        response = requests.get(seacrh_group_id_idcs, headers=headers)
        # print(response.json())
        print("Group Searching response Status_code: " + str(response.status_code))

        if response.status_code == 200:
            print("-- Delete the IDCS group id --> %s  " %  (response.json()['Resources'][0]['id']))
            delete_idcs_group = IDCS_HOST + '/admin/v1/Groups/%s' % (response.json()['Resources'][0]['id'])
            '''
    '''
            response_1 = requests.delete(delete_idcs_group, headers=headers)
            if response_1.status_code == 204:
                print('Deleted group name --> %s' % (response.json()['Resources'][0]['displayName']))
                print('Deleted Group ID is --> %s' % (response.json()['Resources'][0]['id']))
            elif response.status_code == 404:
                print("Group you are trying to delete is already deleted or not found ")
                print("FAILED")
            

        elif response.status_code == 404:
            print("Group you are trying to search is already deleted or not found ")
            print("FAILED")
        else:
            print("Group searching failed. Below is the response content")
            print(str(response.content))
    except Exception as e:
        print("Exception while deleting IDCS Group \n" + str(e))

except Exception as e:
    print("Exception while trying to get access token \n" + str(e))
    # return "FAILED"

# def deleteGroupinIDCS(accessToken):

# return "FAILED"


# group_id = a308fa274667477f8be2ffc65364dc53
# group_name = test

# a = getIDCSAccessToken()
# b = deleteGroupinIDCS(accessToken=a)
'''
