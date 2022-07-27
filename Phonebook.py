#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
import re
import requests
from bs4 import BeautifulSoup


root = tk.Tk()
root.geometry('450x300')
root.title('main')
root.configure(bg='#262126')
root.minsize(450, 325)
root.maxsize(450, 325)
framea = tk.Frame(root)
framea.pack(side='left', anchor='nw', fill='y')
frameb = tk.Frame(root)
frameb.pack(side='left', anchor='nw')
global yh
yh = []

# root Button_functions
def newcontact():
    newcontact = tk.Toplevel(root)
    newcontact.title('New Contact')
    newcontact.configure(bg='#cccccc')
    
    # Lables
    labelname = tk.Label(newcontact, text="First Name ", bg='black', fg='grey')
    labelname.grid(column=0, row=0)
    labellast = tk.Label(newcontact, text='Last Name ', bg='black', fg='grey')
    labellast.grid(column=0, row=1)
    labelemail = tk.Label(newcontact, text='Email          ', bg='black', fg='grey')
    labelemail.grid(column=0, row=2)
    labelnumber = tk.Label(newcontact, text='Number     ', bg='black', fg='grey')
    labelnumber.grid(column=0, row=3)
    
    # Entries
    entryfirst, entrylast, entryemail, entrynumber = tk.Entry(newcontact, bg='#cccccc'), tk.Entry(newcontact, bg='#cccccc'), tk.Entry(newcontact, bg='#cccccc'), tk.Entry(newcontact, bg='#cccccc')
    entryfirst.grid(column=1, row=0)
    entrylast.grid(column=1, row=1)
    entryemail.grid(column=1, row=2)
    entrynumber.grid(column=1, row=3)
    
    # newcontact_Button_functions
    def clicked():
        global first, last, email, number
        
        first=entryfirst.get()
        first=(first[0].upper())+first[1:]
        last=entrylast.get()
        last=(last[0].upper())+last[1:]
        email=entryemail.get()
        number=entrynumber.get()
    
        checker(email)
        if check == False:
            newcontact.destroy()
            
            f = open('Untitled.txt','a')
            if email == '':
                f.write('{}) firstname: {} lastname: {}  number: {}\n'.format(first[0], first, last, number))
                f.close()
                sort_first()
            elif number == '':
                f.write('{}) firstname: {} lastname: {} email: {}\n'.format(first[0], first, last, email))
                f.close()
                sort_first()
            else:    
                f.write('{}) firstname: {} lastname: {} email: {}   number: {}\n'.format(first[0], first, last, email, number))
                f.close()
                sort_first()
        else:
            warning = tk.Label(newcontact, text='Please enter valid email!')
            warning.grid(column=1, row=4)
                                                            
                                                                
    # new_contact_Button                                     
    button = tk.Button(newcontact, text="Confirm", fg="red", bg="orange", highlightbackground='#cccccc', command=clicked)
    button.grid(column=1, row=5)
    
    def checker(a):
        global check
        check = True
        b = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        for i in range(len(a)):
            if a[i] == '@':
                for j in a[0:i]:
                    if j not in b:
                        return 
                        
                for u in range(i+1, len(a)):
                    if a[u] == '.':
                        for t in a[i+1:u]:
                            if t not in b:
        
                                return 
                        for q in a[u+1:len(a)]:
                            if q not in b:
            
                                return 
            elif '@' not in a or '.' not in a:
                return
        check = False
        return 
    
    
    
    
    
    newcontact.mainloop()

