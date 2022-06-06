import random

kword = input('Code: ').split(' ')



filename = input('Name of file:')+'.txt'
def function(word=str()):                                      #function

    cword = word.split('.')


    with open(filename,'r') as f:
        text = f.read()
        pages = text.split('˘')

        p = int(-1)                                             #p like page
      
        while p < 119:
            p = p+1
            
            lw = int(-1)                                    #letter of word
            nw = int(0)                                    #new word id
            
            for k in range (0,801):
                lw = lw+1
                
                if pages[p][k]=='¤':
                    lw = -1
                    nw = nw+1
                
                
                if int(cword[0]) == p and int(cword[1]) == nw and int(cword[2]) == lw:    
                    return(pages[p][k])
                      
    f.close()

for i in range(len(kword)):
    print(function(kword[i]), end="")






input('\nPress enter to exit the program!')