def prime_number(number):
    counter = 0

    #for i in range(1, number + 1):
        #if i == 1 or i == number:
            #continue
        #if number % i == 0:
            #counter += 1
    #if number == 1:
        #return False
    #if counter == 0:
        #return True
    #else:
        #return False

    for i in range (1, number + 1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            counter = counter + 1
    if number == 1:
       return False    
    if counter == 0:
        return True
    else:
        return False

def run():
    number = int(input('Write a number: '))
    if prime_number(number) == True:
        print (str(number), 'is a prime number')
    else:
        print (str(number), 'is not a prime number')

if __name__ == '__main__':
    run()