__author__ = 'Yann.Xia'

from mm.download import Download
from mm.htmls import Htmls
import threading

down_path = 'D://reptile_download/'

a_page = 'http://mm.ked9.com/siwameitui/201506/320.html'


# get all list
def get_list_of_site(index_page):
    html = Htmls(Download.download_html(index_page), 'html.parser')
    page_list = html.get_list()

    page_list = [index_page + i for i in page_list]

    return page_list


# get detail pic of a list
def get_detail_pages_from_list(page_list):
    html = Htmls(Download.download_html(page_list), 'html.parser')
    items = html.get_items()

    return items


# get pages of a detail page
def get_pages_of_a_html(base_url):
    html = Download.download_html(base_url)
    html = Htmls(html, 'html.parser')

    base_urls = base_url.split('/')
    pages = html.get_pages()
    pages.insert(0, base_urls[-1])
    base_url = base_url.replace(base_urls[-1], '')
    for i in range(0, len(pages)):
        pages[i] = base_url + pages[i]

    return pages


# function down
def down_page_img(page):
    html_url = page
    html = Download.download_html(html_url)
    html = Htmls(html, 'html.parser')
    imgs = html.get_img_tag_values()

    for img in imgs:
        file_names = str(img).split('/')
        current_path = down_path + file_names[-2] + '/' + file_names[-1]

        if 'http' in img and 'jpg' in img:
            print("download pic: ", file_names[-1])
            Download.download(img, current_path)


# main logic

index_page = 'http://mm.ked9.com/siwameitui/'
# get all list
page_lists = get_list_of_site(index_page)

# loop page_list
for page_list in page_lists:
    page_items = get_detail_pages_from_list(page_list)

    for page_item in page_items:
        # get_current_page
        pages = get_pages_of_a_html(page_item)

        # add muitl threads
        threads = []

        for page in pages:
            thread = threading.Thread(target=down_page_img, args={page})
            threads.append(thread)
            thread.setDaemon(True)
            thread.start()

        for thread in threads:
            thread.join(60000)
