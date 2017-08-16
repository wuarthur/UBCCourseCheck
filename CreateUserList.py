import pickle

users = {'Henry89098@gmail.com': ['Hantao_Mai',['CPSC,121,101,General','CPSC,221,101,Any']],
         'henry78987@gmail.com': ['Yi_Yang',['CPSC,121,101,General','CPSC,565,121,Any']],
         'yaqixyz@gmail.com': ['y',['EOSC,326,99A,General','PHIL,120,99C,Any']],
         'Yonni.luu@gmail.com': ['Yonni_Luu',['GERM,433,902,General']],
		 'james.k.1452@hotmail.com': ['tanboi',['PHYS,219,L1A,Any']]}


with open('users.pickle', 'wb') as handle:
    pickle.dump(users, handle, protocol=pickle.HIGHEST_PROTOCOL)