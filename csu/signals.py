
from core.service_signals import ServiceSignalBindType
from core.signals import bind_service_signal
import requests
import json
from policy.models import Policy
from insuree.models import Insuree

def bind_service_signals():
    bind_service_signal(
        'policy_service.create', _on_add_policy, ServiceSignalBindType.AFTER)


def _on_add_policy(*args, **kwargs):
    data = kwargs.get('result', None)
    print("The policy ", data)
    if data:
        familyid = data.family_id
        policies = Policy.objects.filter(family_id=familyid).exclude(id=data.id)
        print("All policies ", policies)
        if not policies:
            # This is the first policy the famiily just had, lets send enrollement to camerhealth
            # Note: One insuree equals to One familly
            url = "http://3.137.55.229:8006/v1/auth/token/"

            payload = json.dumps({
                "email": "openimis@minsante.cm ",
                "password": "OpenImis1*"
            })
            headers = {
            'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            response_data = response.json()
            print("Response ", response_data)

            token = response_data.get('access', False)
            print("token ", token)

            if token:
                insurees = Insuree.objects.filter(family=familyid)
                print("insurees ", insurees)
                for insuree in insurees:

                    url = "http://3.137.55.229:8006/v1/enrollments/open_imis_enrol/?mpi="+str(insuree.chf_id)

                    payload={}
                    headers = {
                    'Authorization': 'Bearer ' + str(token)
                    }

                    response = requests.request("GET", url, headers=headers, data=payload)

                    print(response.json())
