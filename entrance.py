#-*- coding:utf8 -*-
import downloader
import myparser
import sys
default_encoding = 'utf-8'
reload(sys)
sys.setdefaultencoding(default_encoding)

TYPE = ['score', 'inplay', 'early']

if __name__ == '__main__':
    ARGS = sys.argv
    type = ARGS[1]
    if type not in TYPE:
        print 'You should specify checking keyword: {score, inplay, early}'
    europe_id = ARGS[2]
    if type != 'score':
        company_id = ARGS[3]
    p = None
    if type == 'score':
        d = downloader.ScoreDownloader()
        p = myparser.ScoreParser(d.download(), europe_id)
    elif type == 'inplay':
        d = downloader.InplayOddsDownloader()
        p = myparser.InplayParser(d.download(), europe_id, company_id)
    elif type == 'early':
        d = downloader.EarlyOddsDownloader()
        p = myparser.EarlyOddsParser(d.download(), europe_id, company_id)

    p.show_data()
