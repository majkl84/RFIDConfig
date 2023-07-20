# SAUK-RFIDConfig

## Настройка параметров RFID-тракт (rfidconfig)

### Библиотека `RFIDConfig` позволяет настраивать параметры RFID через API.

#### Пример использования:

    rfid = RFIDConfig("http://example.com")
    params = rfid.get_params()
    rfid.set_infinite_inventory("true")
    rfid.set_power_antenna("10")
    rfid.set_enable_antenna("true")
    rfid.set_enable_trigger("false")
    rfid.set_trigger_state("off")
    rfid.set_antenna_dependency("2")
    rfid.set_repeattime("50")
    rfid.set_min_hold_ms("10000")
    

##### Атрибуты:
        base_url (str): Базовый URL для API.

##### Методы:
        get_params(): Получает все параметры RFID через API.
            Возвращает:
                dict: Словарь с параметрами.
        
        set_infinite_inventory(value: str): Включает или выключает процесс сканирования RFID-меток.
            Аргументы:
                value (str): Значение (например, "true" или "false").
            Возвращает:
                requests.Response: Ответ от сервера.
        
        set_power_antenna(value: str): Изменяет значение RF-мощности, передаваемой на антенну.
            Аргументы:
                value (str): Значение (например, "10").
            Возвращает:
                requests.Response: Ответ от сервера.
        
        set_enable_antenna(value: str): Включает или отключает RFID-антенну.
            Аргументы:
                value (str): Значение (например, "true" или "false").
            Возвращает:
                requests.Response: Ответ от сервера.
        
        set_enable_trigger(value: str): Включает или отключает триггер (цифровой порт hold).
            Аргументы:
                value (str): Значение (например, "true" или "false").
            Возвращает:
                requests.Response: Ответ от сервера.
        
        set_trigger_state(value: str): Активирует или деактивирует зависимость RFID-антенны от сигнала на цифровых портах.
            Аргументы:
                value (str): Значение (например, "on" или "off").
            Возвращает:
                requests.Response: Ответ от сервера.
        
        set_antenna_dependency(value: str): Изменяет активацию и деактивацию зависимости RFID-антенны от сигнала на цифровых портах.
            Аргументы:
                value (str): Значение (например, "2").
            Возвращает:
                requests.Response: Ответ от сервера.
        
        set_repeattime(value: str): Изменяет период повторения опроса RFID-меток.
            Аргументы:
                value (str): Значение (например, "50").
            Возвращает:
                requests.Response: Ответ от сервера.
        
        set_min_hold_ms(value: str): Изменяет минимальную продолжительность времени, в течение которой RFID-метка должна находиться в зоне чтения, чтобы она была считана.
            Аргументы:
                value (str): Значение (например, "10000").
            Возвращает:
                requests.Response: Ответ от сервера.
    """
    def __init__(self, base_url):
        self.base_url = base_url

    # Методы здесь...