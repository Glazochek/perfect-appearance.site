
for i in range(0, 1000):
    x = '1'*10+'2'*i
    while '21' in x:
        x = x.replace('21', '5')
    if sum(map(int, list(x))) == 34:
        print(i)

