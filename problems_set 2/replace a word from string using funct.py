
def split_remove(string,word ):
    nwestr = string.replace(word," ")
    nwestr=nwestr.strip()
    nwestr=nwestr.replace("  ","")
    return nwestr


str =input("Enter post here : ")
_word =input("Enter  word to remove")
namt =split_remove(str,_word)
print(namt)







# print(str)
# print(str.replace("Ali"," "))
# nstring = str.replace("Ali"," ")
# print(nstring.strip())