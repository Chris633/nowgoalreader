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
        response = urllib2.urlopen('http://interface.win007.com/zq/odds.aspx')
        # response = open('odds.txt', 'r')
        return response.read()


class InplayOddsDownloader(Downloader):
    def __init__(self):
        Downloader.__init__(self)

    def download(self):
        response = urllib2.urlopen('http://interface.win007.com/zq/Odds_Running.aspx')
        # response = open('team.xml', 'r')
        return response.read()


class ScoreDownloader(Downloader):
    def __init__(self):
        Downloader.__init__(self)

    def download(self):
        response = urllib2.urlopen('http://interface.win007.com/zq/today.aspx')
        # response = open('score.xml', 'r')
        return response.read()


class BasketballEarlyOddsDownloader(Downloader):

    def __init__(self):
        Downloader.__init__(self)

    def download(self):
        response = urllib2.urlopen('http://interface.win007.com/lq/LqOdds.aspx')
        # response = open('LqOdds.aspx', 'r')
        return response.read()


class BasketballScoreDownloader(Downloader):
    def __init__(self):
        Downloader.__init__(self)

    def download(self):
        response = urllib2.urlopen('http://interface.win007.com/lq/today.aspx')
        # response = open('today.aspx', 'r')
        return response.read()
