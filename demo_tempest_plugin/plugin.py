'''
Tempest Plugin implementation

@author:luzC

'''
import os

from tempest import config
from tempest.test_discover import plugins
from demo_tempest_plugin import config as plugin_cfg


class sayHiPlugin(plugins.TempestPlugin):
    def get_opt_lists(self):
        return [(
            plugin_cfg.share_group.name,
            plugin_cfg.ShareGroup)]

    def load_tests(self):
        base_path = os.path.split(os.path.dirname(
            os.path.abspath(__file__)))[0]
        test_dir = "demo_tempest_plugin/tests"
        full_test_dir = os.path.join(base_path, test_dir)
        return full_test_dir, base_path

    def register_opts(self, conf):
        config.register_opt_group(
            conf,
            plugin_cfg.service_available_group,
            plugin_cfg.ServiceAvailableGroup)
        config.register_opt_group(
            conf,
            plugin_cfg.share_group,
            plugin_cfg.ShareGroup)

