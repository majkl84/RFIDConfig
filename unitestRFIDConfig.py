import unittest
from unittest.mock import patch

import requests

from RFIDConfig import RFIDConfig, PeripheryConfig, TagIdentity, NetworkConfig, SystemCommands


class TestRFIDConfig(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://example.com/api"
        self.login = "test_login"
        self.password = "test_password"
        self.rfid_config = RFIDConfig(self.base_url, self.login, self.password)

    @patch("requests.get")
    def test_get_params(self, mock_get):
        mock_return_value = mock_get.return_value
        mock_return_value.json.return_value = {"test": "data"}

        response = self.rfid_config.get_params()

        mock_get.assert_called_once_with(
            f"{self.base_url}/rfidconfig",
            auth=(self.login, self.password)
        )
        self.assertEqual(response, {"test": "data"})

    @patch("requests.get")
    def test_set_continuous_scanning(self, mock_get):
        self.rfid_config.set_continuous_scanning(True)

        mock_get.assert_called_once_with(
            f"{self.base_url}/rfidconfig",
            params={"infiniteinventory": "true"},
            auth=(self.login, self.password)
        )

    @patch("requests.get")
    def test_set_power_antenna(self, mock_get):
        power_value = 30
        self.rfid_config.set_power_antenna(power_value)

        mock_get.assert_called_once_with(
            f"{self.base_url}/rfidconfig",
            params={"pwrant1": power_value},
            auth=(self.login, self.password)
        )

    @patch("requests.get")
    def test_set_enable_antenna(self, mock_get):
        enable_value = True
        self.rfid_config.set_enable_antenna(enable_value)

        mock_get.assert_called_once_with(
            f"{self.base_url}/rfidconfig",
            params={"enant1": "true"},
            auth=(self.login, self.password)
        )

    @patch("requests.get")
    def test_set_enable_trigger(self, mock_get):
        enable_value = False
        self.rfid_config.set_enable_trigger(enable_value)

        mock_get.assert_called_once_with(
            f"{self.base_url}/rfidconfig",
            params={"entrig1": "false"},
            auth=(self.login, self.password)
        )

    @patch("requests.get")
    def test_set_trigger_state(self, mock_get):
        state_value = "ready"
        self.rfid_config.set_trigger_state(state_value)

        mock_get.assert_called_once_with(
            f"{self.base_url}/rfidconfig",
            params={"triggered1": state_value},
            auth=(self.login, self.password)
        )

    @patch("requests.get")
    def test_set_antenna_dependency(self, mock_get):
        dependency_value = 1
        self.rfid_config.set_antenna_dependency(dependency_value)

        mock_get.assert_called_once_with(
            f"{self.base_url}/rfidconfig",
            params={"rf_session": dependency_value},
            auth=(self.login, self.password)
        )

    @patch("requests.get")
    def test_set_repeattime(self, mock_get):
        repeat_time = 500
        self.rfid_config.set_repeattime(repeat_time)

        mock_get.assert_called_once_with(
            f"{self.base_url}/rfidconfig",
            params={"repeattime": repeat_time},
            auth=(self.login, self.password)
        )

    @patch("requests.get")
    def test_set_min_hold_ms(self, mock_get):
        hold_time = 1000
        self.rfid_config.set_min_hold_ms(hold_time)

        mock_get.assert_called_once_with(
            f"{self.base_url}/rfidconfig",
            params={"min_hold_ms": hold_time},

            auth=(self.login, self.password)
        )

class TestPeripheryConfig(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://example.com/api"
        self.login = "test_login"
        self.password = "test_password"
        self.config = PeripheryConfig(self.base_url, self.login, self.password)

    @patch("requests.get")
    def test_get_params(self, mock_get):
        mock_return_value = mock_get.return_value
        mock_return_value.json.return_value = {"test": "data"}

        response = self.config.get_params()

        mock_get.assert_called_once_with(
            f"{self.base_url}/peripheryconfig",
            auth=(self.login, self.password)
        )
        self.assertEqual(response, {"test": "data"})

    @patch("requests.get")
    def test_set_relay_unit_enable(self, mock_get):
        value = True
        self.config.set_relay_unit_enable(value)

        mock_get.assert_called_once_with(
            f"{self.base_url}/peripheryconfig",
            params={"smartboard_enable": "true"},
            auth=(self.login, self.password)
        )

    @patch("requests.get")
    def test_set_relay_enable(self, mock_get):
        value = False
        ch = 1
        self.config.set_relay_enable(value, ch)

        mock_get.assert_called_once_with(
            f"{self.base_url}/peripheryconfig",
            params={"smartboard_port1_enable": "false"},
            auth=(self.login, self.password)
        )

    @patch("requests.get")
    def test_set_relay_timer(self, mock_get):
        value = 500
        ch = 2
        self.config.set_relay_timer(value, ch)

        mock_get.assert_called_once_with(
            f"{self.base_url}/peripheryconfig",
            params={"smartboard_port2_timer": "500"},
            auth=(self.login, self.password)
        )

    @patch("requests.get")
    def test_set_wiegand_enable(self, mock_get):
        value = True
        ch = 1
        self.config.set_wiegand_enable(value, ch)

        mock_get.assert_called_once_with(
            f"{self.base_url}/peripheryconfig",
            params={"wiegand1_enable": "true"},
            auth=(self.login, self.password)
        )

    @patch("requests.get")
    def test_set_wiegand_type(self, mock_get):
       value = "26bit"
       self.config.set_wiegand_type(value)

       mock_get.assert_called_once_with(
           f"{self.base_url}/peripheryconfig",
           params={"wiegand1_type": value},
           auth=(self.login, self.password)
       )

class TestTagIdentity(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://example.com/api"
        self.login = "test_login"
        self.password = "test_password"
        self.tag_identity = TagIdentity(self.base_url, self.login, self.password)

    @patch("requests.get")
    def test_get_params(self, mock_get):
        mock_return_value = mock_get.return_value
        mock_return_value.json.return_value = {"test": "data"}

        response = self.tag_identity.get_params()

        mock_get.assert_called_once_with(
            f"{self.base_url}/tagidentity",
            auth=(self.login, self.password)
        )
        self.assertEqual(response, {"test": "data"})

    @patch("requests.get")
    def test_get_tag_list(self, mock_get):
        self.tag_identity.get_tag_list()

        mock_get.assert_called_once_with(
            f"{self.base_url}/tagidentity?taglist=true",
            auth=(self.login, self.password)
        )

    @patch("requests.get")
    def test_set_valid_time_ms(self, mock_get):
        value = 1000
        self.tag_identity.set_valid_time_ms(value)

        mock_get.assert_called_once_with(
            f"{self.base_url}/tagidentity",
            params={"validtime_ms": value},
            auth=(self.login, self.password)
        )

    @patch("requests.get")
    def test_set_hold_time_ms(self, mock_get):
        value = 500
        self.tag_identity.set_hold_time_ms(value)

        mock_get.assert_called_once_with(
            f"{self.base_url}/tagidentity",
            params={"hold_time_ms": value},
            auth=(self.login, self.password)
        )

    @patch("requests.get")
    def test_set_rssi_filter_value(self, mock_get):
        value = -70
        self.tag_identity.set_rssi_filter_value(value)

        mock_get.assert_called_once_with(
            f"{self.base_url}/tagidentity",
            params={"rssi_filter_value": -value},
            auth=(self.login, self.password)
        )

class TestNetworkConfig(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://example.com/api"
        self.login = "test_login"
        self.password = "test_password"
        self.network = NetworkConfig(self.base_url, self.login, self.password)

    @patch("requests.get")
    def test_get_netinfo(self, mock_get):
        mock_return_value = mock_get.return_value
        mock_return_value.json.return_value = {"test": "data"}

        response = self.network.get_netinfo()

        mock_get.assert_called_once_with(
            f"{self.base_url}/netinfo",
            auth=(self.login, self.password)
        )
        self.assertEqual(response, {"test": "data"})

    @patch("requests.get")
    def test_set_sta_enable(self, mock_get):
        value = True
        self.network.set_sta_enable(value)

        mock_get.assert_called_once_with(
            f"{self.base_url}/netinfo",
            params={"sta_enable": "true"},
            auth=(self.login, self.password)
        )

    @patch("requests.get")
    def test_set_ap_enable(self, mock_get):
        value = False
        self.network.set_ap_enable(value)

        mock_get.assert_called_once_with(
            f"{self.base_url}/netinfo",
            params={"ap_enable": "false"},
            auth=(self.login, self.password)
        )

    @patch("requests.get")
    def test_set_wificonnect(self, mock_get):
        ssid = "test_ssid"
        password = "test_password"
        safe = True

        self.network.set_wificonnect(ssid, password, safe)

        mock_get.assert_called_once_with(
            f"{self.base_url}/wificonnect",
            params={"ssid": ssid, "pass": password, "safe": safe},
            auth=(self.login, self.password)
        )

    @patch("requests.get")
    def test_scan_wifi(self, mock_get):
        self.network.scan_wifi()

        mock_get.assert_called_once_with(
            f"{self.base_url}/scan",
            auth=(self.login, self.password)
        )

class TestSystemCommands(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://example.com/api"
        self.login = "test_login"
        self.password = "test_password"
        self.system = SystemCommands(self.base_url, self.login, self.password)

    @patch("requests.get")
    def test_logout(self, mock_get):
        self.system.logout()

        mock_get.assert_called_once_with(
            f"{self.base_url}/logout",
            auth=(self.login, self.password)
        )

    @patch("requests.get")
    def test_get_messagelog(self, mock_get):
        mock_return_value = mock_get.return_value
        mock_return_value.json.return_value = {"messages": ["test"]}

        response = self.system.get_messagelog()

        mock_get.assert_called_once_with(
            f"{self.base_url}/messagelog",
            auth=(self.login, self.password)
        )
        self.assertEqual(response, {"messages": ["test"]})

    @patch("requests.get")
    def test_get_version(self, mock_get):
        mock_return_value = mock_get.return_value
        mock_return_value.json.return_value = {"version": "1.0"}

        response = self.system.get_version()

        mock_get.assert_called_once_with(
            f"{self.base_url}/version",
            auth=(self.login, self.password)
        )
        self.assertEqual(response, {"version": "1.0"})

    @patch("requests.get")
    def test_reboot(self, mock_get):
        self.system.reboot()

        mock_get.assert_called_once_with(
            f"{self.base_url}/reboot",
            auth=(self.login, self.password)
        )

    @patch("requests.get")
    def test_beep_device(self, mock_get):
        self.system.beep_device()

        mock_get.assert_called_once_with(
            f"{self.base_url}/beepdevice",
            auth=(self.login, self.password)
        )

    @patch("requests.get")
    def test_inventory_once(self, mock_get):
        self.system.inventory_once()

        mock_get.assert_called_once_with(
            f"{self.base_url}/inventory_once",
            auth=(self.login, self.password)
        )

    @patch("requests.get")
    def test_set_relay(self, mock_get):
        time = 1000

        self.system.set_relay(time)

        mock_get.assert_called_once_with(
            f"{self.base_url}/relay1",
            params={"time": time},
            auth=(self.login, self.password)
        )