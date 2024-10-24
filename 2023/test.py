# def solution(cards1, cards2, goal):
#     answer = True

#     cards1Idx = 0
#     cards1Len = len(cards1)
#     cards2Idx = 0
#     cards2Len = len(cards2)
    
#     for i in range(0, len(goal)):
#         if cards1Idx < cards1Len and goal[i] == cards1[cards1Idx] :
#             cards1Idx += 1
#         elif cards2Idx < cards2Len and goal[i] == cards2[cards2Idx] :
#             cards2Idx += 1
#         else:
#             return False

#     return answer


# cards1 = ["i", "drink", "water"]
# cards2 = ["want", "to"]
# goal = ["i", "want", "to", "drink", "water"]


# print(solution(cards1, cards2, goal))


def solution(keymap, targets):
    answer = []
    dict = {}

    for key in keymap :
        for i,c in enumerate(key) :
            if c in dict:
                if i+1 < dict[c] :
                    dict[c] = i+1
            else :
                dict[str(c)] = i+1


    for taget in targets:
        mod = 0
        for c in taget :
            if c in dict :
                mod += dict[c]
            else :
                mod = -1 
                break

        answer.append(mod)

    return answer    


keymap = ["ABACD", "BCEFD"]	
targets = ["ABCD","AABB"]

print(solution(keymap, targets))