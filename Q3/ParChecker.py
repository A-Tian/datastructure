from StackModule import Stack

def parChecker(symbolString):
    s = Stack()     # <>堆疊
    s2 = Stack()    # /堆疊
    index = 0   #索引值
    while index < len(symbolString):    #索引值小於字串長度時，執行迴圈
        symbol = symbolString[index]
        if symbol == "<" or symbol == ">":
            s.push(symbol)
        elif symbolString[index - 1] == "<" and symbol == "/":      #字元等於 / 時前一個符號必須等於<
            s2.push(symbol)

        index = index + 1

    if (s2.size() * 4) == s.size():     #一個 / 對應兩組<>，因此 / 堆疊的4倍等於 <> 堆疊時，回傳True
        return True
    else:
        return False
