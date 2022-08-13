import configparser
import os
from pathlib import Path

import requests

BASE_DIR = Path(__file__).resolve().parent.parent


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
    print(res.json())

    return res.json()


if __name__ == "__main__":
    get_road_info_api(126.9784039920235, 37.566627074987274)
