import unittest
from unittest.mock import patch

from SAUKRFIDConfig import RFIDConfig


class TestRFIDConfig(unittest.TestCase):

    def setUp(self):
        self.rfid = RFIDConfig("http://192.168.2.245", "admin", "admin")

    @patch('requests.get')
    def test_get_params(self, mock_get):
        self.rfid.get_params()
        mock_get.assert_called_with('http://192.168.2.245/rfidconfig?infiniteinventory=bool')

    @patch('requests.get')
    def test_set_infinite_inventory(self, mock_get):
        self.rfid.set_infinite_inventory(True)
        mock_get.assert_called_with('http://192.168.2.245/rfidconfig?infiniteinventory=bool',
                                     data={'infiniteinventory': True})

    @patch('requests.get')
    def test_set_power_antenna(self, mock_get):
        self.rfid.set_power_antenna(30)
        mock_get.assert_called_with('http://192.168.2.245/rfidconfig?pwrant1=value',
                                     data={'pwrant1': 30})

    # Тесты для остальных методов                                      

    def test_set_wificonnect(self):
        self.rfid.set_wificonnect('ssid', 'password', False)
        # проверка вызова requests.get с правильными параметрами

    def test_scan_wifi(self):
        self.rfid.scan_wifi()
        # проверка вызова requests.get

    def test_reboot(self):
        self.rfid.reboot()
        # проверка вызова requests.get


if __name__ == '__main__':
    unittest.main()