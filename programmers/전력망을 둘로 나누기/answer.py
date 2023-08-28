def count(linker,n,ban):
    candidate=[0]
    ck=[False for i in range(n)]
    ck[0]=True
    while len(candidate)>0:
        now=candidate.pop(0)
        for c in linker[now]:
            if max(ban)==max(c,now) and min(ban)==min(c,now):
                continue
            if not ck[c]:
                candidate.append(c)
                ck[c]=True
    return sum(ck)
    
def solution(n, wires):
    link=[[] for i in range(n)]
    answer=n
    for info in wires:
        a=info[0]-1
        b=info[1]-1
        if not b in link[a]:
            link[a].append(b)
        if not a in link[b]:
            link[b].append(a)
        
    for info in wires:
        ban=[info[0]-1,info[1]-1]
        temp=count(link,n,ban)
        answer=min(answer,abs(temp+temp-n))
        
    return answer