import requests
from common import bs4_decorator
from constant import *


class Requester:
    """Base class of requests maker like lawman and crawler 
       Provided With Simple request function and bs decorator 
    """

    def __init__(self, tieba_name="steam", cookie=None):
        if cookie is None:
            raise Exception("Cookie must be provided")

        self.session_worker = requests.Session()
        self.cookie = cookie
        self.tieba_base = TIEBA_MOBILE_BASE_URL.format(tieba_name=tieba_name)
        self.url_base = TIEBA_URL

    @bs4_decorator
    def get_content(self, url):
        """
        Get content of url with cookie
        :param url:
        :return:
        """
        return self.session_worker.get(url, cookies=self.cookie)
