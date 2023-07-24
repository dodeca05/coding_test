def solution(n):
    answer = []
    def hanoi(n,start,target,mid):
        if n==1:#하나 옮기는 거면 옮기고 끝내자
            answer.append([start,target])
            return
        hanoi(n-1,start,mid,target)#1번의 n개 중 n-1개를 2번으로 옮긴다.
        answer.append([start,target])#1번의 가장 큰 n을 3번으로 옮긴다.
        hanoi(n-1,mid,target,start)#2번의 n-1개를 3번으로 옮긴다.
        
    hanoi(n,1,3,2)#하노이 시작 n개를 1번에서 3번으로 옮기자 2번이 중간
    return answer