def allcontacts(): 
    
    allcontacts = tk.Toplevel(root)
    allcontacts.title('Contact list')
    allcontacts.geometry('735x700')
    frram = tk.Frame(allcontacts)
    frram.pack(side='top', fill='x')
    frram2 = tk.Frame(allcontacts)
    frram2.pack(side='top', fill='both')
    var = tk.IntVar()
    f = open('Untitled.txt', 'r')
    chars = f.readlines()
    f.close()
    for i in range(len(chars)):
        chars[i] = chars[i][0]
    if chars == sorted(chars):
        var.set(1)
    else:
        var.set(2)
    
    
    def edit(selected):
        hh = ''
        global linetext2
        if buttons[selected]['text'] == '\u270E Edit':
            buttons[selected]['text'] = '\u2714 confirm'
            text[selected].configure(state='normal')
            linetext2 = text[selected].get('1.0', 'end-1c')
        else:
            buttons[selected]['text'] = '\u270E Edit'
            text[selected].configure(state='disabled')
            if text[selected].get('1.0', 'end-1c') != labeltext_list[selected]:
                linetext = text[selected].get('1.0', 'end-1c')
                a = re.search('firstname: ', list1[selected])
                b = re.search(' ', linetext)
                c = re.search(' ', linetext[b.start()+1:])
                d = re.search('lastname: ', list1[selected])
                e = re.search('email: ', list1[selected])
                f = re.search('number: ', list1[selected])
                g = re.search('email: ', linetext)
                h = re.search('number: ', linetext)
                if 'email:' in linetext and 'number:' in linetext:
                    list1[selected] = list1[selected][:a.end()]+ linetext[:b.start()+1] + list1[selected][d.start():d.end()-1] +\
                    linetext[b.start():c.start()+b.start()+1] + list1[selected][e.start()-1:e.end()-1] + linetext[g.end()-1:h.start()] + linetext[h.start():]
                elif 'number:' not in linetext and 'email:' in linetext:
                    list1[selected] = list1[selected][:a.end()]+ linetext[:b.start()+1] + list1[selected][d.start():d.end()-1] +\
                    linetext[b.start():c.start()+b.start()+1] + list1[selected][e.start()-1:e.end()-1] + linetext[g.end()-1:]
                    def gotit():
                        text[selected].configure(state='normal')
                        text[selected].delete('1.0', 'end')
                        text[selected].insert('1.0', linetext2)
                        text[selected].configure(state='disabled')
                        warninboy.destroy()
                    warninboy = tk.Toplevel(allcontacts)
                    warninboy.title('Warning!')
                    warninglabel2 = tk.Label(warninboy, text='Every contact must at least have an email!')
                    warninglabel2.pack()
                    understoodbutton = tk.Button(warninboy, text='Confirm', command=gotit)
                    understoodbutton.pack()
                    
                    warninboy.mainloop()
            for v in list1:
                hh += v
            f = open('Untitled.txt', 'w')
            f.write(hh)
            f.close()
    def delete(selected):
        def yes1(selected):
            def sfg(selected):
                text[selected].grid_forget()
                dismiss.grid_forget()
                buttons[selected].grid_forget()
                deletes[selected].grid_forget()
            hh = ''
            text[selected].configure(state='normal')
            z = text[selected].get('1.0', 'end-1c')
            text[selected].delete('1.0', 'end')
            text[selected].insert('1.0', 'Contact deleted sucessfully.')
            text[selected].configure(state='disabled')
            row = buttons[selected].grid_info()['row']
            column = buttons[selected].grid_info()['column']
            deletes[selected].grid_forget()
            buttons[selected].grid_forget()
            dismiss = tk.Button(frram2, text='Dismiss', command=lambda : sfg(selected))
            dismiss.grid(column=column, row=row)
            dismiss_group.append(dismiss)
            warning.destroy()
            s = re.search(' ', z)
            o = re.search(' ', z[s.start():])
            p = re.search('email: ', z)
            r = re.search(' ', z[p.end():])
            for i in range(len(list1)):
                if z[:s.start()] in list1[i]:
                    if z[s.start():o.start()] in list1[i]:
                        if z[p.end():r.start()] in list1[i]:
                            del list1[i]
                            break
                        

            for v in list1:
                hh += v
            f = open('Untitled.txt', 'w')
            f.write(hh)
            f.close()
        warning = tk.Toplevel(allcontacts)
        warning.title('Warning!')
        warning.geometry('300x50')
        frame1 = tk.Frame(warning)
        frame1.pack()
        frame2 = tk.Frame(warning)
        frame2.pack()
        warninglabel = tk.Label(frame1, text='Are you sure you want to delete this contact?')
        warninglabel.pack(side='bottom')
        yes = tk.Button(frame2, text='yes', command=lambda aa=selected: yes1(aa))
        yes.pack(side='left')
        no = tk.Button(frame2, text='no', command=lambda : warning.destroy())
        no.pack(side='left')
        
        
                

    global labeltext_list, list1, text, buttons, deletes, dismiss_group
    full_name, labeltext, hh='', '', ''
    full_name_list, labeltext_list, buttons, text, deletes, dismiss_group=[], [], [], [], [], []
    pp = -1
    lenth = 0
    f = open('Untitled.txt')
    list1 = f.readlines()
    f.close()
    for l, k in enumerate(list1):
        for i, j in enumerate(k[14:]):
            if j == ' ':
                full_name += (k[14:i+14] + ' ')
                labeltext += (k[14:i+14] + ' ')
                for o, w in enumerate(k[i+15:]):
                    if w == ' ':
                        for y, z in enumerate(k[o+i+16:]):
                            if z == ' ':
                                full_name += k[o+i+16:o+i+y+16]
                                labeltext += k[o+i+16:]
                                labeltext_list.append(labeltext)
                                full_name_list.append(full_name)
                                if len(full_name_list) > 1:
                                    for yummy in range(len(full_name_list)):
                                        if len(full_name_list[yummy]) > lenth:
                                            lenth = len(full_name_list[yummy])
                               
                                pp += 1
                                full_name = ''
                                labeltext = ''
                                
                                if pp == l :
                                    break
                        break
                break
    
    for sa in range(len(labeltext_list)):
        for k, j in enumerate(labeltext_list[sa]):
            if 'email' not in labeltext_list[sa]:
                if j == ':':
                    labeltext_list[sa] = labeltext_list[sa][:k-6]+ ((lenth - len(labeltext_list[sa][:k-6])+1) * ' ') + labeltext_list[sa][k-6:]
                    break
            else:
                if j == ':':
                    labeltext_list[sa] = labeltext_list[sa][:k-5]+ ((lenth - len(labeltext_list[sa][:k-5])+1) * ' ') + labeltext_list[sa][k-5:]
                    break
    global mgh
    mgh = 0
    
    def sort_tmp():
        global text, buttons, deletes, labeltext_list, dismiss_group, list1
        full_name, labeltext, hh = '', '', ''
        labeltext_list, full_name_list = [], []
        if var.get() == 1:
            sort_first()
        else:
            sort_last()

        for i in range(len(dismiss_group)):
            dismiss_group[i].grid_forget()
        for i in range(len(text)):
                text[i].grid_forget()
                buttons[i].grid_forget()
                deletes[i].grid_forget()
        for i in range(len(text)):
            text.pop()
            buttons.pop()
            deletes.pop()
        pp = -1
        lenth = 0
        f = open('Untitled.txt')
        list1 = f.readlines()
        f.close()
        for l, k in enumerate(list1):
            for i, j in enumerate(k[14:]):
                if j == ' ':
                    full_name += (k[14:i+14] + ' ')
                    labeltext += (k[14:i+14] + ' ')
                    for o, w in enumerate(k[i+15:]):
                        if w == ' ':
                            for y, z in enumerate(k[o+i+16:]):
                                if z == ' ':
                                    full_name += k[o+i+16:o+i+y+16]
                                    labeltext += k[o+i+16:]
                                    labeltext_list.append(labeltext)
                                    full_name_list.append(full_name)
                                    if len(full_name_list) > 1:
                                        for yummy in range(len(full_name_list)):
                                            if len(full_name_list[yummy]) > lenth:
                                                lenth = len(full_name_list[yummy])
                                   
                                    pp += 1
                                    full_name = ''
                                    labeltext = ''
                                    
                                    if pp == l :
                                        break
                            break
                    break
        for sa in range(len(labeltext_list)):
            for k, j in enumerate(labeltext_list[sa]):
                if 'email' not in labeltext_list[sa]:
                    if j == ':':
                        labeltext_list[sa] = labeltext_list[sa][:k-6]+ ((lenth - len(labeltext_list[sa][:k-6])+1) * ' ') + labeltext_list[sa][k-6:]
                        break
                else:
                    if j == ':':
                        labeltext_list[sa] = labeltext_list[sa][:k-5]+ ((lenth - len(labeltext_list[sa][:k-5])+1) * ' ') + labeltext_list[sa][k-5:]
                        break
        for e, d in enumerate(labeltext_list):
            hh += d
            w = tk.Text(frram2, height=1, borderwidth=0)
            w.insert(1.0, d)
            w.grid(column=0, row=e+1)
            w.configure(state='disabled', font=("Courier", 12, "italic"))
            editbutton = tk.Button(frram2, text='\u270E Edit', command=lambda b=e: edit(b))
            buttons.append(editbutton)
            text.append(w)
            editbutton.grid(column=1, row=e+1)
            deletebutton = tk.Button(frram2, text='\u2718 Delete', command=lambda v=e: delete(v))
            deletebutton.grid(column=2, row=e+1)
            deletes.append(deletebutton)
                    
    def v(x):
        def b(x):
            irow = 1
            for i in dismiss_group:
                i.grid_forget()
            for i in range(len(text)):
                text[i].grid_forget()
                buttons[i].grid_forget()
                deletes[i].grid_forget()
            for j in range(len(text)):
                if x.char != '\x7f':
                    if searchbar.get() + x.char in labeltext_list[j]:
                        if text[j].get('1.0', 'end-1c') != 'Contact deleted sucessfully.':
                            text[j].grid(column=0, row=irow)
                            buttons[j].grid(column=1, row=irow)
                            deletes[j].grid(column=2, row=irow)
                            irow+=1
                            notfound.grid_forget()
                else:
                    if searchbar.get()[:-2] in labeltext_list[j]:
                        if text[j].get('1.0', 'end-1c') != 'Contact deleted sucessfully.':
                            text[j].grid(column=0, row=irow)
                            buttons[j].grid(column=1, row=irow)
                            deletes[j].grid(column=2, row=irow)
                            irow+=1
                            notfound.grid_forget()
            if irow == 1:
                notfound.grid(column=1,row=0)
        
        def c(x):
            allcontacts.focus()
            if searchbar.get() == '':
                searchbar.insert(0, 'search')
                
            
        
        if searchbar.get() == 'search':
            searchbar.delete(0, 'end')
        searchbar.bind('<Key>', b)
        frram2.bind('<Button-1>', c)
        for t in text:
            t.bind('<Button-1>', c)
    
    searchbar = tk.Entry(frram, borderwidth=0)
    searchbar.grid(column=0, row=0, st='nw')
    searchbar.insert(0, 'search')
    first_or_last = tk.Label(frram, text=' '*18+'Sort by: ')
    first_or_last.grid(column=1, row=0, st='ne')
    first_radio = tk.Radiobutton(frram, text='FN', variable=var, value=1, command=sort_tmp)
    first_radio.grid(column=2, row=0)
    last_radio = tk.Radiobutton(frram, text='LN', variable=var, value=2, command=sort_tmp)
    last_radio.grid(column=3, row=0, st='ne')
    
    for e, d in enumerate(labeltext_list):
        hh +=d
        w = tk.Text(frram2, height=1, borderwidth=0)
        w.insert(1.0, d)
        w.grid(column=0, row=e+1)
        w.configure(state='disabled', font=("Courier", 12, "italic"))
        editbutton = tk.Button(frram2, text='\u270E Edit', command=lambda b=e: edit(b))
        buttons.append(editbutton)
        text.append(w)
        editbutton.grid(column=1, row=e+1)
        deletebutton = tk.Button(frram2, text='\u2718 Delete', command=lambda v=e: delete(v))
        deletebutton.grid(column=2, row=e+1)
        deletes.append(deletebutton)
    
    notfound = tk.Label(frram2, text='No contact found!')
    searchbar.bind('<FocusIn>', v)
        
                            
                    
                
            
        
    allcontacts.mainloop()
    
