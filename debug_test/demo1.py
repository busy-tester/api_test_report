import requests

def req():

    url = "https://lb-api.apps.cluster.5th.im/message/get_msg_overview"

    headers = {
        "x-test-case":"134f08ad5b9b40c2af4324d2767fde35",
        "x-api-key":"54b99190163e0f39e23b6707a89c80fb",
        "x-api-signature":"6778",
        "Content-Type":"application/json",
        "x-noauth":"true"
    }

    data = {
        "mobile": "17693638363",
        "country_code": 86,
        "type": "set_password",
        "captcha": {
            "geetest": {
                "id_type": 2,
                "id_value": "d6d8c2f93de7c5b6564b3bc74ad4e550",
                "challenge": "6b8e020eb28a8edbebf62a9f9577c796"
                }
            }
        }
    res = requests.post(url=url, json=data, headers=headers)
    r = requests.post(url=url, json=data, headers=headers).json()
    # r ＝ res.json()
    # res=requests.post(url=url, data=data, headers=headers).text
    return res.status_code

print(req())

# print(type(str(req()[0])),str(req()[0]))
# a=str(req()[0])
