import requests


class ApiClient:

    def __init__(self, base_url, login, password):
        self.base_url = base_url
        self.login = login
        self.password = password

    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        return requests.get(url, auth=(self.login, self.password))

    def set(self, endpoint, params):
        url = f"{self.base_url}/{endpoint}"
        return requests.get(url, params=params, auth=(self.login, self.password))


class RFIDConfig(ApiClient):

    def get_params(self):
        return self.get("rfidconfig").json()

    def set_continuous_scanning(self, value):
        return self.set("rfidconfig", {"infiniteinventory": str(value).lower()}).json()

    def set_power_antenna(self, value, ch):
        params = {f"pwrant{ch}": value}
        return self.set("rfidconfig", params).json()

    def set_enable_antenna(self, value, ch):
        params = {f"enant{ch}": str(value).lower()}
        return self.set("rfidconfig", params).json()

    def set_enable_trigger(self, value, ch):
        params = {f"entrig{ch}": str(value).lower()}
        return self.set("rfidconfig", params).json()

####????????
    def set_trigger_state(self, value, ch):
        params = {f"triggered{ch}": value}
        return self.set("rfidconfig", params).json()

    def set_antenna_dependency(self, value):
        return self.set("rfidconfig", {"rf_session": value}).json()

    def set_repeattime(self, value):
        return self.set("rfidconfig", {"repeattime": value}).json()

    def set_min_hold_ms(self, value):
        return self.set("rfidconfig", {"min_hold_ms": value}).json()


class PeripheryConfig(ApiClient):

    def get_params(self):
        return self.get("peripheryconfig").json()

    def set_relay_unit_enable(self, value):
        return self.set("peripheryconfig", {"smartboard_enable": str(value).lower()}).json()

    def set_relay_enable(self, value, ch):
        params = {f"smartboard_port{ch}_enable": str(value).lower()}
        return self.set("peripheryconfig", params).json()

    def set_relay_timer(self, value, ch):
        params = {f"smartboard_port{ch}_timer": str(value).lower()}
        return self.set("peripheryconfig", params).json()

    def set_wiegand_enable(self, value, ch):
        params = {f"wiegand{ch}_enable": str(value).lower()}
        return self.set("peripheryconfig", params).json()

    def set_wiegand_type(self, value):
        return self.set("peripheryconfig", {"wiegand1_type": value}).json()

    def set_wiegand_shift_bytes(self, value):
        return self.set("peripheryconfig", {"wiegand1_shift_bytes": value}).json()

    def set_wiegand_source(self, value):
        return self.set("peripheryconfig", {"wiegand1_source": value}).json()

    def set_beep_on_start(self, value):
        return self.set("peripheryconfig", {"beep_on_start": str(value).lower()}).json()

    def set_timeout_logical(self, value):
        return self.set("peripheryconfig", {"timeout_logical_0": value}).json()

    def set_timeout_next_bit(self, value):
        return self.set("peripheryconfig", {"timeout_next_bit": value}).json()


