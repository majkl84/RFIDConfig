from SAUKRFIDConfig import RFIDConfig
import pprint

if __name__ == '__main__':
    rfid_config = RFIDConfig("http://192.168.2.245", "admin", "admin")

### Настройка параметров RFID-тракта (rfidconfig)

    # params = rfid_config.get_params()
    # print(params)

    # response = rfid_config.set_continuous_scanning(True)
    # print(response.status_code)

    # response = rfid_config.set_power_antenna(19)
    # if response.status_code == 200:
    #     print("Power antenna was set successfully!")
    # else:
    #     print("Error setting power antenna.")

    # response = rfid_config.set_enable_antenna(True)
    # print(response.status_code)

    # response = rfid_config.set_enable_trigger(True)
    # print(response.status_code)

    # response = rfid_config.set_trigger_state(1)
    # if response.status_code == 200:
    #     print("Trigger state was set successfully!")
    # else:
    #     print("Error setting trigger state.")

    # response = rfid_config.set_antenna_dependency(4)
    # if response.status_code == 200:
    #     print("Antenna dependency was set successfully!")
    # else:
    #     print("Error setting antenna dependency.")

    # response = rfid_config.set_repeattime(2)
    # if response.status_code == 200:
    #     print("Repeattime was set successfully!")
    # else:
    #     print("Error setting repeattime.")

    # response = rfid_config.set_min_hold_ms(5000)
    # if response.status_code == 200:
    #     print("Min hold time was set successfully!")
    # else:
    #     print("Error setting min hold time.")

################################################################

### Настройка параметров периферийных устройств (peripheryconfig)

    # params = rfid_config.get_periphery_params()
    # pprint.pprint(params)

    # response = rfid_config.set_relay1_enable(True)
    # print(response.status_code)

    # response = rfid_config.set_relay1_timer(400)
    # if response.status_code == 200:
    #     print("Relay 1 timer was set successfully!")
    # else:
    #     print("Error setting relay 1 timer.")

################################################################

### Настройка параметров идентификации RFID-меток (tagidentity)

    # params = rfid_config.get_tag_identity_params()
    # pprint.pprint(params)

    # params = rfid_config.set_tag_list()
    # pprint.pprint(params)

    # response = rfid_config.set_valid_time_ms(500)
    # if response.status_code == 200:
    #     print("Valid time was set successfully!")
    # else:
    #     print("Error setting valid time.")

    response = rfid_config.set_hold_time_ms(500)
    if response.status_code == 200:
        print("Hold time was set successfully!")
    else:
        print("Error setting hold time.")
###############################################################