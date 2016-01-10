#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Code by Zirou - irc.priv8.jp #nosafe and #python

import requests
import BeautifulSoup

user_agent = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
m = requests.get("http://www.mercadobitcoin.com.br/trade-api/", headers=user_agent)
soup = BeautifulSoup.BeautifulSoup(m.content)

for a in soup.findAll("div", attrs={'class': "tickerBlock"}):
    print "%s %s" % (a.text, a.get("ticker_ultimo"))
