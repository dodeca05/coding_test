def pos2n(x,y):
    return x*(x+1)//2+y
def solution(n):
    answer = [-1 for i in range(n*(n+1)//2)]
    x=y=0
    dx=1
    dy=0
    limit=n*(n+1)//2
    for i in range(limit):
        answer[pos2n(x,y)]=i+1
        x+=dx
        y+=dy
        #print(answer,x,y,dx,dy)
        if pos2n(x,y)>=limit or answer[pos2n(x,y)]!=-1 or x>=n or x<0 or y>=n or y<0:
            x-=dx
            y-=dy
            if dx==1 and dy==0:
                dx=0
                dy=1
            elif dx==0 and dy==1:
                dx=-1
                dy=-1
            else:
                dx=1
                dy=0
            x+=dx
            y+=dy
            
    return answer