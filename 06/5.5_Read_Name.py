'''Read_Name'''
def main():
    myfile = open('friends.txt', 'r')
    lines = myfile.readlines()
    myfile.close()
    
    names = [line.strip() for line in lines]
    
    print('\n'.join(names))

main()
