from SAUKRFIDConfig import RFIDConfig

if __name__ == '__main__':
    rfid_config = RFIDConfig("http://192.168.2.245", "admin", "admin")
    # params = rfid_config.get_params()
    # print(params)

    # response = rfid_config.set_continuous_scanning(True)
    # print(response.status_code)

    response = rfid_config.set_power_antenna(19)
    if response.status_code == 200:
        print("Power antenna was set successfully!")
    else:
        print("Error setting power antenna.")