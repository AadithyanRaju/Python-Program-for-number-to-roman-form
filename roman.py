#simple logic conversion
x=int(input())
r=''
while x>10000:
    r+="H"
    x-=10000
while x>=9000:
    r+="MH"
    x-=9000
while x>=5000:
    r+='G'
    x-=5000
while x>=4000:
    r+='MG'
    x-=4000
while x>=1000:
    r+='M'
    x-=1000
while x>=900:
    r+='CM'
    x-=900
while x>=500:
    r+='D'
    x-=500
while x>=400:
    r+='CD'
    x-=400
while x>=100:
    r+='C'
    x-=100
while x>=90:
    r+='XC'
    x-=90
while x>=50:
    r+='L'
    x-=50
while x>=40:
    r+='XL'
    x-=40
while x>=10:
    r+='X'
    x-=10
while x==9:
    r+='IX'
    x-=9
while x>=5:
    r+='V'
    x-=5
while x==4:
    r+='IV'
    x-=4
while x>0:
    r+='I'
    x-=1
print(r)