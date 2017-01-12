main_lst=["enlists","google","inlets","banana" ]
print(main_lst)
srch_ele=''
srch_ele=input("enter search element: ")
print(type(srch_ele))
ct=0
flag=0
for ele in main_lst:
    ct=0
    if len(ele) == len(srch_ele):
        for ch in ele:
            if ch in srch_ele:
                 ct=ct+1
        if ct == len(srch_ele):
           print("anagram")
           flag=1
           break
if flag==0:
   print("not anagram")

