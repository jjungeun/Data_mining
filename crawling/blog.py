import requests
import json
from bs4 import BeautifulSoup
from urllib import parse

class Blog:
    def __init__(self,keyword):
        self.keyword = parse.quote(keyword)
        self.headers = {
            'referer' : 'https://section.blog.naver.com/BlogHome.nhn?directoryNo=0&currentPage=1&groupId=0'
        }
    
    def get_url(self, page):
        urls = []
        url = 'https://section.blog.naver.com/ajax/SearchList.nhn?countPerPage=7&type=post&orderBy=sim&keyword=' + self.keyword + '&currentPage=' + str(page)
        res = requests.get(url,headers=self.headers).text
        
        idx = res.index('{')
        json_res = json.loads(res[idx:])
        for result in json_res['result']['searchList']:
            urls.append(result['postUrl'])
        
        return urls

    def get_content(self, url_ls):
        content_ls = []
        for url in url_ls:
            content = ''
            url_base = 'https://blog.naver.com/PostView.nhn?redirect=Dlog&widgetTypeCall=true&directAccess=false&blogId='
            user = url.split('/',maxsplit=2)[2]
            
            if 'blog.me' in url:
                url_base += user.split('.')[0] + '&logNo=' + user.split('/')[1]
            elif 'co.kr' in url:
                url_base += user.split('.')[1] + '&logNo=' + user.split('/')[1]
            else:
                url_base += user.split('/')[1] + '&logNo=' + user.split('/')[2]
            
            res = requests.get(url_base).text
            soup = BeautifulSoup(res, 'html.parser')
            crawl = soup.select('.se-main-container')

            for line in crawl:
                content += line.text.strip()
                
            content_ls.append(content)
            
        return content_ls

    def crawling_blog(self):
        url_ls = []
        con = []
        for page in range(1,10):
            url_ls = self.get_url(page)
            contents = self.get_content(url_ls)
            for con in contents:
                con = con.replace('\n','')
                con = con.replace('\u200b','')
            break
        print(con)
        return con
