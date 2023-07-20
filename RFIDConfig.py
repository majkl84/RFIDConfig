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
        return self.set("rfidconfig", {"infiniteinventory": str(value).lower()})

    def set_power_antenna(self, value):
        return self.set("rfidconfig", {"pwrant1": value})

    def set_enable_antenna(self, value):
        return self.set("rfidconfig", {"enant1": str(value).lower()})

    def set_enable_trigger(self, value):
        return self.set("rfidconfig", {"entrig1": str(value).lower()})

    def set_trigger_state(self, value):
        return self.set("rfidconfig", {"triggered1": value})

    def set_antenna_dependency(self, value):
        return self.set("rfidconfig", {"rf_session": value})

    def set_repeattime(self, value):
        return self.set("rfidconfig", {"repeattime": value})

    def set_min_hold_ms(self, value):
        return self.set("rfidconfig", {"min_hold_ms": value})

class PeripheryConfig(ApiClient):

    def get_params(self):
        return self.get("peripheryconfig").json()

    def set_relay_unit_enable(self, value):
        return self.set("peripheryconfig", {"smartboard_enable": str(value).lower()})

    def set_relay_enable(self, value, ch):
        params = {f"smartboard_port{ch}_enable": str(value).lower()}
        return self.set("peripheryconfig", params)

    def set_relay_timer(self, value, ch):
        params = {f"smartboard_port{ch}_timer": str(value).lower()}
        return self.set("peripheryconfig", params)

    def set_wiegand_enable(self, value, ch):
        params = {f"wiegand{ch}_enable": str(value).lower()}
        return self.set("peripheryconfig", params)

    def set_wiegand_type(self, value):
        return self.set("peripheryconfig", {"wiegand1_type": value})

    def set_wiegand_shift_bytes(self, value):
        return self.set("peripheryconfig", {"wiegand1_shift_bytes": value})

    def set_wiegand_source(self, value):
        return self.set("peripheryconfig", {"wiegand1_source": value})

    def set_beep_on_start(self, value):
        return self.set("peripheryconfig", {"beep_on_start": str(value).lower()})

    def set_timeout_logical(self, value):
        return self.set("peripheryconfig", {"timeout_logical_0": value})


    def set_timeout_next_bit(self, value):
        return self.set("peripheryconfig", {"timeout_next_bit": value})

class TagIdentity(ApiClient):

    def get_params(self):
        return self.get("tagidentity").json()

    def get_tag_list(self):
        return self.get("tagidentity?taglist=true").json()

    def set_valid_time_ms(self, value):
        return self.set("tagidentity", {"validtime_ms": value})
###????
    def set_hold_time_ms(self, value):
        return self.set("tagidentity", {"hold_time_ms": value})

    def set_rssi_filter_value(self, value):
        return self.set("tagidentity", {"rssi_filter_value": -value})

    def set_rssi_filter_enable(self, value):
        return self.set("tagidentity", {"rssi_filter_enable": str(value).lower()})

    def set_epc_access_password(self, value):
        return self.set("tagidentity", {"epc_access_password": value})

    def set_epc_filter_value(self, value, filter):
        params = {f"epc_filter_value{filter}": str(value).lower()}
        return self.set("tagidentity", params)

    def set_epc_filter_enable(self, value, filter):
        params = {f"epc_filter_enable{filter}": str(value).lower()}
        return self.set("tagidentity", params)

    def set_beep_on_tag(self, value):
        return self.set("tagidentity", {"beep_on_tag": str(value).lower()})

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
        return self.set("tagidentity", {"notify_uart": str(value).lower()})

    def set_notify_uart_json(self, value):
        return self.set("tagidentity", {"notify_uart_json": value})

    def set_add_prefix(self, value):
        return self.set("tagidentity", {"add_prefix": value})

    def set_add_epcl(self, value):
        return self.set("tagidentity", {"add_epcl": str(value).lower()})

    def set_add_epc(self, value):
        return self.set("tagidentity", {"add_epc": str(value).lower()})

    def set_add_tidl(self, value):
        return self.set("tagidentity", {"add_tidl": str(value).lower()})

    def set_add_tid(self, value):
        return self.set("tagidentity", {"add_tid": str(value).lower()})

    # def set_add_suffix(self, value):
    #     return self.set("tagidentity", {"add_suffix": value})

    def set_add_crlf(self, value):
        return self.set("tagidentity", {"add_crlf": str(value).lower()})

    def set_add_ant(self, value):
        return self.set("tagidentity", {"add_ant": str(value).lower()})

    def set_add_rssi(self, value):
        return self.set("tagidentity", {"add_rssi": str(value).lower()})

    def set_notify_uart_alive(self, value):
        return self.set("tagidentity", {"notify_uart_alive": str(value).lower()})

    def set_notify_uart_speed(self, value):
        return self.set("tagidentity", {"notify_uart_speed": value})

    def set_notify_ip(self, value):
        return self.set("tagidentity", {"notify_ip": value})

    def set_notify_port(self, value):
        return self.set("tagidentity", {"notify_port": value})

    def set_notify_time_lim_ms(self, value):
        return self.set("tagidentity", {"notify_time_lim_ms": value})

    def set_notify_enable(self, value):
        return self.set("tagidentity", {"notify_enable": str(value).lower()})


class NetworkConfig(ApiClient):

    def get_netinfo(self):
        return self.get("netinfo").json()

    def set_sta_enable(self, value):
        return self.set("netinfo", {"sta_enable": str(value).lower()})

    def set_ap_enable(self, value):
        return self.set("netinfo", {"ap_enable": str(value).lower()})

    def set_wificonnect(self, ssid, password, safe):
        data = {"ssid": ssid, "pass": password, "safe": safe}
        return self.set("wificonnect", data)

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

  def set_relay(self, time):
    return self.set("relay1", {"time": time})

