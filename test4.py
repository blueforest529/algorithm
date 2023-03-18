# from itertools import product

# def solution(users, emoticons):
#     E = len(emoticons)
#     result = [0, 0]
#     percents = (10, 20, 30, 40)
#     prod = product(percents, repeat=E)
    
#     for p in prod:
#         print(p)
    
    
#     # return answer

users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]


from itertools import product

def solution(users, emoticons):
    E = len(emoticons)
    result = [0, 0]
    percents = (10, 20, 30, 40)
    prod = product(percents, repeat=E)


    for p in prod:
        prod_members, prod_price = 0, 0
        for buy_percent, max_price in users: 
            user_price = 0
            print(p)
            for item_price, item_percent in zip(emoticons, p):
                print(item_price, item_percent)
                if item_percent >= buy_percent:
                    user_price += item_price * (100-item_percent) * 0.01
                print("user_price", user_price)
            if user_price >= max_price:
                prod_members += 1
            else:
                prod_price += user_price

        result = max(result, [prod_members, prod_price])

    return result

print(solution(users, emoticons))
