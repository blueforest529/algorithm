# name = ['tom', 'jerry', 'tom', 'nick']

# def same_name():
#     same = set()
#     for i in range(0, len(name)-1):
#         for j in range(i+1, len(name)):
#             if name[i] == name[j] :
#                 same.add(name[i])

#     return same

# print(same_name())

name2 = ['tom', 'jerry', 'nick']

def zzak():
    zari = set()
    for i in range(0, len(name2)-1):
        for j in range(i+1, len(name2)):
            zari.add(name2[i]+"-"+name2[j])

    return zari

print(zzak())

