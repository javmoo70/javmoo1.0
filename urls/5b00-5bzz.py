#5b00-5bzz
from spiders import pages_details
#生成抓取的urls列表
movie_id1 = ["5"]
movie_id2 = ["b"]
movie_id3 = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
movie_id4 = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
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
'''
#正常抓取流程
movie_ids.reverse()
#开始抓取
for i in movie_ids:
    url = 'https://www.avmoo.com/cn/movie/' + i
    pages_details(url,i)
    print("完成" + i +"页面的抓取")
print("完成 5a00-5azz 的页面抓取")
'''
#发生错误时的抓取流程,需要纪录抓取失败的id
a = movie_ids.index('5b7x') + 1
not_done = movie_ids[0:a]
not_done.reverse()
#开始抓取
for i in not_done:
    url = 'https://www.avmoo.com/cn/movie/' + i
    pages_details(url,i)
    print("完成" + i +"页面的抓取")
print("完成 5b00-5bzz 的页面抓取")