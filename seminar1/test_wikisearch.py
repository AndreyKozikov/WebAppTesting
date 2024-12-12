import requests

S = requests.Session()

def get_sites(lat, long, radius, limit=100):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "geosearch",
        "gscoord": f"{lat}|{long}",
        "gsradius": f"{radius}",
        "gslimit": f"{limit}"
    }

    r= S.get(url, params=params)
    pages = r.json()["query"]["geosearch"]
    sites = [i["title"] for i in pages]
    return sites

def test_step1(test_for_search, coord_for_search):
    assert test_for_search in get_sites(coord_for_search[0], coord_for_search[1], radius=100)

