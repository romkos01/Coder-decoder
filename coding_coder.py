import random

kword = input('Word: ')
    
    
    
filename = input('Name of file:')+'.txt'
def function(word=str()):


    c = word
    counter = int(0)

    with open(filename,'r') as f:
        text = f.read()
        pages = text.split('˘')

        p = int(-1)                                             #p like page
      
        while p < 118:
            p = p+1
                    
            for k in range (0,801):
                #print(c + ' ' + pages[p][k] + ' ' + str(p) +' ' + str(k))
                if pages[p][k] == c:
                    counter = counter+1
                    #print(c + ' ' + pages[p][k] + ' ' + str(p) +' ' + str(k))

    f.close()

    value = random.randint(0,counter-1)
    counter = 0

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
                
                if pages[p][k] == c:
                    counter = counter+1
                    
                    if counter == value:
                        return(str(p) + '.' + str(nw) + '.' + str(lw))
    f.close()




for i in range(len(kword)):
    print(function(kword[i]), end=" ")


input('\nPress enter to exit the program!')