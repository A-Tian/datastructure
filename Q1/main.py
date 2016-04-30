from StackModule import Stack

def infixToPrefix(infixexpr):
    prec = {}
    prec["*"] = 3	#設定優先順序
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec[")"] = 1	#設定優先順序
    opStack = Stack()
    prefixList = []
    tokenList = infixexpr.split()	#將字串分割
    tokenList.reverse()	#反轉排序

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":	#如果是英文或數字直接新增
            prefixList.append(token)
        elif token == ')':	#判斷op
            opStack.push(token)
        elif token == '(':	#判斷op
            topToken = opStack.pop()
            while topToken != ')':
                prefixList.append(topToken)
                topToken = opStack.pop()
        else:	#判斷op
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] > prec[token]):
                  prefixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        prefixList.append(opStack.pop())
    prefixList.reverse()	#反轉排序
    return " ".join(prefixList)

print(infixToPrefix("A + B"))
print(infixToPrefix("A * B + C * D"))
print(infixToPrefix("A + B * C + D"))
print(infixToPrefix("( A + B ) * ( C + D )"))
