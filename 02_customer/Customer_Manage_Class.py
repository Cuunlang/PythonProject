import re
from datetime import datetime
import json

'''
costomer_basic_class.py에 필요한
class파일
'''


class customer_manage():

    def __init__(self,custlist,page,sel_page):
        self.custlist = custlist
        self.page = page
        self.sel_page = sel_page

    

    def 고객정보입력(self):
        I_progress = 0
        while True:
                if I_progress == 0:
                    name = input('이름을 입력해 주세요:')
                    I_progress += 1

                elif I_progress == 1:
                    gender = input('성별을 입력해 주세요:')
                    if gender not in ['M', 'F', 'm', 'f']:
                        print("잘못된 입력입니다. 다시입력해주세요")
                    else: 
                        gender = gender.upper()
                        I_progress +=1
                elif I_progress == 2:
                    email = input('이메일을 입력해 주세요:')
                    email_check=re.compile('^[a-z][a-z0-9]{4,20}@[a-z]{2,20}.[a-z]{2,10}')
                    if email_check.search(email) == None:
                        print("이메일 형식이 올바르지 않습니다! 다시입력해주세요.")
                    elif self.page != -1:
                        for j in self.custlist:
                            if email == j['email']:
                                print("이미 존재하는 이메일 입니다.")
                                I_progress -= 1
                                break
                        I_progress += 1
                    else:
                        I_progress +=1
                elif I_progress == 3:
                    birthyear = int(input('출생년도를 입력해주세요(4자리숫자):'))
                    if birthyear <= datetime.now().year:
                        I_progress +=1
                    else:
                        print(f"출생년도는{datetime.now().year}년도 이하의 4자리숫자로 입력해주세요!")
                elif I_progress == 4:
                    self.custlist.append({"name":name,"gender":gender,"email":email,"birthyear":birthyear})
                    self.page +=1
                    print(f"고객정보가{self.page+1}에 저장되었습니다. ")
                    self.고객정보저장()
                    break


    def 현재고객정보조회(self):
        if self.page == -1 : print("현재 고객정보가 없습니다.")
        else:
            print(f"[고객정보 입니다. page {self.sel_page}/{self.page+1}]\n","="*(len(self.custlist[self.sel_page-1]['email'])+10),"\n")
            print(f"이름:{self.custlist[self.sel_page-1]['name']}\n성별:{self.custlist[self.sel_page-1]['gender']}\n이메일:{self.custlist[self.sel_page-1]['email']}\n출생년도:{self.custlist[self.sel_page-1]['birthyear']}\n","="*(len(self.custlist[self.sel_page-1]['email'])+10))

    def 이전고객정보조회(self):
        if self.page == -1 : print("현재 고객정보가 없습니다.")
        else:
            if self.sel_page - 1 == 0: print("이미 첫번째 페이지 입니다.")
            else:
                self.sel_page -= 1
                print(f"[고객정보 입니다. page {self.sel_page}/{self.page+1}]\n","="*(len(self.custlist[self.sel_page-1]['email'])+10),"\n")
                print(f"이름:{self.custlist[self.sel_page-1]['name']}\n성별:{self.custlist[self.sel_page-1]['gender']}\n이메일:{self.custlist[self.sel_page-1]['email']}\n출생년도:{self.custlist[self.sel_page-1]['birthyear']}\n","="*(len(self.custlist[self.sel_page-1]['email'])+10))

    def 다음고객정보조회(self):
        if self.page == -1 : print("현재 고객정보가 없습니다.")
        else:
            if self.sel_page + 1 > self.page+1: print("마지막 페이지 입니다.")
            else:
                self.sel_page += 1
                print(f"[고객정보 입니다. page {self.sel_page}/{self.page+1}]\n","="*(len(self.custlist[self.sel_page-1]['email'])+10),"\n")
                print(f"이름:{self.custlist[self.sel_page-1]['name']}\n성별:{self.custlist[self.sel_page-1]['gender']}\n이메일:{self.custlist[self.sel_page-1]['email']}\n출생년도:{self.custlist[self.sel_page-1]['birthyear']}\n","="*(len(self.custlist[self.sel_page-1]['email'])+10))

    def 고객정보삭제(self):
        del_email = input('삭제할 이메일을 입력해 주세요:')
        if self.page == -1 : print("삭제할 고객정보가 없습니다.")
        else:
            delok = 0
            for i in range(self.page+1): 
                if del_email == self.custlist[i]['email']:
                    del self.custlist[i]
                    delok = 1
                    break
            if delok == 1 :
                print("삭제가 완료되었습니다.")
                self.page -= 1
                self.고객정보저장()
                if self.sel_page > self.page+1 : self.sel_page = self.page + 1
            else: print("입력된 정보와 일치하는 정보가 없습니다.")

    def 고객정보수정(self):
        idx = -1
        while True:

            cust_email = input('수정할 고객 정보의 이메일을 입력하세요(수정창을 나갈려면\"quit\"입력):')
            if cust_email == 'quit':
                self.고객정보저장()
                break
                
            for i in range(self.page+1):
                if cust_email == self.custlist[i]['email']:
                    idx = i
                    break
            if idx == -1 :print("입력된 이메일과 일치하는 고객정보가 없습니다.")
            else: 

                choice_key = int(input('''수정할 정보를 선택해 주세요.(숫자입력)
                                1. 이름
                                2. 성별
                                3. 이메일
                                4. 출생년도
                '''))
                if choice_key == 1:
                    self.custlist[idx]['name'] = input('새 이름을 입력해 주세요:')
                    print("이름이 수정되었습니다!")
                elif choice_key == 2:
                    while True:
                        regender = input('수정할 성별을 입력해 주세요:')
                        if regender not in ['M', 'F', 'm', 'f']:
                            print("잘못된 입력입니다. 다시입력해주세요")
                        else:
                            self.custlist[idx]['gender'] = regender
                            break
                    print(f"{self.custlist[idx]['name']}님의 성별이 수정되었습니다.")
                elif choice_key == 3:
                    while True:
                        reemail = input('이메일을 입력해 주세요:')
                        if re.search('@',reemail) == None:
                            print("이메일 형식이 올바르지 않습니다! 다시입력해주세요.")
                        else:
                            self.custlist[idx]['email'] = reemail
                            break
                    print(f"{self.custlist[idx]['name']}님의 이메일이 수정되었습니다.")
                elif choice_key == 4:
                    while True:
                        rebirthyear = input('출생년도를 입력해주세요:')
                        if len(str(rebirthyear)) != 4:
                            print("출생년도는 4자리로 입력해주세요!")
                        else:
                            self.custlist[idx]['birthyear'] = rebirthyear
                            break
                    print(f"{self.custlist[idx]['name']}님의 출생년도가 수정되었습니다.")
                else:
                    print("잘못된 입력입니다.")

    def 고객정보저장(self):
        with open("02_customer/customer_list.json","w",encoding='UTF-8') as cs_list:
            #cs_list.write(str(self.custlist))
            json.dump(self.custlist,cs_list)

