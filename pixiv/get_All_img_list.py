#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:xiaoer
@file: get_All_img_list.py
@time: 2018/05/{DAY} 
"""


import urls_manager
import return_indexes
import re
import requests


def get_All_img_list():
    """
        用来获取所有图片的JPG格式URL
    """
    headers = {
        "cookie": "p_ab_id=9; p_ab_id_2=1; __utmz=235335808.1525444436.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.2.64704079.1525444436; PHPSESSID=31500452_d5d2d5b5a8430c07418f4b7f78d0d40c; device_token=4be5577d2414260c9e9c4590ca63ba95; c_type=27; a_type=0; b_type=0; yuid=JJRRiFg59; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^6=user_id=31500452=1^9=p_ab_id=9=1^10=p_ab_id_2=1=1^11=lang=zh=1; __gads=ID=ef4653f7bfe7fc55:T=1525444550:S=ALNI_Ma-VTViG7NHMD1ncI2piLNEL22vrw; module_orders_mypage=%5B%7B%22name%22%3A%22sketch_live%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22tag_follow%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22recommended_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22showcase%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22everyone_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22following_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22mypixiv_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22fanbox%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22featured_tags%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22contests%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22user_events%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22sensei_courses%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22spotlight%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22booth_follow_items%22%2C%22visible%22%3Atrue%7D%5D; is_sensei_service_user=1; _gid=GA1.2.831802687.1525860940; __utma=235335808.64704079.1525444436.1525911825.1525920275.14; __utmc=235335808; __utmt=1; tag_view_ranking=RTJMXD26Ak~Lt-oEicbBr~jH0uD88V6F~pYlUxeIoeg~EyEzlEct2T~NKIsEMOZT5~RKWhQt3bKa~hqvRfnHHng~0xsDLqCEW6~BU9SQkS-zU~y8GNntYHsi~q3eUobDMJW~ETjPkL0e6r~qtVr8SCFs5~azESOjmQSV~xZ6jtQjaj9~nxqUUUA3Yu~KN7uxuR89w~LYjENeTkAP~i83OPEGrYw~9Yweb9F-fM~HozvRNsVHD~vFwTRLUjL6~E8plmQ7kUK~c-0HyG_fc2~EnPQyCHByh~tjt51FqN-e~MDevotg5Bf~hoNJK4MaxF~lcx4SAv5ay~X3PHa6Y9t-~5oPIfUbtd6~mf6rICH32i~zcefxGBLt4~CM9TZgYuXr~O1XEXHhhhH~iFcW6hPGPU~Nbvc4l7O_x~1m8UkUR-IC~EPc4x89KH8~omY3sW9fty~zIv0cf5VVk~QjJSYNhDSl~6zSsU6XX8w~4i9bTBXFoE~GF09UjQt_e~gooMLQqB9a~EA_MGmsO22~AlDva0XKC6~_pwIgrV8TB~0CaTbfGZYk~fn5nUXtjWI~tgP8r-gOe_~8PDkVxzRxX~5-q4dVSeQE~nhVUm2hb1U~rezgCfkPbs~W8BvWADUFc~ujS7cIBGO-~-L-4bBqjrT~tIqkVZurKP~mFuvKdN_Mu~EUwzYuPRbU~WxVAdUQMC-~aKhT3n4RHZ~-oGijJmC5S~l_eZOB0M5F~nrFOQYIh7z~OnPXVFB0OB~7cMRrOPRjW~Ms9Iyj7TRt~Q959js6mBM~nRnn8VBmkN~qvqXJkzT2e~FH69TLSzdM~c31hh0VKmG~jgzicyOO_X~y0n5HRQOaX~dXCQWULiD0~IfTHG7cZ8v~UnhDA4LpTp~3HuvlQ0z6q~o5DB__cIwt~0Sds1vVNKR~LtW-gO6CmS~DotUVrfi2a~jjVAJCBCtW~xSkR4pVgag~_RfiUqtsxe~2GVngxkxTb~mlU259gK3R~HM_o2vRZZM~Xl27wktZcU~Lhz5zfSWz8~aUKGRzPd6e~EFlgudz1Z4~EGefOqA6KB~8BYGt5epl5~5f1R8PG9ra~oKNe5SNEWp; __utmb=235335808.3.10.1525920275",
        "referer": "https://www.pixiv.net/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
        }
    All_img_list = []
    old_All_img_list = []
    urls, id_list = urls_manager.urls_manager()

    for i in range(len(urls)):
        url = urls[i]
        r = requests.get(url,headers=headers)
        r = r.text
        rap = r"[a-zA-z]+://[^\s]*.jpg"
        r = re.compile(rap).findall(r)
        img_url = []
        for j in range(len(r)):
            if id_list[i] in r[j]:
                img_url.append(r[j])
            if len(img_url)<3:
                pass
            else:
                x = return_indexes.return_indexes(img_url)
                old_All_img_list.append(img_url[x])
            print('已获取img_url')
    for x in old_All_img_list:
        if x not in All_img_list:
            All_img_list.append(x)
    return All_img_list,id_list
    # print (All_img_list)














