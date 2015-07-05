__author__ = 'Yann.Xia'

from mm.download import Download
from mm.htmls import Htmls
import threading

base_path = 'F://reptile_download/'

base_url = 'http://mm.ked9.com/siwameitui/201506/320.html'

html = Download.download_html(base_url)
html = Htmls(html, 'html.parser')

base_urls = base_url.split('/')
pages = html.get_pages()
pages.insert(0, base_urls[-1])
base_url = base_url.replace(base_urls[-1], '')

# add muitl threads
threads = []


# function down
def down_page_img(page):
    html_url = base_url + page
    html = Download.download_html(html_url)
    html = Htmls(html, 'html.parser')
    imgs = html.get_img_tag_values()

    for img in imgs:
        file_names = str(img).split('/')
        down_path = base_path + file_names[-2] + '/' + file_names[-1]

        if 'http' in img and 'jpg' in img:
            print("download pic: ", file_names[-1])
            Download.download(img, down_path)


for page in pages:
    thread = threading.Thread(target=down_page_img, args={page})
    threads.append(thread)
    thread.setDaemon(True)
    thread.start()

for thread in threads:
    thread.join(60000)
