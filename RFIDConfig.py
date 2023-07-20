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

