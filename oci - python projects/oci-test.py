import oci
import requests
config = oci.config.from_file("~/.oci/config","Non-Federation")
identity_client = oci.identity.IdentityClient(config, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)
compartments = oci.pagination.list_call_get_all_results(
        identity_client.list_compartments,
        config['tenancy']
    ).data
resource_manager_client1 = oci.resource_manager.ResourceManagerClient(config, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)

groups = oci.pagination.list_call_get_all_results(
        identity_client.list_groups,
        compartment_id = config['tenancy']
    ).data

policies =  oci.pagination.list_call_get_all_results(
        identity_client.list_policies,
        compartment_id = "ocid1.compartment.oc1..aaaaaaaa5eokm7keodwu3va3aruswvovcgrb4mqscnty6fql2fr7vdtzxfxq"
    ).data


stacks = oci.pagination.list_call_get_all_results(resource_manager_client1.list_stacks ,compartment_id="ocid1.compartment.oc1..aaaaaaaa5eokm7keodwu3va3aruswvovcgrb4mqscnty6fql2fr7vdtzxfxq").data

for i in policies:
    #if i.description == "Policy Created by Python Script" and i.lifecycle_state == "ACTIVE" and i.name.__contains__("mdev-test3") == True :
    print (i.name)

for i in groups:
    if i.description == "Group created by A-team automated script" and i.lifecycle_state == "ACTIVE" and i.name.__contains__("mdev-test3") == True :
        print (1)

idp = oci.pagination.list_call_get_all_results(
        identity_client.list_idp_group_mappings,
        identity_provider_id="ocid1.saml2idp.oc1..aaaaaaaaqx5kbnmuzddw3gxzu6ycshcxhwoik7bee7ycvrm5mp2hrw6yaqkq"
    ).data
'''
for i in idp:
    #print (i.idp_group_name)
    print(1)
'''
#x1 = identity_client.delete_idp_group_mapping(identity_provider_id="ocid1.saml2idp.oc1..aaaaaaaaqx5kbnmuzddw3gxzu6ycshcxhwoik7bee7ycvrm5mp2hrw6yaqkq",mapping_id="ocid1.idpgroupmapping.oc1..aaaaaaaavdmmankv6kztv32vruj4cdrcjems3sh6k4zsle2z2uq543y5zfkq")

#y = identity_client.delete_idp_group_mapping(identity_provider_id="ocid1.saml2idp.oc1..aaaaaaaaqx5kbnmuzddw3gxzu6ycshcxhwoik7bee7ycvrm5mp2hrw6yaqkq",mapping_id="ocid1.idpgroupmapping.oc1..aaaaaaaae75f42cvalyrbok22lzjiow2rlpvuxeiyxt5bc5s5jvterp6upzq").data
#y1 = identity_client.list_identity_providers(compartment_id=config['tenancy'],protocol="https").data

#z = identity_client.delete_compartment(compartment_id="ocid1.compartment.oc1..aaaaaaaaul4cizcxcvuxhl3birflieeo32wrezflobeuwlqcn3ntqzzzwaxq").data
#print (z)

import  time

import timeit
waas_cl = oci.waas.WaasClient(config)

'''
try:
   # url = "https://waas.us-ashburn-1.oraclecloud.com/"
   # page = requests.get(url, verify=False)
    y = oci.pagination.list_call_get_all_results(waas_cl.list_waas_policies, compartment_id="ocid1.tenancy.oc1..aaaaaaaadymht6gout6mc5yhsqo4syry4inm2kc44s5o4s7c3re2ylgs66xa").data
    #time.sleep(30)
    if y == []:
        print ("overtime")

    print (y)
except Exception as e:
    print (e)
'''
x  = oci.pagination.list_call_get_all_results(
        identity_client.list_region_subscriptions,
        config['tenancy']
    ).data
z= ([i.region_name for i in  oci.pagination.list_call_get_all_results(
        identity_client.list_region_subscriptions,
        config['tenancy']
    ).data])
y = "''".join([i.region_name for i in  oci.pagination.list_call_get_all_results(
        identity_client.list_region_subscriptions,
        config['tenancy']
    ).data if i.is_home_region == True])

idcs_id = "ocid1.saml2idp.oc1..aaaaaaaaqx5kbnmuzddw3gxzu6ycshcxhwoik7bee7ycvrm5mp2hrw6yaqkq"

# get the list of idp mapped groups
idcs = oci.pagination.list_call_get_all_results(
        identity_client.list_idp_group_mappings,
        identity_provider_id=idcs_id
    ).data



idp_group_id =identity_client.get_idp_group_mapping(identity_provider_id=idcs_id,mapping_id="ocid1.idpgroupmapping.oc1..aaaaaaaacwxhpvzseqr7h5fvi2exy3bgkjjk427xd6nuuauvlaccoz6ckera").data

print(idp_group_id)
