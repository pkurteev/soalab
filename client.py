from serializer import parse_json
import requests


def ping(address):
    req = requests.get(address + "/Ping")
    if req.status_code != 200:
        ping(address)


if __name__ == '__main__':
    port = input()
    address = 'http://127.0.0.1:{}/'.format(port)
    ping(address)
    data = requests.get(address + "/GetInputData").json()
    answer = parse_json(data)
    r = requests.post(address + '/WriteAnswer', json=answer)