class TagIdentity(ApiClient):

    def get_params(self):
        return self.get("tagidentity").json()

    def get_tag_identity(self):
        return self.get("tagidentity?taglist=true").json()

    def get_tag_list(self):
        return self.get("taglist").json()

    def set_valid_time_ms(self, value):
        return self.set("tagidentity", {"validtime_ms": value}).json()

    ###????
    def set_hold_time_ms(self, value):
        return self.set("tagidentity", {"hold_time_ms": value}).json()

    def set_rssi_filter_value(self, value):
        return self.set("tagidentity", {"rssi_filter_value": -value}).json()

    def set_rssi_filter_enable(self, value):
        return self.set("tagidentity", {"rssi_filter_enable": str(value).lower()}).json()

    def set_epc_access_password(self, value):
        return self.set("tagidentity", {"epc_access_password": value}).json()

    def set_epc_filter_value(self, value, filter):
        params = {f"epc_filter_value{filter}": str(value).lower()}.json()
        return self.set("tagidentity", params)

    def set_epc_filter_enable(self, value, filter):
        params = {f"epc_filter_enable{filter}": str(value).lower()}.json()
        return self.set("tagidentity", params)

    def set_beep_on_tag(self, value):
        return self.set("tagidentity", {"beep_on_tag": str(value).lower()}).json()

    # def set_extra_mem_read(self, value):
    #     url = f"{self.base_url}/tagidentity?extra_mem_read=bool"
    #     data = {"extra_mem_read": value}
    #     response = requests.get(url, data=data)
    #     return response
    #
    # def set_extra_mem_bank(self, value):
    #     url = f"{self.base_url}/tagidentity?extra_mem_bank=value"
    #     data = {"extra_mem_bank": value}
    #     response = requests.get(url, data=data)
    #     return response
    #
    # def set_data_start_words(self, value):
    #     url = f"{self.base_url}/tagidentity?data_start_words=value"
    #     data = {"data_start_words": value}
    #     response = requests.get(url, data=data)
    #     return response
    #
    # def set_data_len_words(self, value):
    #     url = f"{self.base_url}/tagidentity?data_len_words=value"
    #     data = {"data_len_words": value}
    #     response = requests.get(url, data=data)
    #     return response

    def set_notify_uart(self, value):
        return self.set("tagidentity", {"notify_uart": str(value).lower()}).json()

    def set_notify_uart_json(self, value):
        return self.set("tagidentity", {"notify_uart_json": value}).json()

    def set_add_prefix(self, value):
        return self.set("tagidentity", {"add_prefix": value}).json()

    def set_add_epcl(self, value):
        return self.set("tagidentity", {"add_epcl": str(value).lower()}).json()

    def set_add_epc(self, value):
        return self.set("tagidentity", {"add_epc": str(value).lower()}).json()

    def set_add_tidl(self, value):
        return self.set("tagidentity", {"add_tidl": str(value).lower()}).json()

    def set_add_tid(self, value):
        return self.set("tagidentity", {"add_tid": str(value).lower()}).json()

    # def set_add_suffix(self, value):
    #     return self.set("tagidentity", {"add_suffix": value})

    def set_add_crlf(self, value):
        return self.set("tagidentity", {"add_crlf": str(value).lower()}).json()

    def set_add_ant(self, value):
        return self.set("tagidentity", {"add_ant": str(value).lower()}).json()

    def set_add_rssi(self, value):
        return self.set("tagidentity", {"add_rssi": str(value).lower()}).json()

    def set_notify_uart_alive(self, value):
        return self.set("tagidentity", {"notify_uart_alive": str(value).lower()}).json()

    def set_notify_uart_speed(self, value):
        return self.set("tagidentity", {"notify_uart_speed": value}).json()

    def set_notify_ip(self, value):
        return self.set("tagidentity", {"notify_ip": value}).json()

    def set_notify_port(self, value):
        return self.set("tagidentity", {"notify_port": value}).json()

    def set_notify_time_lim_ms(self, value):
        return self.set("tagidentity", {"notify_time_lim_ms": value}).json()

    def set_notify_enable(self, value):
        return self.set("tagidentity", {"notify_enable": str(value).lower()}).json()


class NetworkConfig(ApiClient):

    def get_netinfo(self):
        return self.get("netinfo").json()

    def set_sta_enable(self, value):
        return self.set("netinfo", {"sta_enable": str(value).lower()}).json()

    def set_ap_enable(self, value):
        return self.set("netinfo", {"ap_enable": str(value).lower()}).json()

    def set_wificonnect(self, ssid, password, safe):
        data = {"ssid": ssid, "pass": password, "safe": safe}
        return self.set("wificonnect", data).json()

    def scan_wifi(self):
        return self.get("scan").json()


class SystemCommands(ApiClient):
    def logout(self):
        return self.get("logout")

    def get_messagelog(self):
        return self.get("messagelog").json()

    def get_version(self):
        return self.get("version").json()

    def reboot(self):
        return self.get("reboot")

    def beep_device(self):
        return self.get("beepdevice")

    def inventory_once(self):
        return self.get("inventory_once")

    def set_relay(self):
        return self.get("relay1")
