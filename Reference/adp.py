from ppadb.client import Client as AdbClient
import time

if __name__ == '__main__':
    client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037

    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]

    print(f'Connected to {device}')
    paytm = '340 1041' # x y
    device.shell(f'input tap {paytm}')
    time.sleep(5)
    upi= '425 1220'
    device.shell(f'input tap {upi}')
    time.sleep(5)
    upi_id='harishjonsena'
    device.shell(f'input text "{upi_id}"')

