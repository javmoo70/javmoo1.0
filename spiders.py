from bs4 import BeautifulSoup
import requests
import time
import pymongo

def pages_details(url,i,data=None):
    header = {'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}
    wb_data = requests.get(url,header)
    print(wb_data)
    time.sleep(3)
    if str(wb_data) =='<Response [200]>':
        Soup = BeautifulSoup(wb_data.text,'lxml')
        #av标题
        titles = Soup.select('body > div.container > h3')
        #av封面图
        images = Soup.select('body > div.container > div.row.movie > div.col-md-9.screencap > a > img')
        #av番号
        movie_ids = Soup.select('body > div.container > div.row.movie > div.col-md-3.info > p:nth-of-type(1) > span:nth-of-type(2)')
        #av的系列
        series = Soup.select('body > div.container > div.row.movie > div.col-md-3.info > p:nth-of-type(10) > a')
        #av类别 - 多内容
        genres = Soup.select('body > div.container > div.row.movie > div.col-md-3.info > p > span > a')
        #av演员 - 多内容
        players = Soup.select('#avatar-waterfall > a > span')
        #av播放截图 - 多内容
        simples = Soup.select('#sample-waterfall > a > div > img')
        #av发布时间
        release_dates = Soup.select('body > div.container > div.row.movie > div.col-md-3.info > p:nth-of-type(2)')

        Series = []
        Genre = []
        Player =[]
        Simple =[]
        for serie in series:
            Series.append(serie.get_text())
        for genre in genres:
            Genre.append(genre.get_text())
        for player in players:
            Player.append(player.get_text())
        for simple in simples:
            Simple.append(simple.get('src'))
        for Time in release_dates:
            movie_Time = Time.get_text()
        movie_time = movie_Time[-10:]

        if len(Series)==0:
            Series.append('None')

        if len(Genre)==0:
            Genre.append('None')

        if len(Player)==0:
            Player.append('None')

        if len(Simple)==0:
            Simple.append('None')

        client = pymongo.MongoClient('112.124.17.223',27017)
        javmoo = client['web']
        sheet_line = javmoo['movie_details']
        if data == None:
            for title,image,movie_id in zip(titles,images,movie_ids):
                    data = {
                        'avid':i,
                        'movie_title':title.get_text(),
                        'movie_image':image.get('src'),
                        'movie_id':movie_id.get_text(),
                        'series':Series,
                        'genre':Genre,
                        'player':Player,
                        'simple_image':Simple,
                        "time":movie_time
                    }
            print(data)
            sheet_line.insert_one(data)
    else:
        print(i + '抓取失败')

