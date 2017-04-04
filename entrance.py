odds = open('odds.txt')

parts = odds.readline().split('$')

print len(parts)

def split_clauses(clauses):
    return clauses.split(';')

print len(map(split_clauses, parts[1:5])[0])

# part = parts[1]
# matches = part.split(';')
# for match in matches:
#     tmp = match.split(',')
#     print tmp[0:24]


# part = parts[2]
# i = 3
# for part in parts[2:]:
#     print i
#     matches = part.split(';')
#     for match in matches:
#         if '1288337' in match:
#             print match
#     i += 1