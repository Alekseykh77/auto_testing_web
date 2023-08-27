import requests

import yaml

with open("config2.yaml") as f:
    info = yaml.safe_load(f)


def token_auth(token):
    res = requests.get(url=info["url2"], headers={"X-Auth-Token": token}, params={"owner": "notMe"})
    content_var = [item["content"] for item in res.json()['data']]
    return content_var


def test_step2(get_token):
    assert 'Люди заводят собак, а кошки людей. Видно, считают их полезными домашними животными. Кошки очень симпатичные и грациозные животные. Поэтому они популярные и любимые домашние питомцы. Именно с любовью к пушистым и лысым, длиннохвостым и вислоухим, черным, белым, полосатым и пятнистым мы подготовили цитаты и статусы про котов. Кошка — крошечный лев, который любит мышей, ненавидит собак и покровительствует человеку. Я изучил многих философов и многих кошек. Мудрость кошек неизмеримо выше.' in token_auth(
        get_token), "test_step2 FAIL"

def test_step3(get_description):
    assert info["description"] in get_description, "test_step3 FAIL"
