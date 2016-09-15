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

import os

from oslo_log import log as logging
from oslo_service import loopingcall

from os_brick import exception
from os_brick import initiator

from os_brick.i18n import _LI
from os_brick.initiator.connectors import base
from os_brick import utils

DEVICE_SCAN_ATTEMPTS_DEFAULT = 3
LOG = logging.getLogger(__name__)


class NVMeoFabricConnector(base.BaseLinuxConnector):
    """Connector class to attach/detach NVMe over fabric volumes."""

    def __init__(self, root_helper, driver=None,
                 device_scan_attempts=initiator.DEVICE_SCAN_ATTEMPTS_DEFAULT,
                 *args, **kwargs):
        super(NVMeoFabricConnector, self).__init__(
            root_helper,
            driver=driver,
            device_scan_attempts=device_scan_attempts,
            *args, **kwargs)

    @staticmethod
    def get_connector_properties(root_helper, *args, **kwargs):
        """The NVMe connector properties."""
        return {}

    def get_search_path(self):
        return '/dev  '

    def get_volume_paths(self, connection_properties):
        raise NotImplementedError

    @utils.trace
    def connect_volume(self, connection_properties):
        """Discover and attach the volume.

        :param connection_properties: The dictionary that describes all
                                      of the target volume attributes.
        :type connection_properties: dict
        :returns: dict

        connection_properties for NVMe must include:
        TODO (e0ne): add connection_properties description
        """
        raise NotImplementedError

    @utils.trace
    def disconnect_volume(self, connection_properties, device_info):
        """Detach and flush the volume.

        :param connection_properties: The dictionary that describes all
                                      of the target volume attributes.
        :type connection_properties: dict
        :param device_info: historical difference, but same as connection_props
        :type device_info: dict

        connection_properties for NVMe must include:
        TODO (e0ne): add connection_properties description
        """
        raise NotImplementedError

    def extend_volume(self, connection_properties):
        # TODO(e0ne): is this possible?
        raise NotImplementedError
