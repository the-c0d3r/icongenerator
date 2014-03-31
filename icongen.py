import os

def main():
    global content
    logo()
    try:
        
        content = open('icon.txt').readlines()
        i = 1
        for x in content:
            print "%d : %s" % (i,x[:x.find('.')])
            i+=1
            
        getname()
        
    except IOError:
        print "[!] Error, you need icon.txt to work!\n[!] Download it from github"
    except KeyboardInterrupt:
        print "[!] Ctrl + C detected."
        print "[!] Program Terminated!"

def logo():
    print'''
( ========================= )
( ==== ICON GENERATOR ===== )
( ========================= )
'''
    
def getname(): # Get Number input
    try:
        cmd = raw_input("Enter Number : ")
        fnames = [i[:i.find('.')] for i in content]
        if cmd != '' and cmd != 'quit' and cmd != 'exit':
            create(content[int(cmd)-1])
            getname()
        else:
            exit()
    except KeyboardInterrupt:
        print "[!] Ctrl + C detected."
        print "[!] Program Terminated!"
        
def create(name):
    os.system('mkdir folder')
    os.system(('ren "folder" "%s"' % name))
    print "[%s] shortcut created!" % name[:name.index('.')]

if __name__ == '__main__':
    main()
