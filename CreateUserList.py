import pickle

users = {'Hantao_Mai': ['hantaom@gmail.com',['CPSC,121,101,General','CPSC,221,101,Any']],
         'Yi_Yang': ['yaqixyz@gmail.com',['CPSC,121,101,General','CPSC,565,121,Any']]}

with open('users.pickle', 'wb') as handle:
    pickle.dump(users, handle, protocol=pickle.HIGHEST_PROTOCOL)