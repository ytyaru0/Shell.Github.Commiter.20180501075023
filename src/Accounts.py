import os.path
import pathlib
import csv
class Accounts:
    def __init__(self):
        #self.__accounts = {}
        self.__accounts = []
        self.__path_dir_this = pathlib.Path(__file__).parent
        self.__file = self.__path_dir_this / 'Accounts.csv'
        self.__Load()
    def __Load(self):
        self.__accounts.clear()
        with self.__file.open('r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.__accounts.append({
                    'user': row[0],
                    'email': row[1],
                    'pass': row[2],
                })
            #print(self.__accounts)
    @property
    def Accounts(self): return self.__accounts
    @property
    def Users(self):
        return [a['user'] for a in self.Accounts]
    #def Users(self): return self.__accounts.keys()
    def Has(self, username): return username in self.Accounts
    def SortedUsers(self, isReverse=False):
        return sorted(self.__accounts, key=lambda i: i['user'], reverse=isReverse)
    def GetEmail(self, user):
        for u in self.Accounts:
            if user == u['user']: return u['email']
    def GetPass(self, user):
        for u in self.Accounts:
            if user == u['user']: return u['pass']

if __name__ == '__main__':
    a = Accounts()
    # Accounts.py get users
    # Accounts.py get pass {user}
    # Accounts.py get email {user}