def sort():
    def sort_selected(x):
        if x.get() == 1:
            sort_first()
            sort.destroy()
        elif x.get() == 2:
            sort_last()
            sort.destroy()
    sort = tk.Toplevel(root)
    sort.title('Sort Contacts')
    sort.geometry('350x200')
    s = tk.IntVar()
    frame11 = tk.Frame(sort)
    frame11.pack()
    frame12 = tk.Frame(sort)
    frame12.pack()
    frame13 = tk.Frame(sort)
    frame13.pack(side='bottom')
    glabel = tk.Label(frame11, text='\u25CF Select how you want to sort contacts:')
    glabel.pack()
    r1 = tk.Radiobutton(frame12, text='firstname ', variable=s, value=1)
    r1.pack(side='left')
    r2 = tk.Radiobutton(frame12, text='lastname ', variable=s, value=2)
    r2.pack(side='left')
    bUtton = tk.Button(frame13, text='Confirm', command=lambda x=s: sort_selected(x))
    bUtton.pack()
    sort.mainloop()

def text_search():
    def check():
        t_list = []
        a = search_text_Text.get('1.0', 'end-1c')
        namesearch = re.findall('@\w*', a)
        numbersearch = re.findall('#\d*', a)
        result_page = tk.Toplevel(textsearch)
        result_page.title('Search result')
        frame1 = tk.Frame(result_page)
        frame1.pack()
        frame2 = tk.Frame(result_page)
        frame2.pack(fill='both')
        
        for i in range(len(namesearch)):
            for j in range(len(full_name_list)):
                if namesearch[i][1:].lower() in full_name_list[j]:
                    t_list.append(labeltext_list[j])
                    break
        for i in range(len(numbersearch)):
            for j in range(len(labeltext_list)):
                if numbersearch[i][1:].lower() in labeltext_list[j] and labeltext_list[j] not in t_list:
                    t_list.append(labeltext_list[j])
                    break
        if len(t_list) == 0:
            t = tk.Label(frame1, text='No matches were found!')
            t.pack()
        elif len(t_list) > 1:
            t = tk.Label(frame1, text='%s matches have been found'%(len(t_list)))
            t.pack()
        else:
            t = tk.Label(frame1, text='1 match have been found')
            t.pack()
        for e, d in enumerate(t_list):
            w = tk.Label(frame2, text=d)
            w.grid(column=0, row=e, st='nw')
            
        
    textsearch = tk.Toplevel(root)
    textsearch.title('Text search')
    frame1 = tk.Frame(textsearch, width=454, height=20)
    frame1.pack()
    full_name, labeltext='', ''
    full_name_list, labeltext_list=[], []
    pp = -1
    lenth = 0
    f = open('Untitled.txt')
    list1 = f.readlines()
    f.close()
    for l, k in enumerate(list1):
        for i, j in enumerate(k[14:]):
            if j == ' ':
                full_name += (k[14:i+14])
                labeltext += (k[14:i+14] + ' ')
                for o, w in enumerate(k[i+15:]):
                    if w == ' ':
                        for y, z in enumerate(k[o+i+16:]):
                            if z == ' ':
                                full_name += k[o+i+16:o+i+y+16]
                                labeltext += k[o+i+16:]
                                labeltext_list.append(labeltext)
                                full_name_list.append(full_name)
                                if len(full_name_list) > 1:
                                    for yummy in range(len(full_name_list)):
                                        if len(full_name_list[yummy]) > lenth:
                                            lenth = len(full_name_list[yummy])
                               
                                pp += 1
                                full_name = ''
                                labeltext = ''
                                
                                if pp == l :
                                    break
                        break
                break
    for sa in range(len(labeltext_list)):
        for k, j in enumerate(labeltext_list[sa]):
            if 'email' not in labeltext_list[sa]:
                if j == ':':
                    labeltext_list[sa] = labeltext_list[sa][:k-6]+ ((lenth - len(labeltext_list[sa][:k-6])+1) * ' ') + labeltext_list[sa][k-6:]
                    break
            else:
                if j == ':':
                    labeltext_list[sa] = labeltext_list[sa][:k-5]+ ((lenth - len(labeltext_list[sa][:k-5])+1) * ' ') + labeltext_list[sa][k-5:]
                    break
    
    for i in range(len(full_name_list)):
        full_name_list[i] = full_name_list[i].lower()
    
    search_text_label = tk.Label(frame1, text='Enter your text to search for contacts:')
    search_text_label.pack()
    search_text_Text = tk.Text(frame1, highlightthickness=0)
    search_text_Text.pack(fill='both', expand=1)
    sendbutton = tk.Button(frame1, text='Check', command=check)
    sendbutton.pack()
    textsearch.mainloop()
    
