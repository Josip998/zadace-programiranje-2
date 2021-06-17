def brojevi(x):
    for i in range(x):
        if i%2==0:
            yield ('parni: ',i)
        if i%2!=0:
            yield ('neparni: ',i)
iteracija=iter(brojevi(20))
while True:
    try:
        print(next(iteracija))
    except:
        break
brojevi(20)
