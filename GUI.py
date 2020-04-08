from tkinter import *
import os, re, string, random


import os, re, string, random
from tkinter import *

s = os.getcwd()


class passbag():
    def __init__(self):
        self.bag = {}
    
    def __getitem__(self, site):
        return self.bag.get(site.lower(), 'Data for site not available')

    def __setitem__(self, site, password): #problem when generating new password, ##not any more
#        if(site not in self.bag):
#            print('This site is not in the database. Setting password to the one you requested')
#            print(f'Your password for {site} is {password} ')
        self.bag[site.lower()] = password

    def __contains__(self, site):
        if(site in self.bag):
            return True
        return False


    def __delitem__(self, site):
        del self.bag[site]


#    def show_list(self):  ## Basically wanted this to spit out the whole database. It didn't make sense to have a class method for this, simply for returning it so that a button could use it.
#        res = input('WARNING!!! This will print the list of your passwords to the screen, are you sure ?').lower()
#        if(res == 'yes'):
#            print(self.bag)

#    def delete(self, site):   ## Same explanation as above, no use for a class function imo if all we do is manipulate the inner dictionary
#        res = input(f'WARNING!!! This will delete the data for the site {site}. Are you sure you want to carry on with this command ?').lower()
#        if(res=='yes'):
#            self.bag.pop(site, 'The site does not exist in the database.')
#        del()
        


        
    
        

#    def search_by_pass(self)

#print(pass_gen())
if(not os.path.exists(s+'/passhandler')):
    os.makedirs('passhandler')
if(not os.path.exists(s+'/passhandler/password_list.txt')): #meaningless really, append will anyway create new if it didn't exist in the first place. Not meaningless, just found out that I can't read when in append mode, so only append (and consequently create) if file doesn't exist in the first place
    passwords = open(os.path.join(s,'passhandler','password_list.txt'),'a') #actual program has customizable name
    passwords.close()
passwords = open(os.path.join(s,'passhandler','password_list.txt' ))
#print(os.path.join(s,'applications','password_list.txt'))
pairRegex = re.compile(r'.+:.+')
siteRegex = re.compile(r'(.+):.+')
passwordRegex = re.compile(r'.+:(.+)')
content = passwords.read()
#print(content)
pass_pot = passbag()
pair_list = pairRegex.findall(content)
for x in pair_list:
    pass_pot.bag[siteRegex.findall(x)[0]] = passwordRegex.findall(x)[0]

#print(pair_list)
#print(pass_pot.bag)
passwords.close()  
#security question time ??
#####   ALL OF THIS WAS WITHOUT TKINTER TAKING INPUTS FROM THE TERMINAL NOT VERY USER FRIENDLY   #####
#running the gui, accepting inputs and putting the right functions in the right places
#in the end, opening the file in write mode, erasing the previous stuff, and writing whatever is there in the dictionary to the file
#response =  ''  #for now without gui
#while(response != 'end'):
#    response = input('''Welcome to the PASSHANDLE.  ''')

#passwords = open(os.path.join(s,'applications','password_list.txt'), 'r' )  - closing sequence, open a clean txt file and write the dictionary to it.
#for x in pass_pot.bag:
#    passwords.write(f'{x}:{pass_pot.bag[x]}\n')
#passwords.close()





#Initial = Tk()
window = Tk()
site = Entry(window)
password = Entry(window)
#geni = Tk()   ## Window I had opened for a real time look at the dictionary object
#geni.title('dictionary display')


def enter():
#    print(site.get() in pass_pot)
    if(site.get() in pass_pot):
        warning = Tk()
        def overw():
            pass_pot[site.get()] = password.get()
            warning.destroy()
        warning.title('WARNING - passhandler')
        overwrite = Button(warning, text = 'OVERWRITE', command = overw)
        message = Label(warning, text = f'Data for this site already exists\nPassword:{pass_pot[site.get()]}.\nClick on overwrite to continue with action')
        message.pack()
        overwrite.pack()
        warning.mainloop()
        return
    pass_pot[site.get()] = password.get()
#   print(pass_pot.bag)



def pass_gen(s = 16): # default password size for good strength is 16 !
    password.delete(0, END)
    result = ''
    total = [list(string.ascii_lowercase), list(string.ascii_uppercase), list(string.digits), list(string.punctuation)]
    for i in range(s):
        add = random.choice(random.choice(total))
        result+=add+''
    password.insert(10, result)


def end():
#    print(pass_pot.bag)
    passwords = open(os.path.join(s,'passhandler','password_list.txt'), 'w' )  #- closing sequence, open a clean txt file and write the dictionary to it.
    for x in pass_pot.bag:
        passwords.write(f'{x}:{pass_pot.bag[x]}\n')
    passwords.close()
    window.destroy()


def find():
    password.delete(0, END)
    s = pass_pot[site.get()]
    password.insert(10, s)


def delete():
    delwin = Tk()
    delwin.title('Delete window')
    try:
        del pass_pot[site.get()]
        message = Label(delwin, text = 'succesfully deleted data')
        message.pack()
    except KeyError:
        message = Label(delwin, text = 'data for site wasn\'t found, please try again')
        message.pack()
    delwin.mainloop()
    



window.title('Passhandler')
title = Label(window, text = 'Welcome to passhandler.\nPress Enter to store password data or End to terminate the program.\nPress End for succesful storage of passwords')
find = Button(window, text = 'Find', command = find)
find.grid(row = 1, column = 2)
enter = Button(window, text = 'Enter', command=enter)
end = Button(window, text = 'End', command = end)
delete = Button(window, text = 'Delete', command = delete)
generate = Button(window, text = 'generate password', command = pass_gen)
generate.grid(row = 2, column = 2)
s_label = Label(window, text = 'site name (Please enter full url for perfect sync): ')
s_label.grid(row = 1, column = 0)
site.grid(row = 1, column = 1)
p_label = Label(window, text = 'password: ')
p_label.grid(row = 2, column = 0)
password.grid(row = 2, column = 1)
title.grid(row = 0, column =1)
enter.grid(row = 3, column = 1)
end.grid(row = 3, column = 0)
delete.grid(row = 3, column = 2)
#enter.grid(row=4, column = 0)
#end.grid(row = 4, column = 3)
window.mainloop()
#geni.mainloop()

#don't mix pack and grid in the same master window