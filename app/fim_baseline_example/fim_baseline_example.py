import os
import sys

class FIM_BaselineExample(object):
    """
       This class shows a FIM Baseline example.
    """
    def __init__(self, halo):
        EMPTY = ""
        self.group_name = "fim_baseline_example"

        self.halo = halo

        # get a server object
        self.halo_server_obj = self.halo.get_server_obj()

        # get a FIM object
        self.halo_fim_obj = self.halo.get_fim_policy_obj()

        # get a server group object
        self.halo_server_group_object = self.halo.get_server_group_obj()

        # get a http helper obj
        self.halo_http_helper_obj = self.halo.get_http_helper_obj()

        # grab a server IP from the config
        self.server_ip = os.getenv("SERVER_IP")

        if self.server_ip == EMPTY:
            print "No server to use... exiting...\n"
            sys.exit(1)

        # get the server ID for later
        self.server_id = \
            self.halo.get_server_id_for_ip(self.halo_http_helper_obj,
                                           self.server_ip)

        # show example
        self.create_fim_baseline()

    def create_fim_baseline(self):
        EMPTY = 0
        FIRST = 0
        server_group_id = None
        fim_policy_id = ""

        # check to see if the group exists
        server_group_id = \
            self.halo.get_server_group_id_by_name(
                self.halo_server_group_object,
                self.group_name)

        # if it does not then create it and move the server there
        if server_group_id is None:
            server_group_id = self.create_server_group()
            self.assign_server_to_group(server_group_id)

        fim_policy_file_path = \
            "./fim_policy/CoreSystemFilesAmazonLinux_v2.1.json"

        # get the fim policy IDs
        fim_policy_ids = \
            self.halo.get_server_group_fim_policy_ids(
                self.halo_server_group_object,
                server_group_id)

        # if there is one then don't create it again
        # just an example as I don't check to make sure we are uding the
        # right one but I know it is here
        if len(fim_policy_ids) == EMPTY:
            fim_policy_id = self.halo.create_fim_policy(self.halo_fim_obj,
                                                        fim_policy_file_path)
            self.halo.update_server_group_fim_policy_ids(
                self.halo_server_group_object, fim_policy_id, server_group_id)
        else:
            fim_policy_id = fim_policy_ids[FIRST]

        # create the baseline
        halo_fim_baseline_obj = self.halo.get_fim_baseline_obj()
        fim_baseline_id = self.halo.create_fim_baseline(halo_fim_baseline_obj,
                                                        fim_policy_id,
                                                        self.server_id)

    # create a test server group
    def create_server_group(self):
        server_group_id = \
            self.halo.create_server_group(self.halo_server_group_object,
                                          self.group_name)

        return server_group_id

    # assign the server to the group
    def assign_server_to_group(self, server_group_id):
        self.halo.assign_server_to_group(self.halo_server_obj, self.server_id,
                                         server_group_id)

        return server_group_id