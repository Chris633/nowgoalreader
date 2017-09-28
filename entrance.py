# -*- coding:utf8 -*-
import downloader
import parser
import sys
default_encoding = 'utf-8'
reload(sys)
sys.setdefaultencoding(default_encoding)
TYPE_BALL = ['soccer','basketball']
TYPE = ['score', 'inplay', 'early']


def print_usage(type_error):
    if type_error == 1:
        print 'You should specify checking keyword type_ball: {soccer, basketball}'
        print 'python entrance.py ${type_ball}'
    elif type_error == 2:
        print 'You should specify checking keyword: {score, inplay, early}'
        print 'python entrance.py soccer score ${europe_id}'
        print 'python entrance.py soccer inplay ${europe_id} ${company_id}'
        print 'python entrance.py soccer early ${europe_id} ${company_id}'
    elif type_error == 3:
        print 'You should specify checking keyword: {score, odds}'
        print 'python entrance.py basketball score ${europe_id}'
        print 'python entrance.py basketball odds ${europe_id} ${company_id}'


if __name__ == '__main__':
    ARGS = sys.argv

    if ARGS[1] not in TYPE_BALL:
        print_usage(1)
        sys.exit()

    if len(ARGS) < 3 or ARGS[2] not in TYPE:
        if ARGS[1] == 'soccer': 
            print_usage(2)
        if ARGS[1] == 'basketball': 
            print_usage(3)
        sys.exit()

    europe_id = ARGS[3]

    p = None

    check_type_ball = ARGS[1]

    check_type = ARGS[2]

    if check_type_ball == 'soccer':
        if check_type == 'score':
            d = downloader.ScoreDownloader()
            p = parser.ScoreParser(d.download(), europe_id)
        elif check_type == 'inplay':
            d = downloader.InplayOddsDownloader()
            company_id = ARGS[4]
            p = parser.InplayParser(d.download(), europe_id, company_id)
        elif check_type == 'early':
            company_id = ARGS[4]
            d = downloader.EarlyOddsDownloader()
            p = parser.EarlyOddsParser(d.download(), europe_id, company_id)

    elif check_type_ball == 'basketball':
        if check_type == 'score':
            d = downloader.BasketballScoreDownloader()
            p = parser.BasketballScoreParser(d.download(), europe_id)
        elif check_type == 'odds':
            company_id = ARGS[4]
            d = downloader.BasketballEarlyOddsDownloader()
            p = parser.BasketballEarlyOddsParser(d.download(), europe_id, company_id)


    p.show_data()
