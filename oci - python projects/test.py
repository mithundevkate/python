import oci
import random
import time

config = oci.config.from_file("~/.oci/config","DEFAULT")
identity = oci.identity.IdentityClient(config)
user = identity.get_user(config["user"]).data
print(user.compartment_id)


import requests

#proxy = "61.233.25.166:80"
#proxy = "http://www-proxy-hqdc.us.oracle.com:80"

r = requests.get('http://www.google.com', proxies={"http":"http://www-proxy-hqdc.us.oracle.com:80"})
thedata = r.content
print (thedata)

'''
compartment_id = "ocid1.compartment.oc1..aaaaaaaaul4cizcxcvuxhl3birflieeo32wrezflobeuwlqcn3ntqzzzwaxq"
identity = oci.identity.IdentityClient(config)

example_namespace_name = 'examplens_{}'.format(random.randint(0, 1000000))
create_tag_namespace_response = identity.create_tag_namespace(
    oci.identity.models.CreateTagNamespaceDetails(
        compartment_id=compartment_id,
        name=example_namespace_name,
        description='Python SDK example tag namespace'
    )
)
tag_namespace_id = create_tag_namespace_response.data.id

tag_namespaces = identity.list_tag_namespaces(compartment_id).data
tags_in_namespace = identity.list_tags(tag_namespace_id).data

print (tag_namespaces , tags_in_namespace )
'''
