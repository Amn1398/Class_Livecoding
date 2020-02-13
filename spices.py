import requests


class Spices:
    def __init__(self, name, url):
        """

        :param name:
        :param url:
        """
        self.name = name
        self.url = url
        self.html = requests.get(self.url).text

