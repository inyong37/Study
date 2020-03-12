# -*- coding: utf-8 -*-
# Author: Inyong Hwang (inyong1020@gmail.com)
# Date: 2020-03-12-Thu
# Programmers
# Coding Test Examples/Hash_04_Songs
# 코딩테스트 연습/해시/베스트앨범

# Try 1

def solution(genres, plays):
    # Make songs list and sort by number of song played
    # songs = [index of song, genre, number of song played]
    songs = []
    for index, play in enumerate(plays):
        genre = genres[index]
        songs.append([index, genre, play])
    songs.sort(key=lambda x:x[2], reverse=True)
    # Count number of play and sort by genre
    # counted = [genre, total number of song played]
    count = {}
    for i in range(0, len(genres)):
        if genres[i] not in count.keys():
            count[genres[i]] = int(plays[i])
        else:
            count[genres[i]] += int(plays[i])
    counted = sorted(count.items(), reverse=True)
    del count 
    order = [i[0] for i in counted]
    # Pick two songs' index of each genre
    answer = []
    index = 1
    for i in range(0, len(songs[0])):
        if i is 0:
            answer.append(songs[i][0])
            index += 1
        elif songs[i][2] is songs[i-1][2] and index == 3:
            pass
        elif songs[i][2] is songs[i-1][2] and index == 1:
            answer.append(songs[i][0])
            index += 1
        elif songs[i][2] is not songs[i-1][2]:
            answer.append(songs[i][0])
            index = 1
    print(answer)

# Try 2

def solution(genres, plays):
    # playsDict = {genre : total # of played}
    playsDict = {}
    # d = {genre : [# of played, index]}
    d = {}
    for i in range(0, len(genres)):
        genre = genres[i]
        play = plays[i]
        playsDict[genre] = playsDict.get(genre, 0) + play
        d[genre] = d.get(genre, []) + [ (play, i) ]
    
    # Sort by descending order with # of played genre
    genreSort = sorted(playsDict.items(), key=lambda x: x[1], reverse=True)
    
    # Sort by descending order with # of played and sort by ascending order with index
    answer = []
    for (genre, totalPlay) in genreSort:
        d[genre] = sorted(d[genre], key=lambda x: (-x[0], x[1]))
        answer += [ idx for (play, idx) in d[genre][:2] ]
    return answer

# Reference: https://gurumee92.tistory.com/159
