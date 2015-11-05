#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from dbconn import SqlConn
from pprint import pprint
from bs4 import BeautifulSoup, NavigableString, SoupStrainer
import urllib2
import urllib
from sets import Set
import sys
import codecs
import re
import os.path
import pickle

#export VERSIONER_PYTHON_PREFER_32_BIT=no
#export VERSIONER_PYTHON_PREFER_64_BIT=yes

Set2650 = Set([u'普通米',u'优质米',u'糯米',u'特一粉',u'特二粉',u'面条']);
Set2651 = Set([u'菜籽油',u'板油',u'色拉油',u'大豆油']);
Set2652=Set([u'猪腿肉',u'猪夹心',u'精瘦肉',u'大排',u'小排',u'肋条',u'草鸡',u'三黄鸡',u'白条鸡',
u'老鸭',u'牛肉',u'白条鸭',u'羊肉']);
Set2653 = Set([u'鸡蛋',u'鸭蛋']);
Set2654=Set([u'鲫鱼',u'鳊鱼' ,u'白鲢' ,u'花鲢',u'草鱼',u'黑鱼',u'鲈鱼',u'鲳鱼',u'鲜带鱼',u'小黄鱼',u'黄鳝',u'基围虾',u'河蟹',u'龙虾',u'河虾',u'大头虾',u'甲鱼']);
Set2655=Set([u'绿豆芽',u'黄豆芽',u'鲜香菇',u'鲜蘑菇',u'大白菜',u'小白菜',u'青菜',u'包菜',u'白萝卜',u'胡萝卜',u'西芹',u'圆青椒',u'长青椒',u'尖椒',u'花菜',u'西兰花',u'生菜',u'大蒜头',u'南瓜',u'茄子',u'土豆',u'西红柿',u'黄瓜',u'冬瓜',u'洋葱',u'韭芽',u'生姜',u'鸡毛菜',u'娃娃菜',u'杭白菜',u'空心菜',u'苋菜',u'水芹',u'毛豆',u'蚕豆',u'茭白',u'四季豆',u'莴笋',u'丝瓜',u'韭菜',u'大蒜叶',u'菠菜',u'西葫芦',u'蒜苗',u'红薯',u'韭花',u'莲藕',u'草头',u'蓬蒿',u'芋艿',u'春笋',u'冬笋',u'山药',u'云豆',u'扁豆',u'苦瓜',u'紫角叶',u'菜苋',u'金针菇',u'草菇',u'塔菜']);
Set2656=Set([u'苹果',u'桔子',u'梨',u'香蕉',u'西瓜',u'哈密瓜']);
Set2657 = Set([u'豆腐',u'百叶',u'素鸡',u'豆腐干',u'白砂糖',u'绿豆',u'黄豆',u'赤豆',u'花生米']);
SetsAll = Set2650 | Set2656 | Set2655 | Set2654 | Set2653 | Set2652 | Set2651 | Set2657

sfmap = {u'普通米':2601, u'优质米':2602, u'糯米':2603, u'特一粉':2604, u'特二粉':2605, \
    u'面条':2606, u'菜籽油':2607, u'色拉油':2608, u'大豆油':2609, u'精瘦肉':2610, \
    u'小排':2611, u'板油':2612, u'草鸡':2613, u'老鸭':2614, u'牛肉':2615, u'鸡蛋':2616, \
    u'鸭蛋':2617, u'草鱼':2618, u'黑鱼':2619, u'鲜带鱼':2620, u'基围虾':2621, u'黄豆芽':2622, \
    u'鲜蘑菇':2623, u'苹果':2624, u'梨':2625, u'桔子':2626, u'香蕉':2627, u'小白菜':2628, \
    u'包菜':2629, u'胡萝卜':2630, u'土豆':2631, u'生姜':2632, u'丝瓜':2633, u'河蟹':2634, \
    u'龙虾':2635, u'草菇':2636 };

length = len(SetsAll);

def strip_tags(soup, invalid_tags):

    for tag in soup.findAll(True):
        if tag.name in invalid_tags:
            s = ""

            for c in tag.contents:
                if not isinstance(c, NavigableString):
                    c = strip_tags(unicode(c), invalid_tags)
                s += unicode(c)

            tag.replaceWith(s)

    return soup

def local(str_):

    f = open(str_)
    beautifulsoupDemo(f.read());
def internet(str_):
    beautifulsoupDemo(urllib2.urlopen(str_));

def getLatestID(link):
    soup = BeautifulSoup(urllib2.urlopen(link));
    print soup.original_encoding
    linksToNews=soup.find_all("a",text = re.compile("太仓市农副产品市场价格".decode("utf8")))
    latestLink = linksToNews[0]['href'];
    latest_id = re.findall(r'\d+',latestLink)[1];
    return latest_id;

