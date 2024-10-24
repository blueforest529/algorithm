# from datetime import datetime
# # from dateutil import relativedelta

# def solution(today, terms, privacies):
#     answer = []
#     termsSplit = {}
#     privaciesSplit = {}
    
#     for i in terms:
#         tmp = i.split(' ')
#         termsSplit[tmp[0]] = tmp[1]

#     for i in privacies:
#         tmp = i.split(' ')
#         privaciesSplit[tmp[0]] = tmp[1]

#     for i in range(len(privacies)):
#         datetime, category = privacies[i].split()
#         datetime = list(map(int, datetime.split('.')))
#         print(datetime)
#         # datetime = datetime[2] + datetime[1] * 28 + datetime[0] * 28 * 12
#         # if datetime + dic[category] <= today:
#         #     result.append(i+1)


#     # # 현재 시간을 가져온다.
#     # now = datetime.strptime(today ,"%Y.%m.%d")
#     # print(now)
#     # # print(now - relativedelta(months=1))

    
#     # for i, c in enumerate(privaciesSplit):
#     #     day = datetime.strptime(c ,"%Y.%m.%d")
#     #     day = day + relativedelta(months=termsSplit[privaciesSplit[c]])
#     #     if now > day :
#     #         answer.append(i)

#     return answer

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

DATE_FORMAT = "%Y.%m.%d"

def solution(today, terms, privacies):
    today = datetime.strptime(today, DATE_FORMAT) + timedelta(days=1)

    terms_dict = {}
    for term in terms:
        category, expire_months = term.split()
        terms_dict[category] = int(expire_months)

    terms = dict(term.split() for term in terms)

    answer = []
    for index, privacy in enumerate(privacies):
        signed_at, category = privacy.split()
        # print(relativedelta(months=terms_dict[category]))
        if datetime.strptime(signed_at, DATE_FORMAT) + relativedelta(months=terms_dict[category]) < today:
            answer.append(index+1)

    return answer


today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

print(solution(today, terms, privacies))