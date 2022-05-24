users_data = {'Username': 'Shrek', 'age': 23, 'tweet': ['lakers are shit', 'lebron is the GOAT of this game'],
              'verify': False,
              'Username': 'holycr', 'age': 33, 'tweet': ['lakers are shit', 'lebron is the GOAT of this game'],
              'verify': True,
              'Username': 'Jojo', 'age': 18, 'verify': False,
              'Username': 'sundirection', 'age': 42, 'tweet': ['chelsea fail to beat united a their woarst', 'GGMU'],
              'verify': True,
              'Username': 'Avii', 'age': 25, 'tweet': ['Dogs are out there fucking your crush lmao', 'Ass so fat'],
              'verify': False,
              'Username': 'Asiwaju', 'age': 21, 'tweet': ['Crypto make life better', 'got mils at 21, levels!'],
              'verify': True,
              'Username': 'Kvngtw', 'age': 28, 'verify': False,
              'Username': 'Stormjrn', 'age': 22, 'tweet': ['End war', 'They deserve better'],
              'verify': False,
              'Username': 'Greenwood', 'age': 20, 'tweet': ['I AM BACK!'],
              'verify': True,
              'Username': 'Livingbot', 'age': 21, 'verify': False,

              }
# a1 = [user['Username']for user in users_data if user['verify']]
# print(a1)
a2 =map(lambda x:x['Username'], filter(lambda y:y['verify'], users_data))
print(list(a2) )