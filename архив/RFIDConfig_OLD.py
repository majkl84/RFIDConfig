import requests


class RFIDConfig:
    def __init__(self, base_url, login, password):
        self.base_url = base_url
        self.login = login
        self.password = password

### Настройка параметров RFID-тракта (rfidconfig)
    def get_params(self):
        url = f"{self.base_url}/rfidconfig"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        params = response.json()
        return params

    def set_continuous_scanning(self, value):
        url = f"{self.base_url}/rfidconfig?infiniteinventory={str(value).lower()}"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        return response

    def set_power_antenna(self, value):
        url = f"{self.base_url}/rfidconfig?pwrant1={value}"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        return response

    def set_enable_antenna(self, value):
        url = f"{self.base_url}/rfidconfig?enant1={str(value).lower()}"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        return response

    def set_enable_trigger(self, value):
        url = f"{self.base_url}/rfidconfig?entrig1={str(value).lower()}"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        return response

    def set_trigger_state(self, value):
        url = f"{self.base_url}/rfidconfig?triggered1={value}"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        return response

    def set_antenna_dependency(self, value):
        url = f"{self.base_url}/rfidconfig?rf_session={value}"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        return response

    def set_repeattime(self, value):
        url = f"{self.base_url}/rfidconfig?repeattime={value}"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        return response

    def set_min_hold_ms(self, value):
        url = f"{self.base_url}/rfidconfig?min_hold_ms={value}"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        return response

################################################################

### Настройка параметров периферийных устройств (peripheryconfig)

    def get_periphery_params(self):
        url = f"{self.base_url}/peripheryconfig"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        params = response.json()
        return params

    def set_relay_unit_enable(self, value):
        url = f"{self.base_url}/peripheryconfig?smartboard_enable={str(value).lower()}"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        return response

    def set_relay_enable(self, value, ch):
        url = f"{self.base_url}/peripheryconfig?smartboard_port{ch}_enable={str(value).lower()}"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        return response
    def set_relay_timer(self, value, ch):
        url = f"{self.base_url}/peripheryconfig?smartboard_port{ch}_timer={value}"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        return response

    def set_wiegand_enable(self, value, ch):
        url = f"{self.base_url}/peripheryconfig?wiegand{ch}_enable={str(value).lower()}"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        return response
    def set_wiegand_type(self, value):
        url = f"{self.base_url}/peripheryconfig?wiegand1_type={value}"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        return response
    def set_wiegand_shift_bytes(self, value):
        url = f"{self.base_url}/peripheryconfig?wiegand1_shift_bytes={value}"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        return response
    def set_wiegand_source(self, value):
        url = f"{self.base_url}/peripheryconfig?wiegand1_source={value}"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        return response
    def set_beep_on_start(self, value):
        url = f"{self.base_url}/peripheryconfig?beep_on_start={str(value).lower()}"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        return response
    def set_timeout_logical(self, value):
        url = f"{self.base_url}/peripheryconfig?timeout_logical_0={value}"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        return response


    def set_timeout_next_bit(self, value):
        url = f"{self.base_url}/peripheryconfig?timeout_next_bit={value}"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        return response

########################################################################

### Настройка параметров идентификации RFID-меток (tagidentity)

    def get_tag_identity_params(self):
        url = f"{self.base_url}/tagidentity"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        params = response.json()
        return params

    def set_tag_list(self):
        url = f"{self.base_url}/tagidentity?taglist=true"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        params = response.json()
        return params

    def set_valid_time_ms(self, value):
        url = f"{self.base_url}/tagidentity?validtime_ms={value}"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        return response
###????
    def set_hold_time_ms(self, value):
        url = f"{self.base_url}/tagidentity?hold_time_ms={value}"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        return response

    def set_rssi_filter_value(self, value):
        url = f"{self.base_url}/tagidentity?rssi_filter_value={-value}"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        return response

    def set_rssi_filter_enable(self, value):
        url = f"{self.base_url}/tagidentity?rssi_filter_enable={str(value).lower()}"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        return response

    def set_epc_access_password(self, value):
        url = f"{self.base_url}/tagidentity?epc_access_password={value}"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        return response

    def set_epc_filter_value(self, value, filter):
        url = f"{self.base_url}/tagidentity?epc_filter_value{filter}={value}"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        return response

    def set_epc_filter_enable(self, value, filter):
        url = f"{self.base_url}/tagidentity?epc_filter_enable{filter}={str(value).lower()}"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        return response

    def set_beep_on_tag(self, value):
        url = f"{self.base_url}/tagidentity?beep_on_tag={str(value).lower()}"
        response = requests.get(url, auth=(self.login, self.password))
        response.raise_for_status()
        return response

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

########################################################################

