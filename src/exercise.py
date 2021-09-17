def main():
    #write your code below this line
    num = int(input('Give points [0-100]:'))
    
    if num < 0:
        print('impossible')
    elif num <= 49:
        print('failed')
    elif num <= 59:
        print('1')
    elif num <= 69:
        print('2')
    elif num <= 79:
        print('3')
    elif num <= 89:
        print('4')
    elif num <= 100:
        print('5')
    else:
        print('incredible!')

if __name__ == '__main__':
    main()
