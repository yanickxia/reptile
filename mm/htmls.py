__author__ = 'Yann.Xia'
# coding:utf-8

from bs4 import BeautifulSoup


class Htmls(BeautifulSoup):
    def get_img_tags(self):
        return self.find_all('img')

    def get_img_tag_values(self):
        content_div = self.find(name='div', attrs={'class': "content"})
        tags = content_div.find_all('img')
        imgs = []
        for tag in tags:
            imgs.append(tag.get('src'))
        return imgs

    def get_pages(self):
        page_div = self.find(name='div', attrs={'class': "page"})
        page_tags = page_div.find_all('a')

        pages = []
        for page_tag in page_tags:
            page = page_tag.get('href')
            if page != None and page != '#':
                pages.append(page)
        return pages
