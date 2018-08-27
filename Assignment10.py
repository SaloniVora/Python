
#Q10 WAP to accept a string from user assume that it contains not followed by 'bad'.

str1=input("Enter a string ")
str2=str1.split("not")
str3="".join(str2)
str4=str3.replace("bad","good")
print(str4)
