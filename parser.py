# -*- coding:utf8 -*-
from xml.dom.minidom import parseString
import re


class Parser:

    def __init__(self, source, target):
        self.source = source
        self.target = target

    def show_data(self):
        pass

    def __parse__(self):
        pass

    def __find_target__(self, ids):
        pass


class ScoreParser(Parser):

    def __init__(self, source, target):
        Parser.__init__(self, source, target)

    def show_data(self):
        ids = self.__parse__()
        text = self.__find_target__(ids)

        if text is None:
            print u"没有找到对应ID的比赛"
            return 0

        tags = re.findall(r'<(.*?)>', text)
        en_to_zh = {
            "ID": u"比赛ID                                    : ",
            "color": u"颜色值                                    : ",
            "leagueID": u"联赛ID                                    : ",
            "kind": u"类型(1联赛,2杯赛)                         : ",
            "level": u"是否是重要比赛(1重要赛事,0一般赛事)       : ",
            "league": u"赛事类型(简体名,繁体名,英文名)            : ",
            "subLeague": u"subLeague                                 : ",
            "subLeagueID": u"subLeagueID                               : ",
            "time": u"比赛时间                                  : ",
            "time2": u"开场时间                                  : ",
            "home": u"主队(简体名,繁体名,英文名,主队ID)         : ",
            "away": u"客队(简体名,繁体名,英文名,客队ID)         : ",
            "state": u"比赛状态                                  : ",
            "homeScore": u"主队比分                                  : ",
            "awayScore": u"客队比分                                  : ",
            "bc1": u"主队上半场比分                            : ",
            "bc2": u"客队上半场比分                            : ",
            "red1": u"主队红牌                                  : ",
            "red2": u"客队红牌                                  : ",
            "yellow1": u"主队黄牌                                  : ",
            "yellow2": u"客队黄牌                                  : ",
            "order1": u"主队排名                                  : ",
            "order2": u"客队排名                                  : ",
            "explain": u"比赛说明                                  : ",
            "zl": u"是否中立场                                : ",
            "tv": u"电视直播                                  : ",
            "lineup": u"是否有阵容(1为有)                         : ",
            "explain2": u"比赛说明2(加时,点球等)                    : ",
            "corner1": u"主队角球                                  : ",
            "corner2": u"客队角球                                  : "
                    }

        num_to_state = {
            '0': u'未开',
            '1': u'上半场',
            '2': u'中场',
            '3': u'下半场',
            '4': u'加时',
            '-11': u'待定',
            '-12': u'腰斩',
            '-13': u'中断',
            '-14': u'推迟',
            '-1': u'完场',
            '-10': u'取消'
        }

        for tag in tags[1:-1]:
            if tag[-1] == '/':
                print en_to_zh[str(tag[:-1])] + 'None'
            elif tag[0] != '/':
                try:
                    content = re.findall('<' + tag + '>(.*?)</' + tag + '>', text)
                    content = content[0] if len(content) > 0 else 'None'

                    if tag == 'state':
                        content = num_to_state[content]

                    print en_to_zh[str(tag)] + content
                except KeyError:
                    pass

    def __parse__(self):
        return parseString(self.source).getElementsByTagName('ID')

    def __find_target__(self, ids):
        for id in ids:
            if self.target in id.toxml():
                return id.parentNode.toxml()


