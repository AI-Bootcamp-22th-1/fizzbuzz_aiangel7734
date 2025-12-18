for i in range(1, 31+1):
    if i % 3 == 0 or i % 6 == 0 or i % 15 == 0:
        print('fizz'*(i%3==0) + 'buzz'*(i%6==0) + 'fizzbuzz'*(i%15==0))
    else:
        print(i)
