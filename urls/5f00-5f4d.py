#5f00-5f4d
from spiders import pages_details
#生成抓取的urls列表
movie_id1 = ["5"]
movie_id2 = ["f"]
movie_id3 = ["0","1","2","3","4"]
movie_id4 = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d"]
movie_ids = []
for a in movie_id1:
    url_id = a
    for b in movie_id2:
        url_id1 = url_id+b
        for c in movie_id3:
            url_id2 = url_id1+c
            for d in movie_id4:
                url_id3 = url_id2+d
                movie_ids.append(url_id3)
movie_ids.reverse()
#开始抓取
for i in movie_ids:
    url = 'https://www.avmoo.com/cn/movie/' + i
    pages_details(url,i)
    print("完成" + i +"页面的抓取")
print("完5f00-5f4d成 5f00-5f4d 的页面抓取")