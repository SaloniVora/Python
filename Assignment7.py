#Q7 WAP to accept a string from user ,replace the occurrence of first character in remaining part of string with *.('babble' : 'ba**le')


str1=input("Enter the string")
str2=str1[0]+str1[1:].replace(str1[0],"*")
print(str2)
