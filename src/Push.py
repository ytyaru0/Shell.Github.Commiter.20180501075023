import os.path
import pathlib
from Accounts import Accounts
class Push:
    def __init__(self):
        self.__accounts = Accounts()
    def Main(self):
        self.__IsSameRepoName()
        self.__ExistReadMe()
        self.__SelectUser()
        self.__IsRegistedUser()
        self.__OverwriteConfig()
        self.__CreateRepository()
        self.__CheckView()
        self.__AddCommitPush()


if __name__ == '__main__':
    a = Accounts()

