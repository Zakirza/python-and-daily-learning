string=str(input())
str_count={}
count=0

for char in string:
    if char in str_count:
        str_count[char]+=1
    else:
        str_count[char]=1

for key in sorted(str_count):
    if str_count[key]%2!=0:
        count+=1

if count>1:
    print("NO SOLUTION")
else:
    left=[]
    middle=""
    for key in sorted(str_count):
        if str_count[key]%2==0:
            left.append(key*(str_count[key]//2))
        else:
            left.append(key*(str_count[key]//2))
            middle=key*1
    right=left[::-1]
    print("".join(left)+middle+"".join(right))
    
    