import pickle

users = {'Henry89098@gmail.com': ['Hantao_Mai',['CPSC,121,999,General','CPSC,221,999,Any']],
         'yaqixyz@gmail.com': ['y',['EOSC,326,99A,General','PHIL,120,99C,Any']],
         'Yonni.luu@gmail.com': ['Yonni_Luu',['GERM,433,902,General']],
		 'james.k.1452@hotmail.com': ['tanboi',['PHYS,219,L1A,Any']]}


with open('users.pickle', 'wb') as handle:
    pickle.dump(users, handle, protocol=pickle.HIGHEST_PROTOCOL)