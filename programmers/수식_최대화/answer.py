def parse_expression(expression):
    tokens = []
    current_token = ''
    
    for char in expression:
        if char.isdigit():
            current_token += char
        else:
            if current_token:
                tokens.append(int(current_token))
                current_token = ''
            tokens.append(char)
    
    if current_token:
        tokens.append(int(current_token))
    
    return tokens
def caculate(expression_list,op_Pr):
    op=op_Pr[0]
    for i in range(expression_list.count(op)):
        cur=expression_list.index(op)
        a=expression_list[cur-1]
        b=expression_list[cur+1]
        if op=='*':
            temp=a*b
        elif op=='+':
            temp=a+b
        else:
            temp=a-b
        expression_list=expression_list[:cur-1]+[temp]+expression_list[cur+2:]
    if len(op_Pr)>1:
        return caculate(expression_list,op_Pr[1:])
    return abs(expression_list[0])
    
def solution(expression):
    temp_list=parse_expression(expression)
    return max(caculate(temp_list,["+","-","*"]),\
       caculate(temp_list,["+","*","-"]),\
       caculate(temp_list,["-","+","*"]),\
       caculate(temp_list,["-","*","+"]),\
        caculate(temp_list,["*","-","+"]),\
        caculate(temp_list,["*","+","-"])
       )