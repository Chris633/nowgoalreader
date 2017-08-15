# -*- coding:utf8 -*-

import downloader
import parser
import sys

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
        p = parser.ScoreParser(d.download(), europe_id)
    elif type == 'inplay':
        d = downloader.InplayOddsDownloader()
        p = parser.InplayParser(d.download(), europe_id, company_id)
    elif type == 'early':
        d = downloader.EarlyOddsDownloader()
        p = parser.EarlyOddsParser(d.download(), europe_id, company_id)

    p.show_data()
