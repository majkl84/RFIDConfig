from RFIDConfig import RFIDConfig, PeripheryConfig, TagIdentity, NetworkConfig, SystemCommands

base_url = "http://192.168.2.245"
login = "admin"
password = "admin"

rfid_config = RFIDConfig(base_url, login, password)
periphery_config = PeripheryConfig(base_url, login, password)
tag_identity = TagIdentity(base_url, login, password)
net_config = NetworkConfig(base_url, login, password)
system = SystemCommands(base_url, login, password)

# rfid_config.set_continuous_scanning(False)
# periphery_config.set_relay_unit_enable(True)
# periphery_config.set_relay_enable(True, 1)
# tag_identity.set_beep_on_tag(True)
# params = tag_identity.get_tag_list()
# print(params)
# tag_identity.set_notify_uart(True)
# tag_identity.set_notify_uart_json(0)
# tag_identity.set_notify_uart_alive(False)
# tag_identity.set_notify_uart_speed(115200)
# tag_identity.set_notify_ip("192.168.1.55")
# tag_identity.set_notify_port(8090)
# tag_identity.set_notify_time_lim_ms(500)
# tag_identity.set_notify_enable(True)
# params = net_config.get_netinfo()
# print(params)
# net_config.set_sta_enable(True)
# net_config.set_ap_enable(True)
# net_config.set_wificonnect("wifi_ssid", "password123", True)
# params = net_config.scan_wifi()
# print(params)
# params = system.get_version()
# print(params)
# system.reboot()
# system.set_relay1(100)
