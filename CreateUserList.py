import pickle

users = {'Henry89098@gmail.com': ['Hantao_Mai',['CPSC,121,188,General','CPSC,221,191,Any']],
         'henry78987@gmail.com': ['Yi_Yang',['CPSC,121,181,General','CPSC,565,121,Any']],
         'Yaqixyz@gmail.com': ['y',['PHIL,120,99C,Any']]}

with open('users.pickle', 'wb') as handle:
    pickle.dump(users, handle, protocol=pickle.HIGHEST_PROTOCOL)