###Настройка уведомлений о RFID-метках, отправляемых по каналу уведомлений UART (RS232, RS485)

    def set_notify_uart(self, value):
        url = f"{self.base_url}/tagidentity?notify_uart=bool"
        data = {"notify_uart": value}
        response = requests.get(url, data=data)
        return response

    def set_notify_uart_json(self, value):
        url = f"{self.base_url}/tagidentity?notify_uart_json=value"
        data = {"notify_uart_json": value}
        response = requests.get(url, data=data)
        return response

    def set_add_prefix(self, value):
        url = f"{self.base_url}/tagidentity?add_prefix=String"
        data = {"add_prefix": value}
        response = requests.get(url, data=data)
        return response

    def set_add_epcl(self, value):
        url = f"{self.base_url}/tagidentity?add_epcl=bool"
        data = {"add_epcl": value}
        response = requests.get(url, data=data)
        return response

    def set_add_epc(self, value):
        url = f"{self.base_url}/tagidentity?add_epc=bool"
        data = {"add_epc": value}
        response = requests.get(url, data=data)
        return response

    def set_add_tidl(self, value):
        url = f"{self.base_url}/tagidentity?add_tidl=bool"
        data = {"add_tidl": value}
        response = requests.get(url, data=data)
        return response

    def set_add_tid(self, value):
        url = f"{self.base_url}/tagidentity?add_tid=bool"
        data = {"add_tid": value}
        response = requests.get(url, data=data)
        return response

    def set_add_suffix(self, value):
        url = f"{self.base_url}/tagidentity?add_suffix=String"
        data = {"add_suffix": value}
        response = requests.get(url, data=data)
        return response

    def set_add_crlf(self, value):
        url = f"{self.base_url}/tagidentity?add_crlf=bool"
        data = {"add_crlf": value}
        response = requests.get(url, data=data)
        return response

    def set_add_ant(self, value):
        url = f"{self.base_url}/tagidentity?add_ant=bool"
        data = {"add_ant": value}
        response = requests.get(url, data=data)
        return response

    def set_add_rssi(self, value):
        url = f"{self.base_url}/tagidentity?add_rssi=bool"
        data = {"add_rssi": value}
        response = requests.get(url, data=data)
        return response

    def set_notify_uart_alive(self, value):
        url = f"{self.base_url}/tagidentity?notify_uart_alive=bool"
        data = {"notify_uart_alive": value}
        response = requests.get(url, data=data)
        return response

    def set_notify_uart_speed(self, value):
        url = f"{self.base_url}/tagidentity?notify_uart_speed=value"
        data = {"notify_uart_speed": value}
        response = requests.get(url, data=data)
        return response

################################################################

###Настройка параметров уведомления хоста (tagidentity/notify)

    def set_notify_ip(self, value):
        url = f"{self.base_url}/tagidentity?notify_ip=value"
        data = {"notify_ip": value}
        response = requests.get(url, data=data)
        return response

    def set_notify_port(self, value):
        url = f"{self.base_url}/tagidentity?notify_port=value"
        data = {"notify_port": value}
        response = requests.get(url, data=data)
        return response

    def set_notify_time_lim_ms(self, value):
        url = f"{self.base_url}/tagidentity?notify_time_lim_ms=value"
        data = {"notify_time_lim_ms": value}
        response = requests.get(url, data=data)
        return response

    def set_notify_enable(self, value):
        url = f"{self.base_url}/tagidentity?notify_enable=bool"
        data = {"notify_enable": value}
        response = requests.get(url, data=data)
        return response

########################################################################

###Команды для работы с Wi-Fi сетью или Ethernet (netinfo, wificonnect, scan)

    def get_netinfo(self):
        url = f"{self.base_url}/netinfo"
        response = requests.get(url)
        return response

    def set_sta_enable(self, value):
        url = f"{self.base_url}/netinfo?sta_enable=bool"
        data = {"sta_enable": value}
        response = requests.get(url, data=data)
        return response

    def set_ap_enable(self, value):
        url = f"{self.base_url}/netinfo?ap_enable=bool"
        data = {"ap_enable": value}
        response = requests.get(url, data=data)
        return response

    def set_wificonnect(self, ssid, password, safe):
        url = f"{self.base_url}/wificonnect"
        data = {"ssid": ssid, "pass": password, "safe": safe}
        response = requests.get(url, data=data)
        return response

    def scan_wifi(self):
        url = f"{self.base_url}/scan"
        response = requests.get(url)
        return response

################################################################

###Сервисные команды общего назначения

    def logout(self):
        url = f"{self.base_url}/logout"
        response = requests.get(url)
        return response

    def get_messagelog(self):
        url = f"{self.base_url}/messagelog"
        response = requests.get(url)
        return response

    def get_version(self):
        url = f"{self.base_url}/version"
        response = requests.get(url)
        return response

    def reboot(self):
        url = f"{self.base_url}/reboot"
        response = requests.get(url)
        return response

    def beep_device(self):
        url = f"{self.base_url}/beepdevice"
        response = requests.get(url)
        return response

    def inventory_once(self):
        url = f"{self.base_url}/inventory_once"
        response = requests.get(url)
        return response

    def set_relay1(self, time):
        url = f"{self.base_url}/relay1"
        data = {"time": time}
        response = requests.get(url, data=data)
        return response

################################################################

# if __name__ == '__main__':
#
#     rfid_config = RFIDConfig("http://192.168.2.245", "admin", "admin")
#     response = rfid_config.set_infinite_inventory(True)
#     print(response.status_code)
#     print(response.text)
#     assert response.status_code == 200
#
#     params = rfid_config.get_params()
#     assert params["infiniteinventory"] == True

