from RFIDConfig import RFIDConfig, PeripheryConfig, TagIdentity

base_url = "http://192.168.2.245"
login = "admin"
password = "admin"

rfid_config = RFIDConfig(base_url, login, password)
periphery_config = PeripheryConfig(base_url, login, password)
tag_identity = TagIdentity(base_url, login, password)

# rfid_config.set_continuous_scanning(False)
# periphery_config.set_relay_unit_enable(True)
# periphery_config.set_relay_enable(True, 1)
# tag_identity.set_beep_on_tag(True)
params = tag_identity.get_tag_list()
print(params)