#Q3 WAP to accept a string from the user and accept start and end index from user and display the result of the string.


str1=str(input("Enter a string"))
start=int(input("Enter start index"))
end=int(input("Enter end index"))
print("String starting from",start,"index and ending at",end,"index is :",str1[start:end])
