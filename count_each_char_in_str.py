'''
    ip='f46feLK9y56u#@&56hIjbn6KJhA'
    op=Lower Vowels: 2 Upper Vowels: 2 Upper conso: 4 Lower cons: 8 Digits: 8 special: 3
'''
def count_characters(s):
    if len(s)==0:
        return
    uv=0
    lv=0
    uc=0
    lc=0
    digits=0
    special=0
    for i in s:
        if i in"AEIOU":
            uv+=1
        elif i in "aeiou":
            lv+=1
        elif i>='a' and i<='z':
            lc+=1
        elif i>'A' and i<'Z':
            uc+=1
        elif i>='0' and i<='9':
            digits+=1
        else: #or use elif not i.isalnum(): ->isalnum() reads only numbers and alphabets...
            special+=1
    print("Lower Vowels:",lv,"Upper Vowels:",uv,"Upper conso:",uc,"Lower cons:",lc,"Digits:",digits,"special:",special)
s=input("Enter the string:")
count_characters(s)