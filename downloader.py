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
        return response.read()


class InplayOddsDownloader(Downloader):
    def __init__(self):
        Downloader.__init__(self)

    def download(self):
        response = urllib2.urlopen('http://interface.win007.com/zq/Odds_Running.aspx')
        return response.read()


class ScoreDownloader(Downloader):
    def __init__(self):
        Downloader.__init__(self)

    def download(self):
        response = urllib2.urlopen('http://interface.win007.com/zq/today.aspx')
        return response.read()
