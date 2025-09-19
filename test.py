str1=str(input("enter a string: "))
let=str(input("enter a letter: "))
count=0

for i in str1:
    if i == let:
        count+=1
print(count, let+"'s")