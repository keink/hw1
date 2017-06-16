# coding: utf-8
#文字列中の数字を数値に変換
def readNumber(line, index):
    number = 0
    #まず整数部分
    while index < len(line) and line[index].isdigit():
        number = number * 10 + float(line[index])
        index += 1
    #小数点以下も数値に変換
    if index < len(line) and line[index] == '.':
        index += 1
        keta = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * keta
            keta *= 0.1
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index

#+を読み込みtypeがPLUSのtokenにして返す
def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1

#-を読み込みtypeがMINUSのtokenにして返す
def readMinus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

#*を読み込みtypeがTIMESのtokenにして返す
def readTimes(line, index):
    token={'type': 'TIMES'}
    return token, index + 1

#/を読み込みtypeがDIVIDEのtokenにして返す
def readDivide(line, index):
    token={'type': 'DIVIDE'}
    return token, index + 1

#文字列をtokenのリストに変換する
def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        elif line[index] == '*':
            (token, index) = readTimes(line, index)
        elif line[index] == '/' :
            (token, index) = readDivide(line, index)           
        else:
            print 'Invalid character found: ' + line[index]
            exit(1)
        #tokenをリストの末尾に追加
        tokens.append(token)
    return tokens

#足し算と引き算をする
def plusminus_evaluate(tokens):
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            #前の要素の記号で場合分け
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print 'Invalid syntax'
        index += 1
    return answer

#掛け算と割り算をする
def timesdivide_evaluate(tokens):
    ntokens = []
    index = 0
    while index < len(tokens):

        #*が出できたときは、ntokensの末尾要素と元のtokensの次の要素の掛け算
        if tokens[index]['type'] == 'TIMES':
            number = ntokens[-1]['number'] * tokens[index+1]['number']
            token = {'type':'NUMBER','number':number}

            #前の要素が新しいtokenのリストに追加済み 削除して掛け合わせた数値を追加
            ntokens.pop()
            ntokens.append(token)
            index += 2

        elif tokens[index]['type'] == 'DIVIDE':
            number = ntokens[-1]['number'] / tokens[index+1]['number']
            token = {'type':'NUMBER','number':number}
            ntokens.pop()
            ntokens.append(token)
            index += 2

        #*,/以外(+,数値)だったら新しいtokenの末尾に追加
        else:
            ntokens.append(tokens[index])
            index += 1

    return ntokens


#正しく計算できているかテスト
def test(line, expectedAnswer):
    tokens = tokenize(line)
    ntokens = timesdivide_evaluate(tokens)
    actualAnswer = plusminus_evaluate(ntokens)
    if abs(actualAnswer - expectedAnswer) < 1e-8:
        print "PASS! (%s = %f)" % (line, expectedAnswer)
    else:
        print "FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer)


# Add more tests to this function :)
def runTest():
    print "==== Test started! ===="
    #足し算と引き算だけ
    test("1",1)
    test("1+2",3)
    test("1.0+2",3)
    test("1.0+2.0",3)
    test("1-2",-1)
    test("1.0-2",-1)
    test("1.0-2.0",-1)
    test("1.0+2.1-3.0",0.1)
    test("1.0-2.1+3.0",1.9)

    #掛け算と割り算だけ
    test("1*2",2)
    test("1.0*2",2)
    test("1.0*2.0",2)
    test("1/2",0.5)
    test("1.0/2",0.5)
    test("1/2.0",0.5)
    test("1.0/2.0",0.5)
    test("1.0*2.0*3.0",6)
    test("6.0/3.0/2.0",1)
    test("1.0*3.0/2.0",1.5)
    test("1.0/2.0*3.0",1.5)

    #加減、乗除の組み合わせ
    test("1.0+2.0*3.0",7)
    test("1.0*2.0+3.0",5.0)
    test("1.0+4.0/2.0-3.0*4.0",-9)

    print "==== Test finished! ====\n"

runTest()

while True:
    print '> ',
    line = raw_input()  #読み込み
    tokens = tokenize(line) #字句のリストに変換
    ntokens = timesdivide_evaluate(tokens)  #掛け算、割り算の計算
    answer = plusminus_evaluate(ntokens)    #足し算、引き算の計算
print "answer = %f\n" % answer