seconds=int(input("Enter Seconds:- "))
h=0
m=0
if seconds>=3600:
    h=seconds//3600
    seconds=seconds%3600
if seconds>=60:
    m=seconds//60
    seconds=seconds%60
print(f"{h}Hr:{m}Mn:{seconds}Sec")