def fake():
    if len(yh) == 0:
        global fake_page, progress
        fake_page = tk.Toplevel(root)
        fake_page.title('loading...')
        yh.append(fake_page)
        progress = ttk.Progressbar(fake_page, orient='horizontal', length=300, mode='determinate')
        progress.grid(column=0, row=0)
        progress['value'] = 0
        fake_page.update()
        progress['value'] += 50
        fake_page.update()
    a = ''
    b = "https://fauxid.com"
    c = ''
    d = []
    
    page = requests.get(b)
    
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    
    events = soup.find_all('span', class_="id_name can-copy")
    
    
    for i in events:
        a+=i.text 
    e = re.finditer(' ', a)
    f = 0
    for i in e:
        g = i.start()
        f+=1
    if f == 1:
        progress['value'] += 50
        fake_page.update()
        fake_page.title('Fake contact')
        frame1 = tk.Frame(fake_page)
        frame1.grid(column=0, row=0)
        frame2 = tk.Frame(fake_page)
        frame2.grid(column=0,row=1)
        d.append(a[:g])
        d.append(a[g+1:])
        c = 'https://datafakegenerator.com/generador.php'
        paga = requests.get(c)
        soap = BeautifulSoup(paga.content, 'html.parser')
        eventt = soap.find_all('p', class_='izquierda')
        d.append(eventt[9].text)
        d.append(eventt[11].text)
        label = tk.Label(frame1, text='Do you want to insert this contact:\n{}   email: {}   number: {}\n '.format(d[0]+' '+d[1], d[2], d[3]))
        label.grid(column=0, row=0)
        yh.pop()
        def insert():
            f = open('Untitled.txt','a')
            f.write('{}) firstname: {} lastname: {} email: {}   number: {}\n'.format(d[0][0].upper(), d[0], d[1], d[2], d[3]))
            f.close()
            fake_page.destroy()
            f = open('Untitled.txt','r')
            chars = f.readlines()
            for i in range(len(chars)):
                chars[i] = chars[i][0].upper()
            if chars == chars.sort():
                sort_first()
            else:
                sort_last()
            f.close()
        def noinsert():
            fake_page.destroy()
        yes = tk.Button(frame2, text='Yes', command=insert)
        yes.grid(column=0, row=0)
        no = tk.Button(frame2, text='No', command=noinsert)
        no.grid(column=1, row=0)
        fake_page.mainloop()
        return
    else:
        fake()
    
    fake_page.mainloop()
            