def beautifulsoupDemo(content):
    soup = BeautifulSoup(content);
    table_name = soup.find_all('td',class_="newsimg_cn")[1].string;
    #table_name = "12月02日太仓市农副产品市场价格"
    #print table_name;

    time_str = soup.find_all('td',class_="xl70")[0].renderContents();
    #print time_str
    timeExcel = re.findall(r'\d+',time_str);
    #print timeExcel;
    month = timeExcel[1]
    day = timeExcel[2]
    year = timeExcel[0]
    # p_s = soup.find_all('p')[16:1818];
    # # 0 - 1802 1803/16
    # i = 0;
    # print p_s[0].string;
    # print(p_s[0].string.decode('gb2312')==u'普通米'.strip())
    # while(i<1803):
    #     print p_s[i],p_s[i+1];
    #     i = i+15;
    contents = u""
    sqls = [];
    table_all = soup.find_all('table')
    print len(table_all)
    if(len(table_all) >= 6):
        table = table_all[5]
        rows = table.findAll('tr')[3:-1];
        count = 0;
        for row in rows:
            p_s = row.find('p');
            sentence = u''.join(p_s.get_text().split())
            #sentence = unicode(sentence);
            if  sentence in SetsAll:
                data = [];
                count = count +1;
                if sentence in Set2650:
                    data.append("2650");
                elif sentence in Set2651:
                    data.append("2651");
                elif sentence in Set2652:
                    data.append("2652");
                elif sentence in Set2653:
                    data.append("2653");
                elif sentence in Set2654:
                    data.append("2654");
                elif sentence in Set2655:
                    data.append("2655");
                elif sentence in Set2656:
                    data.append("2656");
                elif sentence in Set2657:
                    data.append("2657");
                else:
                	print "non in set"
                #print sentence;
                data.append(sentence);
                data.append(p_s.find_next('p').string[0:-1]);
                #name = (data[1]).encode('utf-8', 'replace')
                print 'generate sql'
      
                this_sql = "INSERT INTO `SUBSIDIARYFOODPRICEDATA`(`YEAR`,`SUBSIDIARYFOODNAME`,`MONTH`,`DAY`,`PRICE`,`subsidiary_food_type`)VALUES("+year + ",'" + sentence+ "'," + month+","+day+","+data[2]+","+data[0]+");";
               
                sqls.append(this_sql);
                contents = contents + str(day) + u'\t' + str(month) + u'\t' + u'\t'.join(data) + u'\t' + str(year)  + u'\n'
        strFile='./dataTC/DailyPrice_'+year+'_'+month+'_'+day+'.csv'
        f = codecs.open(strFile,'a','utf-8')
        f.write(contents)
        f.close()
        print "start connect to sql"
        sqlconn = SqlConn()
        print "start batch insert"
        sqlconn.batchInsert(sqls)
        print "close connection"
        sqlconn.closeConn();
        if(count != length):
            #print table_name + " td error"
            return;
        


if __name__ == "__main__":
    index = "http://www.tcprice.gov.cn/newscenter.asp?PageNo=1&leixing=%C5%A9%B8%B1%B2%FA%C6%B7%BC%DB%B8%F1";
    print index;
    latest_id = getLatestID(index);
    print latest_id;
    # if os.path.exists('./data.pkl'):
    #     output = open('./data.pkl','r')
    #     id = pickle.load(output)
    #     output.close;
    # else:
    id = 848;
    #print "\xe6\x99\xae\xe9\x80\x9a\xe7\xb1\xb3"
    #print "中文"
    while(id<=int(latest_id)):#756
        try:
            link = "http://www.tcprice.gov.cn/news1.asp?id=" + str(id);
            print "start :",link
            internet(link);
            output = open('./data.pkl','w+');
            pickle.dump(id,output)
            output.close
            #beautifulsoupDemo(link);
        except IndexError:
            print 'IndexError'
            indexErrorFile='./dataTC/indexErrorFile.txt'
            f = codecs.open(indexErrorFile,'a','utf-8')
            f.write(link + ' not exists: indexerror')
            f.close()
        except AttributeError,e:
            print e
            print 'AttrError'
            attributeErrorFile='./dataTC/attributeErrorFile.txt'
            f = codecs.open(attributeErrorFile,'a','utf-8')
            f.write(link + ' not exists: attributeerror')
            f.close()
        except UnicodeEncodeError,e:
            print e
            print 'UnicodeError'
            unicodeEncodeErrorFile='./dataTC/unicodeEncodeErrorFile.txt'
            f = codecs.open(unicodeEncodeErrorFile,'w','utf-8')
            f.write(link + ' UnicodeEncodeError')
            f.close()
        id = id + 1;
    




