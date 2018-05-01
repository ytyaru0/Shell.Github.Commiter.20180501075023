import os.path
import pathlib
from Accounts import Accounts
class UserSelect:
    def __init__(self):
        self.__accounts = Accounts()
    def Main(self):
        #self.__IsSameRepoName()
        #self.__ExistReadMe()
        self.__SelectUser()
        self.__IsRegistedUser()
        self.__OverwriteConfig()
        self.__CreateRepository()
        self.__CheckView()
        self.__AddCommitPush()
    def IsRegistedUser(self, username):
        return self.__accounts.Has(username)
    def SelectUser(self):
        self.__accounts.SortUser()
        answer = ''
        while '' == answer:
            print('ユーザを選択してください。')
            for i, item in enumerate(self.__accounts.Accounts):
                print('{}:{}', i, self.__accounts.Accounts[i]['user'])
            answer = input()
            try: return self.__accounts.Accounts[int(answer)]['user']
            except:
                print('エラーです。入力値を見なおしてください。')
                continue

if __name__ == '__main__':
    a = Accounts()

