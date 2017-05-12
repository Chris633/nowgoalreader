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
        ids = self.__parse__()
        print self.__find_target__(ids)

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
        display = dict()
        display['europe_id'] = self.target

        match = company_odds[0].split(',')
        display['match_time'] = match[2]
        display['start_time'] = match[3]
        display['state'] = match[14]
        display['home_score'] = match[15]
        display['away_score'] = match[16]
        display['home_red_card'] = match[20]
        display['away_red_card'] = match[21]

        handicap_odds = company_odds[1].split(',')
        handicap = dict()
        handicap['home_odds'] = handicap_odds[6]
        handicap['line'] = handicap_odds[5]
        handicap['away_odds'] = handicap_odds[7]
        display['handicap'] = handicap

        standard_odds = company_odds[2].split(',')
        standard = dict()
        standard['home_odds'] = standard_odds[5]
        standard['draw_odds'] = standard_odds[6]
        standard['away_odds'] = standard_odds[7]
        display['standard'] = standard

        hilo_odds = company_odds[3].split(',')
        hilo = dict()
        hilo['line'] = hilo_odds[5]
        hilo['home_odds'] = hilo_odds[6]
        hilo['away_odds'] = hilo_odds[7]
        display['hilo'] = hilo

        print display
        return display

    def __find_target__(self, ids):
        result = list()

        matches = ids[0]
        standard = ids[1]
        handicap = ids[2]
        hilo = ids[3]

        for match in matches:
            if self.target in match:
                result.append(match)

        def add_to_result(clauses):
            for clause in clauses:
                company = clause.split(',')[1]
                if self.target in clause and company in self.company:
                    result.append(clause)

        # add_to_result(matches)
        add_to_result(standard)
        add_to_result(handicap)
        add_to_result(hilo)
        for r in result:
            print r
        return result

    def __parse__(self):

        def split_clause(clauses):
            return clauses.split(';')

        parts = self.source.split('$')

        return map(split_clause, parts[1:5])


class InplayParser(Parser):

    def __init__(self, source, target, company):
        Parser.__init__(self, source, target)
        self.company = company
        self.odds_type = ('1', '2', '4')

    def show_data(self):
        all_odds = self.__find_target__(self.__parse__())
        print all_odds

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
            if company in self.company:
                odds_type = content[7]
                for type in self.odds_type:
                    if odds_type == type:
                        all_odds[type].append(content)
        return all_odds
