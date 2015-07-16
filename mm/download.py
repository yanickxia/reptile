__author__ = 'Yann.Xia'

import urllib.request
from mm.paths import Paths


class Download:
    @staticmethod
    def download(url, download_location):
        Paths.create_paths(download_location)
        file = open(download_location, 'wb')

        conn = Download.loop_connection(url)
        file.write(conn.read())
        file.close()

        print("save pic location:", download_location)

    @staticmethod
    def download_html(url):

        conn = Download.loop_connection(url)

        return conn.read()

    @staticmethod
    def loop_connection(url):
        while True:
            try:
                conn = urllib.request.urlopen(url)
                break
            except:
                print("Try Connection url: ", url)
        return conn
