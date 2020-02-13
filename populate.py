import requests

from spices import Spices


def combine_crap(piece1=1, piece2=2):
    return piece1 + piece2


if __name__ == '__main__':
    results = requests.get("http://github.com")
    # print(results.text)
    # print(combine_crap(5))
    # print(combine_crap(piece2=5))
    lao_gan_ma = Spices(name="Lao Gan Ma", url="https://en.wikipedia.org/wiki/Lao_Gan_Ma")
    print(lao_gan_ma.html)
