#Q9 WAP to accept 2 strings from user and check if second string is right rotation of first.('manager','germana' return true)


str1=input("String 1")
str2=input("String 2")
loc=str1.find(str2[0])
print(str1[loc:] in str2 and str1[:loc] in str2)
