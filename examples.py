from RFIDConfig import RFIDConfig, PeripheryConfig, TagIdentity, NetworkConfig, SystemCommands
import pprint
base_url = "http://192.168.2.245" # IP address устройства
login = "admin" # Логин для устройства
password = "admin" # Пароль для устройства

rfid_config = RFIDConfig(base_url, login, password)
periphery_config = PeripheryConfig(base_url, login, password)
tag_identity = TagIdentity(base_url, login, password)
net_config = NetworkConfig(base_url, login, password)
system = SystemCommands(base_url, login, password)


### Настройка параметров RFID-тракта (rfidconfig)

# params = rfid_config.get_params()
# params = rfid_config.set_continuous_scanning(True) # Непрерывное сканирование
# params = rfid_config.set_power_antenna(19, 1) # задаем мощность антенны
# params = rfid_config.set_enable_antenna(True, 1) # вкл/выкл антенны
# params = rfid_config.set_enable_trigger(True, 1) # вкл/выкл Hold триггера
# params = rfid_config.set_trigger_state(1, 1) # вкл/выкл конкретной антенны для Hold триггера ???????
# params = rfid_config.set_antenna_dependency(4)
# params = rfid_config.set_repeattime(1)
# params = rfid_config.set_min_hold_ms(5000)

################################################################

### Настройка параметров периферийных устройств (peripheryconfig)

params = periphery_config.get_params()
# params = periphery_config.set_relay_unit_enable(False) # вкл/выкл блока реле
# params = periphery_config.set_relay_enable(True, 1) # вкл/выкл реле в метод передаем True/False и № реле
# params = periphery_config.set_relay_timer(400, 1) # в метод передаем значение ms и № реле
# params = periphery_config.set_wiegand_enable(True, 1) # в метод передаем True/False и № Wiegand
# params = periphery_config.set_wiegand_type(34) # в метод передаем тип Wiegand 26/34
# params = periphery_config.set_wiegand_shift_bytes(2)
# params = periphery_config.set_wiegand_source(1)
# params = periphery_config.set_beep_on_start(True)
# params = periphery_config.set_timeout_logical(100)
# params = periphery_config.set_timeout_next_bit(900)

################################################################

### Настройка параметров идентификации RFID-меток (tagidentity)

# params = tag_identity.get_params()
# params = tag_identity.get_tag_list()
# params = tag_identity.set_valid_time_ms(5000)
# params = tag_identity.set_hold_time_ms(2000) # глюк в интерфейсе
# params = tag_identity.set_rssi_filter_value(50)
# params = tag_identity.set_rssi_filter_enable(False)
# params = tag_identity.set_epc_access_password(00000000)
# params = tag_identity.set_epc_filter_value("E280699500", 2)
# params = tag_identity.set_epc_filter_enable(True, 1)
# params = tag_identity.set_beep_on_tag(True)
# - set_extra_mem_read() - Чтение дополнительного сектора памяти. Элемент проверка «Свой-чужой»
# - set_extra_mem_bank() - Номер банка памяти из которого будем читать данные. Элемент проверка «Свой-чужой»
# - set_data_start_words() - Первый блок памяти который будет читаться (в словах, по 2 байта)
# - set_data_len_words() - Количество данных, которые будут читаться (в словах, по 2 байта


################################################################

###Настройка уведомлений о RFID-метках, отправляемых по каналу уведомлений UART (RS232, RS485)

# params = tag_identity.set_notify_uart(True)
# params = tag_identity.set_notify_uart_json(0)
# params = tag_identity.set_add_prefix() # - к посылке по UART добавить префикс, строка до 4 байт ????
# params = tag_identity.set_add_epcl(1) # - к посылке по UART добавить длину EPC-кода (измеряемую в байтах)
# params = tag_identity.set_add_epc(1) # - к посылке по UART добавить код EPC
# params = tag_identity.set_add_tidl(1) # - к посылке по UART добавить длину TID-кода (измеряемую в байтах)
# params = tag_identity.set_add_tid(1) # - к посылке по UART добавить код TID
# params = tag_identity.set_add_suffix(1) # - к посылке по UART добавить префикс, строка до 4 байт
# params = tag_identity.set_add_crlf(1) # - к посылке по UART добавлять «возврат каретки \r 0x0D CR» и «перевод строки \n 0x0A LF»
# params = tag_identity.set_add_ant(1) # - к посылке по UART добавить номер антенны, которая обнаружила метку
# params = tag_identity.set_add_rssi(1) # - к посылке по UART добавить силу сигнала от метки RSSI
# params = tag_identity.set_notify_uart_alive(False)
# params = tag_identity.set_notify_uart_speed(115200)

################################################################

###Настройка параметров уведомления хоста (tagidentity/notify)

# params = tag_identity.set_notify_ip("192.168.1.55")
# params = tag_identity.set_notify_port(8090)
# params = tag_identity.set_notify_time_lim_ms(500)
# params = tag_identity.set_notify_enable(True)

##########################################

###Команды для работы с Wi-Fi сетью или Ethernet (netinfo, wificonnect, scan)

# params = net_config.get_netinfo()
# params = net_config.set_sta_enable(True)
# params = net_config.set_ap_enable(True)
# params = net_config.set_wificonnect("wifi_ssid", "password123", True)
# params = net_config.scan_wifi()

################################################################

###class SystemCommands():

# system.logout() # - выход из web-интерфейса
# params = system.get_messagelog() # - получить лог сообщений
# params = system.get_version()
# system.reboot()
# system.beep_device() # - звуковой сигнал
# system.inventory_once() # - однократная инвентаризация
# system.set_relay()

################################################################

pprint.pprint(params)
