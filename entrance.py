# -*- coding:utf8 -*-
import downloader
import parser
import sys
default_encoding = 'utf-8'
reload(sys)
sys.setdefaultencoding(default_encoding)
TYPE = ['score', 'early']


def print_usage():
    print 'You should specify checking keyword: {score, inplay, early}'
    print 'python entrance.py score ${europe_id}'
    print 'python entrance.py early ${europe_id} ${company_id}'


if __name__ == '__main__':
    ARGS = sys.argv

    if len(ARGS) < 3 or ARGS[1] not in TYPE:
        print_usage()
        sys.exit()

    europe_id = ARGS[2]

    p = None

    check_type = ARGS[1]

    if check_type == 'score':
        d = downloader.ScoreDownloader()
        p = parser.ScoreParser(d.download(), europe_id)
    elif check_type == 'early':
        company_id = ARGS[3]
        d = downloader.EarlyOddsDownloader()
        p = parser.EarlyOddsParser(d.download(), europe_id, company_id)

    p.show_data()
