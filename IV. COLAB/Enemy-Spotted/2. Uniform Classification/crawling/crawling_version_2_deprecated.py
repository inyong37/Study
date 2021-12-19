from urllib.request import urlopen
import argparse
import requests as req
from bs4 import BeautifulSoup
# reference: https://enjoysomething.tistory.com/42

parser = argparse.ArgumentParser()
parser.add_argument("-data", required=False, default='acu pattern')
args = parser.parse_args()

data = args.data


def main():
    url_info = "https://www.google.com/search?"
    params = {
        "q": data
    }

    html_object = req.get(url_info, params)
    if html_object.status_code == 200:
        bs_object = BeautifulSoup(html_object.text, "html.parser")
        img_data = bs_object.find_all("img")
        for i in enumerate(img_data[1:]):
            t = urlopen(i[1].attrs['src']).read()
            filename = "img_" + str(i[0] + 1) + '.jpg'
            with open(filename, "wb") as f:
                f.write(t)
                print("Image Save Success")


if __name__ == "__main__":
    main()
