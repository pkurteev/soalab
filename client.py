import requests


def ping(address):
    req = requests.get(address + "/Ping")
    if req.status_code != 200:
        ping(address)


if __name__ == '__main__':
    port = input()
    address = 'http://127.0.0.1:{}/'.format(port)
    ping(address)
    r = requests.post(address + "/PostInputData", json={"K": 10, "Sums": [1.01, 2.02], "Muls": [1, 4]})
    r = requests.get(address + "/GetAnswer")
    print(r.content.decode('utf-8'))
    r = requests.get(address + "/Stop")