def sort_first():
    N_SLs = ''
    name = ''
    full_name_list=[]
    pp = -1
    lenth = 0
    f = open('Untitled.txt')
    list = f.readlines()
    f.close()
    for l, k in enumerate(list):
        for i, j in enumerate(k[14:]):
            if j == ' ':
                name += (k[14:i+14] + ' ')
                for o, w in enumerate(k[i+15:]):
                    if w == ' ':
                        for y, z in enumerate(k[o+i+16:]):
                            if z == ' ':
                                name += k[o+i+16:o+i+y+16]
                                full_name_list.append(name)
                                if len(full_name_list) > 1:
                                    for yummy in range(len(full_name_list)):
                                        if len(full_name_list[yummy]) > lenth:
                                            lenth = len(full_name_list[yummy])
                               
                                pp += 1
                                name = ''
                                

                                
                                if pp == l :
                                    break
                        break
                break
                                
                            
    full_name_list.sort()
    for i in range(len(full_name_list)):
        for jj, j in enumerate(full_name_list[i]):
            if j == ' ':
                for k in list:
                    if full_name_list[i][:jj] in k:
                        if (' ' + full_name_list[i][jj+1:] + ' ') in k:
                            N_SLs += k
                            break
                break
        
        
    f = open('Untitled.txt', 'w')
    f.write(N_SLs)
    f.close()

