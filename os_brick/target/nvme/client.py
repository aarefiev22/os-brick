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

import json
import requests

from os_brick import exception


class NVMeRPCClient(object):

    def __init__(self, ip_address='127.0.0.1', port=5260, instance_id=0):
        self.url = "http://{ip_address}:{port}/jsonrpc".format(
            ip_address=ip_address, port=port + instance_id)
        self.headers = {'content-type': 'application/json'}
        self.payload = {'jsonrpc': '2.0', 'id': 1}

    def call(self, method, params):
        self.payload['method'] = method
        self.payload['params'] = params

        response = requests.post(
            self.url,
            data=json.dumps(self.payload),
            headers=self.headers).json()

        if 'error' in response:
            raise exception.NVMeRPCException(
                message=response['error']['message'])

        return response
