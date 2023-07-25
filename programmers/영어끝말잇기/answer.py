def solution(n, words):
    count=0
    keys=[]
    for w in words:
        if w in keys or (len(keys)>0 and keys[-1][-1]!=w[0]):
            return[count%n+1,count//n+1]
        keys.append(w)
        count+=1
    return [0,0]