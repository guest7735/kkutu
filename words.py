import random
f = open("kkutu_co_kr.txt", encoding="utf-8")
result = []
for line in f:
    result.append(line)

print(str(len(result)))

def get_word(start):
    text_list = []
    for i in result:
        if i.startswith(start):
            text = i
            if len(text) >= 2:
                text_list.append(text)
    text_list.sort(key=lambda item: (len(item), item), reverse=True) #정렬부분
    return text_list[0]

def attack(start):
    word_list = get_word(start)
    """
    if len(word_list) == 0:
        print("찾을 수 없음")
        return
    

    length = len(word_list)
    if length > 10:
        length = 5

    i = random.randrange(0, length)
    """
    message = word_list#[i]
    for i in range(1, 291357):
        if result[i] == message:
            print(i)
            break
    print(message)
    #send(message) #send함수 실행

a = input()
attack(a)