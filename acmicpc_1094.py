Xcm = format(int(input()), 'b')

cnt = 0
for one in str(Xcm):
    if int(one):
        cnt += 1
        
print(cnt)