def sort_last():
    SL_s, reversedlist, wantedlist = '', [], []
    hh=''
    f = open('Untitled.txt')
    list = f.readlines()
    for i in list:
        a = re.search('lastname: ', i)
        b = re.search(' ', i[a.end():])
        SL_s += i[a.end():a.end()+b.start()+1]
        c = re.search('firstname: ', i)
        SL_s += i[c.end():a.start()-1]
        reversedlist.append(SL_s)
        SL_s = ''
    reversedlist.sort()
    for j in reversedlist:
        d = re.search(' ', j)
        for k in list:
            if j[:d.start()] in k:
                if j[d.start()+1:] in k:
                    wantedlist.append(k)
                    break
    for p in wantedlist:
        hh+=p
    f = open('Untitled.txt', 'w')
    f.write(hh)
    f.close()

def About():
    a = ' '*10+'Developed by AmirHossein Borumand as \u00A9CP\n'+' '*20+'from SKU\n\n'+' '*18+'summer of 1400'
    aboutl = tk.Label(frameb, text=a, fg='white', bg='#262126',font =("Ariel", 10))    
    aboutl.pack() 
    about_button['state'] = 'disabled'
    
    
    
    

# Root_Buttons
global about_button
newc_button = tk.Button(framea, text='\u271B New Contact ', fg='blue', activeforeground='white', command=newcontact)
newc_button.pack()
allc_button = tk.Button(framea, text=' \u4DC0  Contact list ', fg='blue', activeforeground='white', command=allcontacts)
allc_button.pack()
srtc_button = tk.Button(framea, text=' \u2B83  Sort order   ', fg='blue', activeforeground='white', command=sort)
srtc_button.pack()
txts_button = tk.Button(framea, text=' \u1CC5  Text search ', fg='blue', activeforeground='white', command=text_search)
txts_button.pack()
fake_button = tk.Button(framea, text=' ? Fake contact ', fg='blue', activeforeground='white', command=fake)
fake_button.pack()
lavel = tk.Label(framea, text='           \n'*8).pack()
about_button = tk.Button(framea, text='About', fg='blue', activeforeground='white', state='normal', command=About)
about_button.pack(anchor='s')
lavel2 = tk.Label(framea, text='           \n'*1).pack()

root.mainloop()