from SAUKRFIDConfig import RFIDConfig

if __name__ == '__main__':
    rfid_config = RFIDConfig("http://192.168.2.245", "admin", "admin")
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

    response = rfid_config.set_min_hold_ms(5000)
    if response.status_code == 200:
        print("Min hold time was set successfully!")
    else:
        print("Error setting min hold time.")