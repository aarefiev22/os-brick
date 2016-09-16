# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import requests
import json

SPDK_JSONRPC_IP_ADDRESS_BASE = '127.0.0.1'
SPDK_JSONRPC_PORT_BASE = 5260
SPDK_JSONRPC_INSTANCE_ID_BASE = 0


class RPCException(Exception):
    pass


class NVMeRPCClient(object):

    def __init__(self, ip_address, port, instance_id):
        ip_address = ip_address or SPDK_JSONRPC_IP_ADDRESS_BASE
        port = port or SPDK_JSONRPC_PORT_BASE
        instance_id = instance_id or SPDK_JSONRPC_INSTANCE_ID_BASE

        self.url = "http://{ip_address}:{port}{instance_id}/jsonrpc".format(
            ip_address=ip_address, port=port, instance_id=instance_id)
        self.headers = {'content-type': 'application/json'}
        self.payload = {'jsonrpc': '2.0', 'id': 0}

    def call(self, method, params):
        self.payload['method'] = method
        self.payload['params'] = params

        response = requests.post(
            self.url,
            data=json.dumps(self.payload),
            headers=self.headers).json()

        if 'error' in response:
            raise RPCException(response['error']['message'])

        return response
