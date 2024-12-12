import requests
import yaml

with open("config.yaml", 'r') as stream:
    config = yaml.safe_load(stream)
    username = config['username']
    password = config['password']
    url = config['url']

class TestStandGbRu():

    # Провека наличия поста в ленте постов другого пользователя
    def test_post_header_check(self, api_session, seacrh_post_by_title):
        param = {
            "owner" : "notMe"
        }
        response = api_session.get("https://test-stand.gb.ru/api/posts", params=param)
        posts = response.json()["data"]
        titles = [post["title"] for post in posts]
        assert seacrh_post_by_title in titles

    # Тест проверки по полю description наличия поста в ленте своих постов после его создания
    def test_create_post(self, api_session, create_post):
        response = api_session.get("https://test-stand.gb.ru/api/posts")
        if response.status_code != 200:
            raise Exception(f"Failed to fetch posts: {response.status_code} - {response.text}")
        posts = response.json()["data"]
        titles = [post["title"] for post in posts]
        assert  create_post in titles




