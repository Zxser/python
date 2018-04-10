# coding=utf-8
#######################################################
# filename:test_xlrd.py
# author:defias
# date:xxxx-xx-xx
# function：读excel文件中的数据
#######################################################
import os, sys, subprocess, time
import re

def main():
    exceptlist = []
    datalines = ''
    i = 0
    j = 0
    k = 0
    daralineshour = [ [ []  for i in range(24) for j in range(60) ] for k in range(500)]
    #print daralineshour[2][0]
    #return
    #for i in range(0, 24):
    #    daralineshour.append('')

    size_in_on_sec = 0

    while True:
        print 'new Round begin!'

        f = open(r'G:\\tmpdata\\333.txt', 'r')
        handle=0
        year, mon, day, hour, min, sec = 0, 0, 0, 0, 0, 0
        yearold, monold, dayold, hourold, minold, secold = 0, 0, 0, 0, 0, 0
        size_in_on_sec = 0
        for line in f.readlines():
            #print line
            if not re.match('2017-.*', line):
                continue

            timestamp, size = line.split(' ')
            #print timestamp, '!!', size

            timeinfo = timestamp.split('xxxxx')

            timeinfoOK = timeinfo[0] + ' ' + timeinfo[1]

            year, mon, day = timeinfoOK.split(' ')[0].split('-')
            hour, min, sec = timeinfoOK.split(' ')[1].split(':')

            if day != '14' or hour != '14':
                continue



            if exceptlist.__len__() > 0 and (year+mon+day+hour+min+sec in exceptlist):
                continue

            #print '----------------'
            #print year, mon, day, handle

            #if day == '15':
                #print year, mon, day
                #print exceptlist

            if yearold != 0:
                if not (yearold == year and monold == mon and  dayold == day and hourold == hour and minold == min and secold == sec ):
                     #print year,mon,day,yearold,monold,dayold
                     continue
                #else:
                    #print year, mon, day, handle
                    #print exceptlist
                    #handle += 1
                    #print day
            #print 'new Round begin ok!! %s ' % yearold
            #print year,mon,day,yearold, monold, dayold
            #print exceptlist

            handle += 1

            yearold, monold, dayold,hourold, minold, secold =  year, mon, day,hour, min, sec
            #print dayinfo,'|||', secinfo
            #year,mon,day,hour,min,sec=timeinfoOK.split(' ')
            datalines += year+'-'+mon+'-'+day+' '+hour+':'+min+':'+ sec + ','+ size

            size_in_on_sec += int(size)

            #if  int(hour) >= 0 and int(hour) <= 24:
                #print int(hour)
                #print a
                #print hour, min
                #daralineshour[int(hour)][int(min)].append(year+'-'+mon+'-'+day+' '+hour+':'+min+':'+ sec + ','+ size);
                #print daralineshour[int(hour)][int(min)]


            #print datalines
            #print datalines.__len__()
            #print year, '|||', mon, '|||', day, '|||', hour, '|||', min, '|||', sec


            #print handle
            #print 'hgi'
        f.close()

        print 'one round end! %s-%s-%s %s:%s:%s ' %( year, mon , day,hour,min,sec)
        print 'Did not search this! %s-%s-%s %s:%s:%s ' %(yearold, monold, dayold,hourold,minold,secold)

        if int(hour) >= 0 and int(hour) <= 24:
            # print int(hour)
            # print a
            # print hour, min
            daralineshour[int(hour)][int(min)].append(
                year + '-' + mon + '-' + day + ' ' + hour + ':' + min + ':' + sec + ',' + str(size_in_on_sec));
            # print daralineshour[int(hour)][int(min)]
            size_in_on_sec = 0

        print handle
        if handle <= 0:
            print 'end searching!'
            for i in range(0 , 24):
                for j in range(0, 60):
                    #print '=================='
                    if daralineshour[i][j].__len__() == 0:
                        continue

                    str_convert = ''.join(daralineshour[i][j])
                    #print i, j
                    #print '?'
                    #print str_convert

                    with open('tiezi.csv', 'ab+') as fout:  # 再次文本方式写入，不含空行
                        fout.write(str_convert)
            break


        if yearold != 0 and (yearold+monold+dayold+hourold+minold+secold not in exceptlist):
            print year
            exceptlist += [yearold+monold+dayold+hourold+minold+secold]

            #print 'now handleed year: ' + year
            #print exceptlist

            #print 'is in list: %d ' % (year+mon+day in exceptlist)

        #break

        #print handle

if __name__ == '__main__': main()


