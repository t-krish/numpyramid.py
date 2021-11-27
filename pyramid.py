
x = input('How many numbers should the pyramid be?: ')
x = int(x)
x = x + 1
y = ' ' * x
s = 0
line = 0
for i in range(1, x) :
    line = line + 1
    st1 =''
    for k in range(i,i+line):
        s = s+1
        st1 = str(st1) + ' ' + str(s)
    print(y, st1, y)
    y = ' ' * (x-i)