class EarlyOddsParser(Parser):

    def __init__(self, source, target, company):
        Parser.__init__(self, source, target)
        self.company = company

    def show_data(self):

        company_odds = self.__find_target__(self.__parse__())
        if company_odds == {}:
            print u"没有找到对应ID或公司的比赛"
            return 0
        print "---------------------------------------------------"
        print u"1.联赛资料:"+'\n'
        print u"联赛ID:"+company_odds['league'].split(',')[0].strip()
        print u"类型（1联赛,2杯赛):" + company_odds['league'].split(',')[1]
        print u"颜色值:" + company_odds['league'].split(',')[2]
        print u"国语名:" + company_odds['league'].split(',')[3]
        print u"繁体名:" + company_odds['league'].split(',')[4]
        print u"英文名:" + company_odds['league'].split(',')[5]
        print u"资料库路径:" + company_odds['league'].split(',')[6]
        print u"是否是重要赛事(0次要赛事,1重要赛事):" + company_odds['league'].split(',')[7]
        print "---------------------------------------------------"

        print u"2.赛程资料:" + '\n'
        print u"比赛ID:" + company_odds['match'].split(',')[0].strip()
        print u"联赛ID:" + company_odds['match'].split(',')[1]
        print u"比赛时间:" + company_odds['match'].split(',')[2]
        print u"开场时间:" + company_odds['match'].split(',')[3]
        print u"主队ID:" + company_odds['match'].split(',')[4]
        print u"主队国语名:" + company_odds['match'].split(',')[5]
        print u"主队繁体名:" + company_odds['match'].split(',')[6]
        print u"主队英文名:" + company_odds['match'].split(',')[7]
        print u"主队排名:" + company_odds['match'].split(',')[8]
        print u"客队ID:" + company_odds['match'].split(',')[9]
        print u"客队国语名:" + company_odds['match'].split(',')[10]
        print u"客队繁体名:" + company_odds['match'].split(',')[11]
        print u"客队英文名:" + company_odds['match'].split(',')[12]
        print u"客队排名:" + company_odds['match'].split(',')[13]
        print u"比赛状态(0未开,1上半场,2中场,3下半场,-11待定,-12腰斩,-13中断,-14推迟,-1完场):" + company_odds['match'].split(',')[14]
        print u"主队得分:" + company_odds['match'].split(',')[15]
        print u"客队得分:" + company_odds['match'].split(',')[16]
        print u"中立场:" + company_odds['match'].split(',')[17]
        print u"级别(0彩票赛事,1重要赛事,2次要赛事):" + company_odds['match'].split(',')[18]
        print u"主队红牌:" + company_odds['match'].split(',')[19]
        print u"客队红牌:" + company_odds['match'].split(',')[20]
        print u"主队黄牌:" + company_odds['match'].split(',')[21]
        print u"客队黄牌:" + company_odds['match'].split(',')[22]
        print "---------------------------------------------------"

        print u"3.亚赔(让球盘):" + '\n'
        print u"比赛ID:" + company_odds['asia_handicap'].split(',')[0].strip()
        print u"公司ID:" + company_odds['asia_handicap'].split(',')[1]
        print u"初盘盘口:" + company_odds['asia_handicap'].split(',')[2]
        print u"主队初盘赔率:" + company_odds['asia_handicap'].split(',')[3]
        print u"客队初盘赔率:" + company_odds['asia_handicap'].split(',')[4]
        print u"即时盘口:" + company_odds['asia_handicap'].split(',')[5]
        print u"主队即时赔率:" + company_odds['asia_handicap'].split(',')[6]
        print u"客队即时赔率:" + company_odds['asia_handicap'].split(',')[7]
        print u"是否封盘:" + company_odds['asia_handicap'].split(',')[8]
        print u"是否走地:" + company_odds['asia_handicap'].split(',')[9]
        print "---------------------------------------------------"

        print u"4.欧赔(标准盘):" + '\n'
        print u"比赛ID:" + company_odds['eu_handicap'].split(',')[0].strip()
        print u"公司ID:" + company_odds['eu_handicap'].split(',')[1]
        print u"初盘主胜赔率:" + company_odds['eu_handicap'].split(',')[2]
        print u"初盘和局赔率:" + company_odds['eu_handicap'].split(',')[3]
        print u"初盘客胜赔率:" + company_odds['eu_handicap'].split(',')[4]
        print u"即时盘主胜赔率:" + company_odds['eu_handicap'].split(',')[5]
        print u"即时盘和局赔率:" + company_odds['eu_handicap'].split(',')[6]
        print u"即时盘客胜赔率:" + company_odds['eu_handicap'].split(',')[7]
        print "---------------------------------------------------"

        print u"大小球:" + '\n'
        print u"比赛ID:" + company_odds['bigsmall'].split(',')[0].strip()
        print u"公司ID:" + company_odds['bigsmall'].split(',')[1]
        print u"初盘盘口:" + company_odds['bigsmall'].split(',')[2]
        print u"初盘大球赔率:" + company_odds['bigsmall'].split(',')[3]
        print u"初盘小球赔率:" + company_odds['bigsmall'].split(',')[4]
        print u"即时盘盘口:" + company_odds['bigsmall'].split(',')[5]
        print u"即时盘大球赔率:" + company_odds['bigsmall'].split(',')[6]
        print u"即时盘小球赔率:" + company_odds['bigsmall'].split(',')[7]
        print "---------------------------------------------------"

        print u"半场让球:" + '\n'
        print u"比赛ID:" + company_odds['half'].split(',')[0].strip()
        print u"公司ID:" + company_odds['half'].split(',')[1]
        print u"初盘盘口:" + company_odds['half'].split(',')[2]
        print u"主队初盘赔率:" + company_odds['half'].split(',')[3]
        print u"客队初盘赔率:" + company_odds['half'].split(',')[4]
        print u"即时盘口:" + company_odds['half'].split(',')[5]
        print u"主队即时赔率:" + company_odds['half'].split(',')[6]
        print u"客队即时赔率:" + company_odds['half'].split(',')[7]
        print "---------------------------------------------------"

        print u"半场大小球:" + '\n'
        print u"比赛ID:" + company_odds['hbigsmall'].split(',')[0].strip()
        print u"公司ID:" + company_odds['hbigsmall'].split(',')[1]
        print u"初盘盘口:" + company_odds['hbigsmall'].split(',')[2]
        print u"初盘大球赔率:" + company_odds['hbigsmall'].split(',')[3]
        print u"初盘小球赔率:" + company_odds['hbigsmall'].split(',')[4]
        print u"即时盘盘口:" + company_odds['hbigsmall'].split(',')[5]
        print u"即时盘大球赔率:" + company_odds['hbigsmall'].split(',')[6]
        print u"即时盘小球赔率:" + company_odds['hbigsmall'].split(',')[7]
        print "---------------------------------------------------"

    def __find_target__(self, ids):
        result = dict()

        leagues = ids[0]
        matches = ids[1]
        asia_handicaps = ids[2]
        eu_handicaps = ids[3]
        bigsmalls = ids[4]
        halfs = ids[6]
        hbigsmalls = ids[7]

        for match in matches:
            if self.target in match:
                result['match'] = match
                for league in leagues:
                    if match.split(',')[1] in league:
                        result['league'] = league
        def add_to_result(clauses,name):
            for clause in clauses:
                company = clause.split(',')[1]
                if self.target in clause and self.company in company:
                    result[name] = clause

        add_to_result(asia_handicaps,'asia_handicap')
        add_to_result(eu_handicaps, 'eu_handicap')
        add_to_result(bigsmalls, 'bigsmall')
        add_to_result(halfs, 'half')
        add_to_result(hbigsmalls, 'hbigsmall')

        return result

    def __parse__(self):
        def split_clause(clauses):
            return clauses.split(';')

        parts = self.source.split('$')
        return map(split_clause, parts)


