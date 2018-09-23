#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:xiaoer
@file: demo1.py
@time: 2018/05/{DAY} 
"""

import requests
import re


url = 'https://www.pixiv.net/ranking.php?mode=daily&date=20180507'
headers = {
"referer": "https://www.pixiv.net/ranking.php?mode=daily",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36",
"cookie": "p_ab_id=9; p_ab_id_2=1; __utmz=235335808.1525444436.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.2.64704079.1525444436; PHPSESSID=31500452_d5d2d5b5a8430c07418f4b7f78d0d40c; device_token=4be5577d2414260c9e9c4590ca63ba95; c_type=27; a_type=0; b_type=0; yuid=JJRRiFg59; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^6=user_id=31500452=1^9=p_ab_id=9=1^10=p_ab_id_2=1=1^11=lang=zh=1; __gads=ID=ef4653f7bfe7fc55:T=1525444550:S=ALNI_Ma-VTViG7NHMD1ncI2piLNEL22vrw; module_orders_mypage=%5B%7B%22name%22%3A%22sketch_live%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22tag_follow%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22recommended_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22showcase%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22everyone_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22following_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22mypixiv_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22fanbox%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22featured_tags%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22contests%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22user_events%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22sensei_courses%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22spotlight%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22booth_follow_items%22%2C%22visible%22%3Atrue%7D%5D; is_sensei_service_user=1; _gid=GA1.2.831802687.1525860940; tag_view_ranking=RTJMXD26Ak~Lt-oEicbBr~jH0uD88V6F~pYlUxeIoeg~EyEzlEct2T~NKIsEMOZT5~RKWhQt3bKa~hqvRfnHHng~0xsDLqCEW6~BU9SQkS-zU~y8GNntYHsi~q3eUobDMJW~azESOjmQSV~xZ6jtQjaj9~qtVr8SCFs5~i83OPEGrYw~E8plmQ7kUK~c-0HyG_fc2~tjt51FqN-e~hoNJK4MaxF~vFwTRLUjL6~KN7uxuR89w~5oPIfUbtd6~ETjPkL0e6r~CM9TZgYuXr~O1XEXHhhhH~Nbvc4l7O_x~iFcW6hPGPU~mf6rICH32i~zcefxGBLt4~gooMLQqB9a~EA_MGmsO22~1m8UkUR-IC~GF09UjQt_e~EPc4x89KH8~omY3sW9fty~zIv0cf5VVk~QjJSYNhDSl~6zSsU6XX8w~4i9bTBXFoE~LYjENeTkAP~AlDva0XKC6~mFuvKdN_Mu~Q959js6mBM~IfTHG7cZ8v~-L-4bBqjrT~EUwzYuPRbU~0CaTbfGZYk~_pwIgrV8TB~aKhT3n4RHZ~tIqkVZurKP~fn5nUXtjWI~tgP8r-gOe_~8PDkVxzRxX~5-q4dVSeQE~nhVUm2hb1U~UnhDA4LpTp~W8BvWADUFc~ujS7cIBGO-~EnPQyCHByh~WxVAdUQMC-~lcx4SAv5ay~MDevotg5Bf~9Yweb9F-fM~HozvRNsVHD~-oGijJmC5S~l_eZOB0M5F~nrFOQYIh7z~OnPXVFB0OB~7cMRrOPRjW~Ms9Iyj7TRt~X3PHa6Y9t-~nRnn8VBmkN~qvqXJkzT2e~FH69TLSzdM~c31hh0VKmG~jgzicyOO_X~y0n5HRQOaX~dXCQWULiD0~nxqUUUA3Yu~rezgCfkPbs~3HuvlQ0z6q~o5DB__cIwt~0Sds1vVNKR~LtW-gO6CmS~DotUVrfi2a~jjVAJCBCtW~xSkR4pVgag~_RfiUqtsxe~mlU259gK3R~Xl27wktZcU~HM_o2vRZZM~Lhz5zfSWz8~EFlgudz1Z4~aUKGRzPd6e~8BYGt5epl5~EGefOqA6KB~D5-rma_A2j~5f1R8PG9ra~oKNe5SNEWp; __utma=235335808.64704079.1525444436.1525872531.1525911825.13; __utmc=235335808; __utmt=1; _gat_UA-1830249-138=1; __utmb=235335808.11.10.1525911825"
}

r = requests.get(url,headers=headers)

rap = r"[a-zA-z]+://[^\s]*.jpg"
r = re.compile(rap).findall(r.text)

rap1 = "(6[0-9]{7})"
num = re.compile(rap1).findall(str(r))
print(len(num))