"""Start or stop tagged Azure VMs on a schedule."""

import os
import argparse
from dotenv import load_dotenv
from azure.identity import ClientSecretCredential
from azure.mgmt.compute import ComputeManagementClient

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--action", choices=["start", "stop"], required=True)
args = parser.parse_args()

credential = ClientSecretCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    client_id=os.getenv("AZURE_CLIENT_ID"),
    client_secret=os.getenv("AZURE_CLIENT_SECRET"),
)

client = ComputeManagementClient(credential, os.getenv("AZURE_SUBSCRIPTION_ID"))

for vm in client.virtual_machines.list_all():
    rg = vm.id.split("/")[4]
    print(f"{args.action.upper()}: {vm.name} in {rg}")
    if args.action == "stop":
        client.virtual_machines.begin_deallocate(rg, vm.name)
    else:
        client.virtual_machines.begin_start(rg, vm.name)

print("Done.")
