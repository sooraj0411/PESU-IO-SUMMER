s=input("Enter string:")
flg=1
for i in s:
  if(ord('0')<ord(i)>ord('9')):
      flg=0
      break

if flg:
    print("String is numeric")
else:
    print("string is not numeric")
