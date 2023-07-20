[TOC]

# SAUK-RFIDConfig

## class RFIDConfig:
 
    Класс для настройки параметров RFID-считывателя

----------------------------------------------------------------
##    Атрибуты:
    - base_url - базовый URL для запросов к RFID-считывателю
----------------------------------------------------------------
##    Методы:
### Настройка параметров RFID-тракт (rfidconfig) 
    - get_params() - получить текущие параметры конфигурации RFID
    - set_infinite_inventory() - установить режим инвентаризации
    - set_power_antenna() - установить мощность антенны 
    - set_enable_antenna() - вкл./выкл. антенну
    - set_enable_trigger() - вкл./выкл. триггер
    - set_trigger_state() - установить состояние триггера
    - set_antenna_dependency() - установить зависимость антенн
    - set_repeattime() - установить время повторной идентификации
    - set_min_hold_ms() - установить минимальное время удержания
### Настройка параметров периферийных устройств (peripheryconfig)    
    - get_periphery_params() - получить параметры периферии
    - set_relay1_enable() - вкл./выкл. реле
    - set_relay1_timer() - установить таймер для реле
    - set_wiegand1_enable() - вкл./выкл. Wiegand
    - set_wiegand1_type() - установить тип Wiegand
    - set_wiegand1_shift_bytes() - сдвиг байтов Wiegand
    - set_wiegand1_source() - источник данных Wiegand
    - set_beep_on_start() - вкл./выкл. звуковой сигнал
    - set_timeout_logical_0() - таймаут логического 0
    - set_timeout_next_bit() - таймаут следующего бита
### Настройка параметров идентификации RFID-меток (tagidentity)
    - get_tag_identity_params() - получить параметры идентификации
    - set_tag_list() - вкл./выкл. список меток
    - set_valid_time_ms() - время валидности метки
    - set_hold_time_ms() - время удержания метки
    - set_rssi_filter_value() - значение фильтра RSSI
    - set_rssi_filter_enable() - вкл./выкл. фильтр RSSI
    - set_epc_access_password() - пароль доступа к EPC
    - set_epc_filter_value1() - значение фильтра EPC
    - set_epc_filter_enable1() - вкл./выкл. фильтр EPC
    - set_beep_on_tag() - вкл./выкл. звук при считывании
    - set_extra_mem_read() - чтение доп. памяти
    - set_extra_mem_bank() - банк доп. памяти
    - set_data_start_words() - начало данных доп. памяти 
    - set_data_len_words() - длина данных доп. памяти
### Настройка уведомлений о RFID-метках, отправляемых по каналу уведомлений UART (RS232, RS485)
    - set_notify_uart() - вкл./выкл. уведомления UART
    - set_notify_uart_json() - формат JSON уведомлений UART
    - set_add_prefix() - добавить префикс в уведомление 
    - set_add_epcl() - добавить длину EPC
    - set_add_epc() - добавить EPC
    - set_add_tidl() - добавить длину TID
    - set_add_tid() - добавить TID
    - set_add_suffix() - добавить суффикс
    - set_add_crlf() - добавить CRLF 
    - set_add_ant() - добавить номер антенны
    - set_add_rssi() - добавить RSSI
    - set_notify_uart_alive() - отправка keep-alive
    - set_notify_uart_speed() - скорость UART
### Настройка параметров уведомления хоста (tagidentity/notify)
    - set_notify_ip() - IP адрес уведомлений 
    - set_notify_port() - порт уведомлений
    - set_notify_time_lim_ms() - таймаут уведомлений
    - set_notify_enable() - вкл./выкл. уведомлений
### Команды для работы с Wi-Fi сетью или Ethernet (netinfo, wificonnect, scan)
    - get_netinfo() - получить инфо о сети
    - set_sta_enable() - вкл./выкл. WiFi STA
    - set_ap_enable() - вкл./выкл. WiFi AP  
    - set_wificonnect() - подключиться к WiFi
    - scan_wifi() - сканирование WiFi
### Сервисные команды общего назначения
    - logout() - выход из web-интерфейса
    - get_messagelog() - получить лог сообщений
    - get_version() - получить версию ПО
    - reboot() - перезагрузка устройства
    - beep_device() - звуковой сигнал
    - inventory_once() - однократная инвентаризация
    - set_relay1() - управление реле 1
----------------------------------------------------------------
## Примеры
    rfid_config = RFIDConfig("http://192.168.10.1", "admin", "admin")
### Получение текущих настроек RFID:    
    params = rfid_config.get_params()
    print(params)

### Включение режима непрерывной инвентаризации:

    response = rfid_config.set_infinite_inventory(True)

### Установка мощности антенны на 20 дБм:

    rfid.set_power_antenna(20)

### Включение фильтра по RSSI -80 дБм:

    rfid.set_rssi_filter_enable(True)
    rfid.set_rssi_filter_value(80)

### Добавление префикса в уведомления UART:
 
    rfid.set_add_prefix("RFID:")

### Подключение к WiFi сети:

    rfid.set_wificonnect("MyWiFi", "password123", False)

### Перезагрузка устройства:

    rfid.reboot()

Таким образом, класс позволяет управлять всеми основными параметрами RFID-считывателя и интегрировать его в различные системы.