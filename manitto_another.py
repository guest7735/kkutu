import random

list_ = []
names = ["박시우", "채지훈", "이예원", "김민서", "임예영", "김은영", "송나린", "박건우", "최지송", "조석준", "오동언", "유지상", "최민규", "인태영", "이현민", "심예원"]
random.shuffle(names)
a = 8
member = 15
names.remove("김민서")
list_.append("김민서")
names.remove("채지훈")
list_.append("채지훈")

#print(names)
#print(list_)

for i in range(1, member):
    name1 = random.choice(names)
    list_.append(name1)
    names.remove(name1)
    #print(list_)

#확인
list_.remove("채지훈")
list_.append("채지훈")
#print(list_)

i = 0
while i < 16:
    print("이름을 입력하세요 : ")
    name = input()
    if not name in list_:
        print("없는 이름입니다. 다시 입력해주세요\n\n")
        continue
    index_ = list_.index(name)
    if index_ == 15:
        print("당신의 마니또는 %s입니다. \n\n" % list_[0])
        i+=1    
    else:
        print("당신의 마니또는 %s입니다. \n\n" % list_[index_ + 1])
        i+=1

#print(list_)