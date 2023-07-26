def numTransfer(num,s):#진법 변환
    result=""
    numbers=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    while num>=s:
        temp=num%s
        result=numbers[temp]+result
        num=num//s
    result=numbers[num]+result
    return result
def solution(n, t, m, p):
    p-=1#순서인지 쉽게 알아내기 위해 하나를 빼서 0번째~ 부터 이런식으로 나중에 판단하게 된다. 
    answer = ''
    count=0
    number=0
    while len(answer)<t:
        temp=numTransfer(number,n)
        for al in temp:
            if count%m==p:
                answer+=al
            count+=1
        number+=1
        
    return answer[:t]