import sys
from Accounts import Accounts

def ErrorMessage():
    print('引数エラー。: {}'.format(sys.argv))
    print('以下のいずれかのパターンのみ受け付けます。')
    #print('$ python Accounts.py ...')
    #print('                     exist {user}')
    #print('                     get users')
    #print('                     get pass {user}')
    #print('                     get email {user}')
    print('$ python Accounts.py exist {user}')
    print('$ python Accounts.py get users')
    print('$ python Accounts.py get pass {user}')
    print('$ python Accounts.py get email {user}')
    sys.exit(1)

if __name__ == '__main__':
    a = Accounts()
    if sys.argv[1] == 'exist' and 1 < len(sys.argv): print(a.Has(sys.argv[2]))
    elif sys.argv[1] == 'get' and sys.argv[2] == 'users':
        for u in a.SortedUsers(): print(u['user'])
    elif sys.argv[1] == 'get' and sys.argv[2] == 'email' and 3 < len(sys.argv): print(a.GetEmail(sys.argv[3]))
    elif sys.argv[1] == 'get' and sys.argv[2] == 'pass' and 3 < len(sys.argv): print(a.GetPass(sys.argv[3]))
    else: ErrorMessage();
