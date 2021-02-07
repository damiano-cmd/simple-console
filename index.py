import requests
from bs4 import BeautifulSoup as soup
import pprint
import json
from os.path import isdir
from os import listdir, system, mkdir, remove
from shutil import rmtree
from re import split as spl

print("Type help for guidance")
cd = ''
help_text = [
    'Type cd to see the selected directory ',
    'To select a directory type cd #path ',
    'To add to the directory cd #.\path',
    'Type ls to listhe contens of the current directory ',
    'cls is to clear the screen',
    'quit is to exist the program',
    'api is to interact with an online api / api url:[url_to_the_api] [is it a get, post, put or delete request] doc:[file_name you want to save the response]',
    'type of api requests are post:[data_to_send], delete, get, put:[data_to_send]',
    'api example: api url:https://www.api.com/login post:{"email":"example@gmail.com","password":"1234"}',
    'make makes a file or a directory in the selected directory example: make dir:[directory_name] file:[file_name.file_extension',
    'delete deletes file or directory in the selected'
]

while 1:
    command = input("> ")
    command = command.split(" ")

    if 'help' == command[0]:
        for i in help_text:
            print(i)

    if 'cd' == command[0]:
        if len(command) > 1:
            direct = command[1]
            if 'back' == direct:
                bck = cd.split('\\')
                del bck[-1]
                newcd = ''
                for i in bck:
                    newcd = newcd + i + '\\'
                cd = newcd
                print('The Directory is ' + cd)
            else:
                if '.' == direct[0]:
                    direct = direct.replace('.', cd)
                if isdir(direct):
                    cd = direct
                    print('Curent dir ' + cd)
                else:
                    print('Directory dose not exist!!!')
        else:
            print(cd)

    if 'ls' == command[0]:
        try:
            for i in listdir(cd):
                print(i)
        except:
            print('Cant list the directory!!!')
    
    if 'cls' == command[0]:
        system('cls')
    
    if 'api' == command[0]:
        for i in command:
            if 'url:' in i:
                y = i.split('url:')
                if 'get' in command:
                    try:
                        html = requests.get(y[1])
                        pprint.pprint(html.json())
                    except:
                        print('Some thing went wrong!!!!')
                for g in command:
                    if 'post:' in g:
                        try:
                            h = g.split('post:')
                            jsond = json.loads(str(h[1]))
                            html = requests.post(y[1], data=jsond)
                            pprint.pprint(html.json())
                        except:
                            print('Some thing went wrong!!!!')
                    if 'put:' in g:
                        try:
                            h = g.split('put:')
                            jsond = json.loads(str(h[1]))
                            html = requests.put(y[1], data=jsond)
                            pprint.pprint(html.json())
                        except:
                            print('Some thing went wrong!!!!')
                if 'delete' in command:
                    try:
                        delete = requests.delete(y[1])
                        pprint.pprint(delete)
                    except:
                        print('Cant delete!!!!')
                for x in command:
                    if 'doc:' in x:
                        m = x.split('doc:')
                        with open(cd + '\\' + m[1] + '.json', 'w') as f:
                            f.write(str(html.json()).replace("'", '"'))
    
    if 'make' == command[0]:
        if cd == '':
            print('select a directory with cd')
        else:
            for i in command:
                if 'dir:' in i:
                    y = i.split('dir:')
                    mkdir(cd + '\\' + y[1])
                if 'file:' in i:
                    y = i.split('file:')
                    with open(cd + '\\' + y[1], 'a') as f:
                        f.write('')
    
    if 'delete' == command[0]:
        if len(command) == 1:
            print('First select the directory with cd')
        elif isdir(cd):
            try:
                if '.' in command[1]:
                    remove(cd + '\\' + command[1])
                else:
                    rmtree(cd + '\\' + command[1])
            except:
                print('Cant remove file')
        else:
            print('The file dose not exist!!!')
    
    if 'quit' in command:
        if len(command) > 1:
            if command[1] == 'y':
                break
        else:
            conformation = input("Do you want to quit(Y/N) > ")
            if conformation == 'Y' or 'y' or 'Yes' or 'yes':
                break
            else:
                pass