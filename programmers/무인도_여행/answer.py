import sys
sys.setrecursionlimit(4500)# <- 요게 파이썬이라 꼭 필요한듯
def getFood(maps,x,y):
    foodCount=0
    foodCount+=int(maps[x][y])
    maps[x][y]='X'
    if x+1<len(maps) and maps[x+1][y]!='X':
        foodCount+=getFood(maps,x+1,y)
    if y+1<len(maps[0]) and maps[x][y+1]!='X':
        foodCount+=getFood(maps,x,y+1)
    if x-1>=0 and maps[x-1][y]!='X':
        foodCount+=getFood(maps,x-1,y)
    if y-1>=0 and maps[x][y-1]!='X':
        foodCount+=getFood(maps,x,y-1)
    
    return foodCount
    
def solution(maps):
    answer = []
    for i in range(len(maps)):
        maps[i]=list(maps[i])
        
    for x in range(len(maps)):
        for y in range(len(maps[0])):
            if maps[x][y]!='X':
                answer.append(getFood(maps,x,y))
    answer.sort()
    if answer==[]:
        return [-1]
    return answer
