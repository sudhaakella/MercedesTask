#!/usr/bin/env python2.7
import jenkins

# Connect to jenkins server
server = jenkins.Jenkins('http://localhost:9999', username='admin', password='8b41cca6b35f4d848cad9063bcf05035')
user = server.get_whoami()
version = server.get_version()

# Ensure connection is established
print('Hello %s from Jenkins %s' % (user['fullName'], version))

# Trigger the job per request basis
# TODO: Can add this trigger job logic based on future time to run or nightly/hourly runs
server.build_job('twentyfourhours', None, {'token': '11029df9cd4d283b5ccfeb0205dae57c1b'})

print('Triggered job: twentyfourhours')




