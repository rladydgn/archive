import configparser
import os
from pathlib import Path

import requests
from haversine import haversine

BASE_DIR = Path(__file__).resolve().parent.parent


# tmap api call
def get_road_info_api(lon, lat) -> dict:
    config = configparser.ConfigParser(interpolation=None)
    config.read(os.path.join(BASE_DIR, 'config.ini'))

    uri = "https://apis.openapi.sk.com/tmap/road/nearToRoad?version=1"
    data = {
        "appKey": config['API']["TMAP_API_KEY"],
        "lon": lon,
        "lat": lat
    }

    for key, value in data.items():
        uri += "&" + key + "=" + str(value)

    res = requests.get(uri)
    # print(res.json())

    return res.json()


# WSG84 좌표계 좌표를 이용하여 두 좌표 사이의 거리 반환(m)
def get_distance(start_longitude, start_latitude, end_longitude, end_latitude, unit='m') -> float:
    start = (start_latitude, start_longitude)
    end = (end_latitude, end_longitude)

    return haversine(start, end, unit=unit)


def get_latest(data) -> list:
    data_dic = {}
    for d in data:
        if not d['user_id'] in data_dic or (d['user_id'] in data_dic and d['created_at'] > data_dic[d['user_id']]['created_at']):
            data_dic[d['user_id']] = d

    r_data = []
    for value in data_dic.values():
        r_data.append(value)

    return r_data


if __name__ == "__main__":
    print(get_road_info_api(126.9784039920235, 37.566627074987274))
    print(get_distance(126.984739, 37.562707, 126.984333, 37.564495))
    print(get_distance(126.994597, 37.610938, 126.995213, 37.610493))
    print(get_distance(126.994597, 37.610938, 126.999597, 37.610938))

# 126.994597, 37.610938 학교 정문
# 126.995213, 37.610493