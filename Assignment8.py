#Q8  WAP to accept 2 strings from user and jumble them (swap first 2 characters of both strings).{'dog','dinner' o/p 'dig','donner'

str1=input("Enter string 1")
str2=input("Enter string 2")
str3=str2[:2]+str1[2:]
str4=str1[:2]+str2[2:]
print(str3,str4)
