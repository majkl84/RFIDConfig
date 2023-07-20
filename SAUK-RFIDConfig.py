import requests


class RFIDConfig:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_params(self):
        url = f"{self.base_url}/rfidconfig?infiniteinventory=bool"
        response = requests.get(url)
        return response.json()

    def set_infinite_inventory(self, value):
        url = f"{self.base_url}/rfidconfig?infiniteinventory=bool"
        data = {"infiniteinventory": value}
        response = requests.post(url, data=data)
        return response

    def set_power_antenna(self, value):
        url = f"{self.base_url}/rfidconfig?pwrant1=value"
        data = {"pwrant1": value}
        response = requests.post(url, data=data)
        return response

    def set_enable_antenna(self, value):
        url = f"{self.base_url}/rfidconfig?enant1=bool"
        data = {"enant1": value}
        response = requests.post(url, data=data)
        return response

    def set_enable_trigger(self, value):
        url = f"{self.base_url}/rfidconfig?entrig1=bool"
        data = {"entrig1": value}
        response = requests.post(url, data=data)
        return response

    def set_trigger_state(self, value):
        url = f"{self.base_url}/rfidconfig?triggered1=value"
        data = {"triggered1": value}
        response = requests.post(url, data=data)
        return response

    def set_antenna_dependency(self, value):
        url = f"{self.base_url}/rfidconfig?rf_session=value"
        data = {"rf_session": value}
        response = requests.post(url, data=data)
        return response

    def set_repeattime(self, value):
        url = f"{self.base_url}/rfidconfig?repeattime=value"
        data = {"repeattime": value}
        response = requests.post(url, data=data)
        return response

    def set_min_hold_ms(self, value):
        url = f"{self.base_url}/rfidconfig/min_hold_ms=value"
        data = {"min_hold_ms": value}
        response = requests.post(url, data=data)
        return response