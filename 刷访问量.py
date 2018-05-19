import webbrowser as web     
import time
import os
import random    
count = random.randint(1,2)    
j=0    
while j<count:    
    i=0    
    while i<=8 :    
        web.open_new_tab('https://mengqingyu.blogspot.com/2018/05/linux.html')  #网址替换这里  
        i=i+1    
        time.sleep(3)  #这个时间根据自己电脑处理速度设置，单位是s
    else:    
        time.sleep(10)
 
        os.system('taskkill /F /IM chrome.exe')  #google浏览器，其他的更换下就行
        #print 'time webbrower closed'  
          
    j=j+1    
