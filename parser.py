# -*- coding:utf8 -*-
from xml.dom.minidom import parseString


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
        text = self.__find_target__(self.__parse__())

        if text is None:
            print u"没有找到对应ID的比赛"
            return 0

        info = text.split('^')
        print u"赛事ID                  ".ljust(15)+":" + info[0][12:]
        print u"联赛/杯赛ID             ".ljust(15) + ":" + info[1]
        print u"类型(1联赛,2杯赛)       ".ljust(15) + ":" + info[2]
        print u"联赛名                  ".ljust(15) + ":" + info[3]
        print u"分几节进行(2半场,4小节)".ljust(15) + ":" + info[4]
        print u"颜色值                  ".ljust(15) + ":" + info[5]
        print u"开赛时间                ".ljust(15) + ":" + info[6]
        print u"比赛状态                ".ljust(15) + ":" + info[7]
        print u"小节剩余时间            ".ljust(15) + ":" + info[8]
        print u"主队ID                  ".ljust(15) + ":" + info[9]
        print u"主队名                  ".ljust(15) + ":" + info[10]
        print u"客队ID                  ".ljust(15) + ":" + info[11]
        print u"客队名                  ".ljust(15) + ":" + info[12]
        print u"主队排名                ".ljust(15) + ":" + info[13]
        print u"客队排名                ".ljust(15) + ":" + info[14]
        print u"主队得分                ".ljust(15) + ":" + info[15]
        print u"客队得分                ".ljust(15) + ":" + info[16]
        print u"主队一节得分(上半场)".ljust(15) + ":" + info[17]
        print u"客队一节得分(上半场)".ljust(15) + ":" + info[18]
        print u"主队二节得分            ".ljust(15) + ":" + info[19]
        print u"客队二节得分            ".ljust(15) + ":" + info[20]
        print u"主队三节得分(下半场)".ljust(15) + ":" + info[21]
        print u"客队三节得分(下半场)".ljust(15) + ":" + info[22]
        print u"主队四节得分            ".ljust(15) + ":" + info[23]
        print u"客队四节得分            ".ljust(15) + ":" + info[24]
        print u"加时数                  ".ljust(15) + ":" + info[25]
        print u"主队1'ot得分            ".ljust(15) + ":" + info[26]
        print u"客队1'ot得分            ".ljust(15) + ":" + info[27]
        print u"主队2'ot得分            ".ljust(15) + ":" + info[28]
        print u"客队2'ot得分            ".ljust(15) + ":" + info[29]
        print u"主队3'ot得分            ".ljust(15) + ":" + info[30]
        print u"客队3'ot得分            ".ljust(15) + ":" + info[31]
        print u"是否有技术统计          ".ljust(15) + ":" + info[32]
        print u"电视直播                ".ljust(15) + ":" + info[33]
        print u"备注(直播内容)          ".ljust(15) + ":" + info[34]
        print u"中立场(1中立场,0非中立)".ljust(15) + ":" + info[35][0]

    def __parse__(self):
        return parseString(self.source).getElementsByTagName('h')

    def __find_target__(self, ids):
        for id in ids:
            if self.target in id.toxml():
                return id.toxml()