class InplayParser(Parser):

    def __init__(self, source, target, company):
        Parser.__init__(self, source, target)
        self.company = company
        self.odds_type = ('1', '2', '4')

    def show_data(self):
        all_odds = self.__find_target__(self.__parse__())
        print'-------------------------------------------------------------------------------------------------'
        print "%50s"%"Handicap:\n"
        print "%5s" % u"记录ID","%8s" % u"比赛ID","%3s" % u"时间","%5s" % u"主队得分",\
            "%5s" % u"客队得分","%4s" % u"主队红牌","%4s" % u"客队红牌","%2s" % u"类型",\
            "%3s" % u"公司ID","%4s" % u"赔率1","%4s" % u"赔率2","%4s" % u"赔率3","%8s" % u"变盘时间"

        for text1 in all_odds['1']:
            print "%s" % text1[0][3:],"%8s" % text1[1],"%4s" % text1[2],\
                "%7s" % text1[3],"%8s" % text1[4],"%8s" % text1[5],\
                "%8s" % text1[6],"%6s" % text1[7],"%5s" % text1[8],\
                "%8s" % text1[9],"%7s" % text1[10],"%6s" % text1[11],"%7s" % text1[12][:-4]
        print'-------------------------------------------------------------------------------------------------'
        print "%50s" % "Hilo:\n"
        print "%5s" % u"记录ID", "%8s" % u"比赛ID", "%3s" % u"时间", "%5s" % u"主队得分", \
            "%5s" % u"客队得分", "%4s" % u"主队红牌", "%4s" % u"客队红牌", "%2s" % u"类型", \
            "%3s" % u"公司ID", "%4s" % u"赔率1", "%4s" % u"赔率2", "%4s" % u"赔率3", "%8s" % u"变盘时间"

        for text1 in all_odds['2']:
            print "%s" % text1[0][3:], "%8s" % text1[1], "%4s" % text1[2], \
                "%7s" % text1[3], "%8s" % text1[4], "%8s" % text1[5], \
                "%8s" % text1[6], "%6s" % text1[7], "%5s" % text1[8], \
                "%8s" % text1[9], "%7s" % text1[10], "%6s" % text1[11], "%7s" % text1[12][:-4]
        print'-------------------------------------------------------------------------------------------------'
        print "%50s" % "Standard:\n"
        print "%5s" % u"记录ID", "%8s" % u"比赛ID", "%3s" % u"时间", "%5s" % u"主队得分", \
            "%5s" % u"客队得分", "%4s" % u"主队红牌", "%4s" % u"客队红牌", "%2s" % u"类型", \
            "%3s" % u"公司ID", "%4s" % u"赔率1", "%4s" % u"赔率2", "%4s" % u"赔率3", "%8s" % u"变盘时间"

        for text1 in all_odds['4']:
            print "%s" % text1[0][3:], "%8s" % text1[1], "%4s" % text1[2], \
                "%7s" % text1[3], "%8s" % text1[4], "%8s" % text1[5], \
                "%8s" % text1[6], "%6s" % text1[7], "%5s" % text1[8], \
                "%8s" % text1[9], "%7s" % text1[10], "%6s" % text1[11], "%7s" % text1[12][:-4]
        print'-------------------------------------------------------------------------------------------------'

    def __parse__(self):
        return parseString(self.source).getElementsByTagName('h')

    def __find_target__(self, ids):
        standard = list()
        handicap = list()
        hilo = list()

        all_odds = {
            '1': handicap,
            '2': hilo,
            '4': standard
        }

        for id in ids:
            content = id.toxml().split(',')
            company = content[8]
            odds_type = content[7]
            if company in self.company and odds_type in self.odds_type and self.target in content[1]:
                all_odds[odds_type].append(content)
        return all_odds

    @staticmethod
    def __compare_time(first_time, second_time):
        pass
