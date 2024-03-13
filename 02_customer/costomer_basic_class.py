import json

with open ("02_customer/customer_list.json","r",encoding='UTF-8') as f:
    data = f.read()
    custlist = json.loads(data)


page = len(custlist)-1 if custlist is not None else -1
sel_page=1

from Customer_Manage_Class import customer_manage #클래스파일 불러오기

a = customer_manage(custlist,page,sel_page) #클래스호출


while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    >>>''').upper()

    if choice=="I":        
        print("고객 정보 입력")
        a.고객정보입력()
    elif choice=="C":
        print("현재 고객 정보 조회")
        a.현재고객정보조회()
    elif choice == 'P':
        print("이전 고객 정보 조회")
        a.이전고객정보조회()
    elif choice == 'N':
        print("다음 고객 정보 조회")
        a.다음고객정보조회()
    elif choice=='D':
        print("고객 정보 삭제")
        a.고객정보삭제()
    elif choice=="U": 
        print("고객 정보 수정")
        a.고객정보수정()
    elif choice=="Q":
        print("프로그램 종료")
        break
