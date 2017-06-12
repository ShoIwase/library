# -*- coding: utf-8 -*-
import requests
import lxml.html
import tweepy
import os
import datetime

consumer_key = "*****"
consumer_secret = "*****"
access_token = "*****"
access_token_secret = "*****"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

response = requests.get('http://www.keyakizaka46.com/s/k46o/diary/member/list?ima=0000&ct=10')
root = lxml.html.fromstring(response.content)

f = open('title.txt')
oldtitle = f.read()
f.close()
 
title_xpath = root.xpath('/html/body/div/div/div[1]/div[2]/div/div[1]/article[1]/div[1]/div[2]/h3/a')
date_xpath = root.xpath('/html/body/div/div/div[1]/div[2]/div/div[1]/article[1]/div[3]/ul/li[1]')

title = title_xpath[0].text
date = date_xpath[0].text.strip()

now = datetime.datetime.now()

if oldtitle == title:
 print("true "+now.strftime("%Y/%m/%d %H:%M:%S"))
else:
 f = open('title.txt','w')
 f.write(title)
 f.close()
 print("false")
 api.update_status(status=(u"【"+title+u"】志田愛佳 "+date))