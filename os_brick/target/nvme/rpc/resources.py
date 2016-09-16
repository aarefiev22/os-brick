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

from os_brick.target.nvme.client import NVMeRPCClient


# TODO(apopovych): create common NVMe Exception class
# and move it to seprate errors.py file
class NVMeParamException(Exception):
    pass


class NVMeTargetObject(object):

    def __init__(self):
        self.client = NVMeRPCClient()


class InitiatorGroup(NVMeTargetObject):

    def get(self):
        """Display current initiator group configuration.

        :returns: dict
        """

        return self.client.call('get_initiator_group')

    def add(self, tag, initiators, netmasks):
        """Add an initiator group.

        :param tag: initiator group tag
        :type tag: int
        :param initiators: list of initiator hostnames or IP addresses,
                           enclosed in quotes.  Example: ['ALL'] or
                           ['127.0.0.1', '192.168.200.100'].
        :type initiators: list of strings
        :param netmasks: list of initiator netmasks enclosed in quotes.
                         Example: ['255.255.0.0', '255.248.0.0'].
        :type netmasks: list of strings
        :returns: None
        """

        if not (tag > 0):
            raise NVMeParamException('Tag value must be > 0')

        return self.client.call(
            'add_initiator_group', {
                'tag': tag,
                'initiators': initiators,
                'netmasks': netmasks
            })

    def delete(self, tag):
        """Delete an initiator group.

        :param tag: initiator group tag
        :type tag: int
        :returns: None
        """

        if not (tag > 0):
            raise NVMeParamException('Tag value must be > 0')

        return self.client.call('delete_initiator_group', {'tag': tag})


class PortalGroup(NVMeTargetObject):

    def get(self):
        """Display current portal group configuration.

        :returns: dict
        """

        return self.client.call('get_portal_groups')

    def add(self, tag, portals):
        """Add a portal group.

        :param tag: portal group tag
        :type tag: int
        :param portals: list of portals in 'host:port' format. Example:
                        ['192.168.100.100:3260', '192.168.100.100:3261']
        :type portals: list of strings
        :returns: None
        """

        if not (tag > 0):
            raise NVMeParamException('Tag value must be > 0')

        return self.client.call(
            'add_portal_group', {
                'tag': tag,
                'portals': portals
            })

    def delete(self, tag):
        """Delete a portal group.

        :param tag: portal group tag
        :type tag: int
        :returns: None
        """

        if not (tag > 0):
            raise NVMeParamException('Tag value must be > 0')

        return self.client.call('delete_portal_group', {'tag': tag})


class TargetNode(NVMeTargetObject):

    def get(self):
        """Display target nodes.

        :returns: dict
        """

        return self.client.call('get_target_nodes')

    def add(self, name, alias_name, pg_tags, ig_tags, lun_names, lun_ids,
            queue_depth, chap_disabled, chap_required, chap_mutual,
            chap_auth_group):
        """Add a target node.

        :param name: target node name (ASCII).
        :type name: string
        :param alias_name: target node alias name (ASCII).
        :type alias_name: string
        :param pg_tags: list of Portal Group Tags (int > 0).
        :type pg_tags: list of ints. Portal groups must pre-exist.
        :param ig_tags: list of Initiator Group Tag (int > 0).
        :type ig_tags: list of ints. Initiator group must pre-exist.
        :param lun_names: list of LUNs names. The LUNs must pre-exist.
        :type lun_names: list of strings.
        :param lun_ids: list of LUNs names. The LUNs must pre-exist.
        :type lun_ids: list of ints. LUN0 (id = 0) is required
        :param queue_depth: Desired target queue depth.
        :type queue_depth: int
        :param chap_disabled: CHAP authentication should be disabled for this
                              target node. Mutually exclusive with
                              chap_required.
        :type chap_disabled: int
        :param chap_required: CHAP authentication should be required for this
                              target node. Mutually exclusive with
                              chap_disabled.
        :type chap_required: int
        :param chap_mutual: CHAP authentication should be mutual/bidirectional.
        :type chap_mutual: int
        :param chap_auth_group: Authentication group ID for this target node.
                                Authentication group must be precreated.
        :type chap_auth_group: int
        """
        pass

    def delete(self):
        pass


class LUN(NVMeTargetObject):

    def get_active(self):
        pass

    def delete(self):
        pass

    def construct_with_aio(self, fname):
        pass

    def construct_with_malloc(self, fname):
        pass


class IpAddress(NVMeTargetObject):

    def add(self):
        pass

    def get(self):
        pass


class Trace(NVMeTargetObject):

    def get_flags(self):
        pass

    def set_flag(self, flag):
        pass

    def clear_flag(self, flag):
        pass


class Interface(NVMeTargetObject):

    def get(self):
        pass


class iSCSI(NVMeTargetObject):

    def get_connections(self):
        pass

    def get_devices(self):
        pass


class Instance(NVMeTargetObject):

    def kill(sig_name):
        pass
