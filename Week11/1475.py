# from collections import Counter
# result = 1
# roomnumber = input()
# collection = Counter(roomnumber)
# sum = 0

# if collection['9'] :
#     sum += collection['9']
# if collection['6'] :
#     sum += collection['6']
    
# if sum > 0 :
#     if sum % 2 == 0 :
#         result = sum // 2
#     else :
#         result = (sum // 2)+ 1

# print( result)

# for key in collection:
#     if collection[key] > 1 and key != '9' and key != '6':
#         print(collection[key])
#         result += collection[key] - 1
            
# print(result)

num = input()
checked = [0]*10

for i in num:
    if i == '6' or i == '9':
        if checked[6] <= checked[9]:
            checked[6] += 1
        else:
            checked[9] += 1
    else:
        checked[int(i)] += 1

print(max(checked))