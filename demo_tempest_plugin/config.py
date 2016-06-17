'''
Tempest plugin configuration for say_hi packages

@author: luzC

'''
from oslo_config import cfg
from tempest import config


service_available_group = cfg.OptGroup(
    name="service_available",
    title="Available OpenStack Services"
)

ServiceAvailableGroup = [
    cfg.BoolOpt("dluxSay", default=True,
                help="Whether or not dluxsay is expected to be available")
]

share_group = cfg.OptGroup(
    name="say_hi",
    title="Say hi test variables"
)

ShareGroup = [
    cfg.StrOpt("extra_msg", default="Extra info from plugin config",
               help="Some extra message to print when saying hi.")
    cfg.BoolOpt("is_extra", default=True, 
               help="Whether or not to add text")
    cfg.IntOpt("extra_nums", default=0, help="Extra int quantity")
]
