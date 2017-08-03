FIM Baseline Example
-

This is sample code and is not supported.  The code will create a Halo server group, move a workload to the group,
create a FIM policy, and create a FIM baseline.

API Setup

A) Install the CloudPassage SDK

Type: pip install cloudpassage
Configure the SDK
Type: sudo vi /etc/cloudpassage.yaml
defaults:
key_id: 
secret_key: 
api_hostname: api.cloudpassage.com
api_port: 443

or

export HALO_API_KEY=
export HALO_API_SECRET_KEY=
export HALO_API_HOSTNAME=api.cloudpassage.com

Files
-

1) app - the execution code and application code

a) runner.py - runs the code

b) app/fim_baseline_example

- __init__.py - init code
- config_helper.py - configuration.  The user will need to set os.environ["SERVER_IP"] = "" with an IP address to use
for the example.
- fim_baseline_example.py - the example

c) fim_policy - a JSON FIM policy

d) halo_general - a wrapper for the Halo API that will be pulled from GitHub

Use
-

python app/runner.py

Output
-

$ python app/runner.py
Checking if baseline is active...

Baseline is Pending... will check again shortly...

Checking if baseline is active...

Baseline is Pending... will check again shortly...

Checking if baseline is active...

Baseline is active...

Then you can go into the portal and look at the group, baseline etc.
