import oci

config = oci.config.from_file("~/.oci/config","DEFAULT")

object = oci.waas.WaasClient(config)

identity_client = oci.identity.IdentityClient(config, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)
compartments = oci.pagination.list_call_get_all_results(
        identity_client.list_compartments,
        config['tenancy']
    ).data


Compartment_id="ocid1.compartment.oc1..aaaaaaaahorst72sqd5bc5swqses2rqzjioknzovvlzq5eyiwbh7z2olefvq"
#functions.clear()
print ("Getting all WAF Policy objects")
#for Compartment in compartments:
items = oci.pagination.list_call_get_all_results(object.list_waas_policies, Compartment_id).data
#print (items)

if len(items) != 0 :

    for item in items:
    #if (item.lifecycle_state != "DELETED"):
           # AllItems.append(item)
        print("- {} - {} - {}".format(item.display_name, item.lifecycle_state , item.id))
        print ("\n")
        print("Deleting: {}".format(item.display_name))
        object.delete_waas_policy(waas_policy_id=item.id)
else:
    print ("No WAF policies are associated !!")
