import oci
import requests

config = oci.config.from_file("~/.oci/config", "Non-Federation")
identity_client = oci.identity.IdentityClient(config, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)


#print (config['tenancy'])
ll= oci.pagination.list_call_get_all_results(
        identity_client.list_user_group_memberships,
        compartment_id=config['tenancy'],group_id = "ocid1.group.oc1..aaaaaaaazr2welzxrsjp6cclofvzqntiqyoeilpk42ygigxsr6xxvwnbh3uq"
    ).data

'''
if len(ll) > 0:
    for i in ll:
        print ("This user-group memebership id will be removed " , i.id)
        remove = identity_client.remove_user_from_group(user_group_membership_id=i.id)
        #print (i.user_id)
'''
group = identity_client.get_group(
    group_id="ocid1.group.oc1..aaaaaaaazr2welzxrsjp6cclofvzqntiqyoeilpk42ygigxsr6xxvwnbh3uq").data

#if group is not None:
 #   print(group)

email_client = oci.email.EmailClient(config)
email_senders = oci.pagination.list_call_get_all_results(email_client.list_senders, compartment_id=config['tenancy']).data
email_sus =  oci.pagination.list_call_get_all_results(email_client.list_suppressions, compartment_id=config['tenancy']).data
#print (email_senders)
#print (email_sus)

get_email = email_client.get_sender(sender_id= "ocid1.emailsender.oc1.iad.aaaaaaaagsj3gwspqzo4hndnylovzqrnogvzppa4m5nn2p5ccsleizdsru3a").data
print(get_email)

get_sus =  email_client.get_suppression(suppression_id="ocid1.emailsuppression.oc1..aaaaaaaaeebbcyir76m4acp4crz3bupwhuoj3wfyhk2fjavcomgugwlz7imq").data
print(get_sus)
