import random

list_ = []
names = ["박시우", "채지훈", "이예원", "김민서", "임예영", "김은영", "송나린", "박건우", "최지송", "조석준", "오동언", "유지상", "최민규", "인태영", "이현민", "심예원"]
random.shuffle(names)
a = 8
member = 17
names.remove("채지훈")
list_.append("채지훈")
names.remove("김민서")
list_.append("김민서")

#print(names)
#print(list_)

for i in range(1, a):
    name1 = random.choice(names)
    list_.append(name1)
    names.remove(name1)
    name2 = random.choice(names)
    list_.append(name2)
    names.remove(name2)
    print(list_)
    
#확인

for i in range(1, member):
    print("이름을 입력하세요 : ")
    name = input()
    index_ = list_.index(name)
    if index_ % 2 == 0:
        print("당신의 마니또는 %s입니다. \n" % list_[index_ + 1])
    elif index_ % 2 != 0:
        print("당신의 마니또는 %s입니다. \n" % list_[index_ - 1])
