# SAUK-RFIDConfig

## Библиотека для настройки параметров RFID-считывателя

----------------------------------------------------------------
##    Атрибуты:
    - base_url - базовый URL для запросов к RFID-считывателю
    - login - пользователь устройства
    - password - пароль устройства
----------------------------------------------------------------
## class RFIDConfig:
### Настройка параметров RFID-тракт (rfidconfig) 
####    Методы:

    - get_params() - получить текущие параметры конфигурации RFID
    - set_continuous_scanning() - вкл./выкл. непрерывного сканирования
    - set_power_antenna() - установить мощность антенны 
    - set_enable_antenna() - вкл./выкл. антенну
    - set_enable_trigger() - вкл./выкл. триггер (hold)
    - set_trigger_state() - установить состояние триггера
                                1 – зависит от hold №1
                                2 – зависит от hold №2
                                3 – зависит от обоих портов hold
    - set_antenna_dependency() - Номер сессии (настройка параметров антиколлизии, тонкая настройка)
    - set_repeattime() - количество считываний RFID-меток (тонкая настройка)
    - set_min_hold_ms() - минимальное время включения цифрового триггерного порта Hold 
----------------------------------------------------------------
## class PeripheryConfig():
### Настройка параметров периферийных устройств (peripheryconfig)   
####    Методы:
    - get_params() - Запрос всех параметров
    - set_relay_unit_enable() - вкл./выкл. блок реле
    - set_relay_enable() - вкл./выкл. реле (передаем в метод состояние True/False и № реле)
    - set_relay_timer() - установить таймер для реле (передаем в метод время в ms и № реле)
    - set_wiegand_enable() - вкл./выкл. Wiegand (передаем в метод состояние True/False и № Wiegand)
    - set_wiegand_type() - установить тип Wiegand 26/34
    - set_wiegand_shift_bytes() - сдвиг байтов Wiegand
    - set_wiegand_source() - Источник данных для Wiegand (банк памяти метки EPC или TID) 
      Элемент проверки «Свой-чужой» (для того чтобы брать данные EPC отправить 1, TID отправить 0)
    - set_beep_on_start() - вкл./выкл. подачу звукового сигнала при включении прибора 
      (сигнал подается после загрузки)
    - set_timeout_logical() - Ширина логического сигнала по интерфейсу Wiegand
    - set_timeout_next_bit() - Период следования импульсов по интерфейсу Wiegand
----------------------------------------------------------------
## class TagIdentity():
### Настройка параметров идентификации RFID-меток (tagidentity)
####    Методы:
    - get_params() - возвращаем все параметры
    - set_tag_list() - возвращаем все параметры + таблицу идентификации
    - set_valid_time_ms() - Новое значение "Время сна RFID-метки", миллисекунды
    - set_hold_time_ms() - Новое значение "Время удержания метки в таблице инвентаризации", миллисекунды
    - set_rssi_filter_value() - Новое значение RSSI фильтра (всегда отрицательная величина), дБ
    - set_rssi_filter_enable() - вкл./выкл. проверку уровня сигнала от метки, RSSI
    - set_epc_access_password() - Пароль AccessPassord, который проверяется на метках Элемент проверки «Свой-чужой»
    - set_epc_filter_value() - значение фильтра EPC (передавать в метод надо значение и № фильтра)
    - set_epc_filter_enable() - вкл./выкл. проверку EPC-фильтра Элемент проверка «Свой-чужой» (передаем в метод состояние True/False и № фильтра)
    - set_beep_on_tag() - вкл./выкл. подачу звукового сигнала при обнаружении RFID-метки, если метка прошла процесс проверки «Свой-чужой»
    - set_extra_mem_read() - Чтение дополнительного сектора памяти. Элемент проверка «Свой-чужой»
    - set_extra_mem_bank() - Номер банка памяти из которого будем читать данные. Элемент проверка «Свой-чужой»
    - set_data_start_words() - Первый блок памяти который будет читаться (в словах, по 2 байта)
    - set_data_len_words() - Количество данных, которые будут читаться (в словах, по 2 байта
### Настройка уведомлений о RFID-метках, отправляемых по каналу уведомлений UART (RS232, RS485)
    - set_notify_uart() - вкл./выкл. уведомления UART
    - set_notify_uart_json() - Изменение протокола уведомлений: 
                                                0-байтовый, 
                                                1-JSON строки,
                                                2-строки ASCII
    - set_add_prefix() - к посылке по UART добавить префикс, строка до 4 байт
    - set_add_epcl() - к посылке по UART добавить длину EPC-кода (измеряемую в байтах)
    - set_add_epc() - к посылке по UART добавить код EPC
    - set_add_tidl() - к посылке по UART добавить длину TID-кода (измеряемую в байтах)
    - set_add_tid() - к посылке по UART добавить код TID
    - set_add_suffix() - к посылке по UART добавить префикс, строка до 4 байт
    - set_add_crlf() - к посылке по UART добавлять «возврат каретки \r 0x0D CR» и «перевод строки \n 0x0A LF» 
    - set_add_ant() - к посылке по UART добавить номер антенны, которая обнаружила метку
    - set_add_rssi() - к посылке по UART добавить силу сигнала от метки RSSI
    - set_notify_uart_alive() - Разрешить \ Запретить отправку сообщений KeepAlive по UART
    - set_notify_uart_speed() - Изменение скорости работы UART (RS232, RS485)
### Настройка параметров уведомления хоста (tagidentity/notify)
    - set_notify_ip() - IP адрес уведомлений 
    - set_notify_port() - порт уведомлений
    - set_notify_time_lim_ms() - таймаут уведомлений
    - set_notify_enable() - вкл./выкл. уведомлений
----------------------------------------------------------------
## class NetworkConfig():
### Команды для работы с Wi-Fi сетью или Ethernet (netinfo, wificonnect, scan)
####    Методы:
    - get_netinfo() - получить инфо о сети
    - set_sta_enable() - вкл./выкл. WiFi STA
    - set_ap_enable() - вкл./выкл. WiFi AP  
    - set_wificonnect() - подключиться к WiFi
    - scan_wifi() - сканирование WiFi
----------------------------------------------------------------
## class SystemCommands():
### Сервисные команды общего назначения
####    Методы:
    - logout() - выход из web-интерфейса
    - get_messagelog() - получить лог сообщений
    - get_version() - получить версию ПО
    - reboot() - перезагрузка устройства
    - beep_device() - звуковой сигнал
    - inventory_once() - однократная инвентаризация
    - set_relay() - управление реле 1
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