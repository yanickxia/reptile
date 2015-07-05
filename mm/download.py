__author__ = 'Yann.Xia'

import urllib.request
from mm.paths import Paths


class Download:
    @staticmethod
    def download(url, download_location):
        Paths.create_paths(download_location)
        file = open(download_location, 'wb')

        conn = urllib.request.urlopen(url)
        file.write(conn.read())
        file.close()

        print("save pic location:", download_location)

    @staticmethod
    def download_html(url):
        conn = urllib.request.urlopen(url)
        html = conn.read()

        return html


