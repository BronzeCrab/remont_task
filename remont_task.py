import requests as rq
import json
from math import sin, cos, sqrt, atan2, radians

PARIS_LONG = 2.350987
PARIS_LAT = 48.856667
DISTANCE_FROM_PARIS_KM = 450
API_URL = "https://opensky-network.org/api/states/all"


def calc_distance(lat1, lon1, lat2, lon2):
    """
    https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude#answer-19412565
    """
    # approximate radius of earth in km
    R = 6371.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)

    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


def get_all_planes():
    resp = rq.get(API_URL)
    if resp.status_code == 200:
        try:
            resp = json.loads(resp.text)
            return resp['states']
        except Exception as e:
            return 'Error: {0}'.format(e)
    else:
        return 'Error with api'


def main():
    planes = get_all_planes()
    if type(planes) is list:
        return [plane for plane in planes if len(plane) >= 7 and
                type(plane[6]) is float and type(plane[5]) if float and
                calc_distance(PARIS_LAT, PARIS_LONG, plane[6], plane[5]) <=
                DISTANCE_FROM_PARIS_KM]
    return planes


if __name__ == '__main__':
    main()
