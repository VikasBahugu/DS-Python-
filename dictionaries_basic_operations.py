a = {'Vikas':12, 'vivek':{'good','bad'}, 'Swetank' : 33}
# print(a)
print("-------------------------")
# ca = a.pop('vivek','233')
# print(ca)

# print(a.get('viv'))

#deleting value using popitem returns a tuple which is stored in 2 variables.
# b = ()
# b = a.popitem()
# print(b)
#----------
# l,m = a.popitem()
# print(l,m)
#---------
# l,m = a.popitem()
# print(l,m)
# l,m = a.popitem()
# print(l,m)
# b = {'ashish':23,'akash':{'worst'},'vivek':45}
# a.update(b)
# print(a)
# c = {'A':12,'B':13}
# for key in a.values():
#     print(key)
# for value in a.keys():
#     print(value)
# for pair in a.items():
#     print(pair)

# lis = a.items()
# b = list(lis)
# print(b)

# a = ['a','b','c','d']
# b = [1,2,3]
# print(list(zip(a,b)))
# print(dict(zip(a,b)))
# print(dict(list(zip(b,a))))

# e = {'a':12, 'v':13, 'c':14, 'k':15}
# print("Before del: ",e)
# del e['a']
# print("After del: ",e)
# e.popitem()
# print(e)
# e.pop('a')
# print(e)

#===========================
# mydict = {x: x*x+4 for x in range(10)}
# print(mydict)
#=================================
# mydict = {"Vikas":12,
#           "Vivek":21,
#           "Swetank":55
# }
# for index,val in enumerate(mydict):
#     print(index,val)
#+=====================================
# mydict = {"Vikas":12,
#           "Vivek":21,
#           "Swetank":55
# }
# print(mydict.get("Vikas"))
# mydict.update({"Vikas":"Vikas"})
# print(mydict)
#-----------------------------------------

# dicti = ["Swetank","Ghosh","Rajiv"]
# dicts = dict(enumerate(dicti))
# print(dicts)
# for i in range(0,len(dicts)):
#     print(i," -> ",dicts[i],)
# #-------------------------

# # from _collections import defaultdict
#
# dict = _collections.OrderedDict(Vikas=3,Swetank=4)
# print(dict.keys())
#-------------------------
# import pandas
# emp_details = {'Employee': {'Dave': {'ID': '001',
#                                      'Salary': 2000,
#                                      'Designation':'Python Developer'},
#                             'Ava': {'ID':'002',
#                                     'Salary': 2300,
#                                     'Designation': 'Java Developer'},
#                             'Joe': {'ID': '003',
#                                     'Salary': 1843,
#                                     'Designation': 'Hadoop Developer'}}}
# df = pandas.DataFrame(emp_details['Employee'])
# print(df)