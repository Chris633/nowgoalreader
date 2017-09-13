# -*- coding:utf8 -*-
import urllib2


class Downloader:

    def __init__(self):
        pass

    def download(self):
        pass


class EarlyOddsDownloader(Downloader):

    def __init__(self):
        Downloader.__init__(self)

    def download(self):
        response = urllib2.urlopen('http://interface.win007.com/lq/LqOdds.aspx')
        # response = open('LqOdds.aspx', 'r')
        return response.read()


class ScoreDownloader(Downloader):
    def __init__(self):
        Downloader.__init__(self)

    def download(self):
        response = urllib2.urlopen('http://interface.win007.com/lq/today.aspx')
        # response = open('today.aspx', 'r')
        return response.read()
