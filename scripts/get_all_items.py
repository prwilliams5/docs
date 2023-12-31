#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright 2021 Opensource ICT Solutions B.V.
# https://oicts.com
#
#version: 1.0.0
#date: 06-11-2021

'''This script can be used to get all items from a host when a trap is triggered. Use
of this script must be taken with caution as it may overload a host in critical moments.
'''


import json
import sys
import requests

url = ''
token = ''

headers = {'Content-Type': 'application/json'}

hostname    = sys.argv[1]

def main():
    hostid = hostid_get(token)
    itemid_array = itemid_get(hostid,token)
    update(itemid_array,token)

def hostid_get(token):
    payload = {}
    payload['jsonrpc'] = '2.0'
    payload['method'] = 'host.get'
    payload['params'] = {}
    payload['params']['output'] = ['hostid']
    payload['params']['filter'] = {}
    payload['params']['filter']['host'] = hostname
    payload['auth'] = token
    payload['id'] = 1


    #Doing the request
    request = requests.post(url, data=json.dumps(payload), headers=headers)
    data = request.json()

    hostid = data["result"][0]["hostid"]
    return hostid

def itemid_get(hostid,token):
    payload = {}
    payload['jsonrpc'] = '2.0'
    payload['method'] = 'item.get'
    payload['params'] = {}
    payload['params']['output'] = 'itemid'
    payload['params']['filter'] = {}
    payload['params']['filter']['host'] = hostname
    payload['params']['filter']['type'] = "0", "1", "3", "5", "8", "9", "10", "11", "12", "13", "14", "15", "16", "19", "20", "21"
    payload['auth'] = token
    payload['id'] = 1

    request = requests.post(url, data=json.dumps(payload), headers=headers)
    data = request.json()

    itemid_array = []
    for itemid in data['result']:
        itemid_array.append(str(itemid['itemid']))
    return itemid_array

def update(itemid_array,token):
    payload = {}
    payload['jsonrpc'] = '2.0'
    payload['method'] = 'task.create'
    payload['params'] = []
    for itemid in itemid_array:
        request = {}
        request['type'] = '6'
        request['request'] = {}
        request['request']['itemid'] = itemid
        payload['params'].append(request)
    payload['auth'] = token
    payload['id'] = 1

    request = requests.post(url, data=json.dumps(payload), headers=headers)
    data = request.json()
    json_string = json.dumps(data)

    print(json_string)

if __name__ == '__main__':
    main()
