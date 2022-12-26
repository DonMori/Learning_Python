cont_fizzbuzz = 0
cont_fizz = 0
cont_buzz = 0

for i in range(1, 101, 1):
    if i%3 == 0 and i%5 == 0:
        cont_fizzbuzz+=1
        print(i, 'FizzBuzz')
    if i%5 == 0:
        cont_buzz+=1
        print(i, 'Buzz')
    if i%3 == 0:
        cont_fizz+=1
        print(i, 'Fizz')
    if i%3 != 0 and i%5 != 0:
        print(i)
    


print(f'\n\tResult Table\nCont of Fizz : {cont_fizz}\nCont of Buzz : {cont_buzz}\nCont of FizzBuzz : {cont_fizzbuzz}')