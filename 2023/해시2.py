#프로그래머스 - 베스트엘범
def solution(genres, plays):
    answer = []
    site = {}
    for i, (genre, play) in enumerate(zip(genres,plays)):
        if genre in site.keys():
            site[genre] = [site[genre][0]+play, site[genre][1]+[[play,i]]]
        else:
            site[genre] = [play, [[play,i]]]

    site = sorted(site.items(), key=lambda x: -x[1][0])
    for i, indexs in site :
        for j in sorted(indexs[1], key=lambda x: -x[0])[:2] :
            answer.append(j[1])

    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))