class EarlyOddsParser(Parser):

    def __init__(self, source, target, company):
        Parser.__init__(self, source, target)
        self.company = company

    def show_data(self):

        company_odds = self.__find_target__(self.__parse__())
        if company_odds == {}:
            print u"没有找到对应ID或公司的比赛"
            return 0

        print u"""
[Hint]  companyId  companyName
             1         澳门
             2        易胜博
             3         皇冠
             8        Bet365
             9         韦德
            31         利记"""
        print "---------------------------------------------------"

        print u"1.联赛资料:"+'\n'
        league_info = company_odds['league'].split(',')
        print u"联赛ID:" + league_info[0].strip()
        print u"类型(1联赛,2杯赛):" + league_info[1]
        print u"颜色值:" + league_info[2]
        print u"联赛名:" + league_info[3]
        print u"比赛分几节(2半场,4小节)" + league_info[5]
        print "---------------------------------------------------"

        print u"2.赛程资料:" + '\n'
        match_info = company_odds['match'].split(',')
        print u"比赛ID:" + match_info[0].strip()
        print u"联赛ID:" + match_info[1]
        print u"比赛时间:" + match_info[2]
        print u"主队ID:" + match_info[3]
        print u"主队国语名:" + match_info[4]
        print u"主队繁体名:" + match_info[5]
        print u"主队英文名:" + match_info[6]
        print u"主队排名:" + match_info[7]
        print u"客队ID:" + match_info[8]
        print u"客队国语名:" + match_info[9]
        print u"客队繁体名:" + match_info[10]
        print u"客队英文名:" + match_info[11]
        print u"客队排名:" + match_info[12]
        print u"比赛状态(0未开,1上半场,2中场,3下半场,-11待定,-12腰斩,-13中断,-14推迟,-1完场):" + match_info[13]
        print u"主队得分:" + match_info[14]
        print u"客队得分:" + match_info[15]
        print u"电视直播:" + match_info[16]
        print u"中立场(1中立场,0非中立):" + match_info[17]
        print u"是否是竞彩赛事:" + match_info[18]
        print "---------------------------------------------------"

        print u"3.亚赔(让球盘):" + '\n'
        if 'asia_handicap' not in company_odds.keys():
            print u"Not found"
        else:
            asia_info = company_odds['asia_handicap'].split(',')
            print u"比赛ID:" + asia_info[0].strip()
            print u"公司ID:" + asia_info[1]
            print u"初盘盘口:" + asia_info[2]
            print u"主队初盘赔率:" + asia_info[3]
            print u"客队初盘赔率:" + asia_info[4]
            print u"即时盘口:" + asia_info[5]
            print u"主队即时赔率:" + asia_info[6]
            print u"客队即时赔率:" + asia_info[7]
        print "---------------------------------------------------"

        print u"4.欧赔(标准盘):" + '\n'
        if 'eu_handicap' not in company_odds.keys():
            print u"Not found"
        else:
            eu_info = company_odds['eu_handicap'].split(',')
            print u"比赛ID:" + eu_info[0].strip()
            print u"公司ID:" + eu_info[1]
            print u"初盘主胜赔率:" + eu_info[2]
            print u"初盘客胜赔率:" + eu_info[3]
            print u"即时盘主胜赔率:" + eu_info[4]
            print u"即时盘客胜赔率:" + eu_info[5]
        print "---------------------------------------------------"

        print u"大小球:" + '\n'
        if 'bigsmall' not in company_odds.keys():
            print u"Not found"
        else:
            bigsmall_info = company_odds['bigsmall'].split(',')
            print u"比赛ID:" + bigsmall_info[0].strip()
            print u"公司ID:" + bigsmall_info[1]
            print u"初盘盘口:" + bigsmall_info[2]
            print u"初盘大分赔率:" + bigsmall_info[3]
            print u"初盘小分赔率:" + bigsmall_info[4]
            print u"即时盘盘口:" + bigsmall_info[5]
            print u"即时盘大分赔率:" + bigsmall_info[6]
            print u"即时盘小分赔率:" + bigsmall_info[7]
        print "---------------------------------------------------"

    def __find_target__(self, ids):
        result = dict()

        leagues = ids[0]
        matches = ids[1]
        asia_handicaps = ids[2]
        eu_handicaps = ids[3]
        bigsmalls = ids[4]

        for match in matches:
            if self.target in match:
                result['match'] = match
                for league in leagues:
                    if match.split(',')[1] in league:
                        result['league'] = league

        def add_to_result(clauses, name):
            if name is 'bigsmall':
                company_id_dict = {'1': '4', '2': '5', '3': '6', '8': '11', '9': '12', '31': '34'}
                self.company = company_id_dict[self.company]
            for clause in clauses:
                company = clause.split(',')[1]
                if self.target in clause and self.company in company:
                    result[name] = clause

        add_to_result(asia_handicaps, 'asia_handicap')
        add_to_result(eu_handicaps, 'eu_handicap')
        add_to_result(bigsmalls, 'bigsmall')
        return result

    def __parse__(self):
        def split_clause(clauses):
            return clauses.split(';')

        parts = self.source.split('$')
        return map(split_clause, parts)
