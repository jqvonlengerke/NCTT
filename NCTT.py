#READ ME in TOOL KIT.
#THIS VERSION HAS BEEN MODIFIED TO WORK WITH ALL OPERATING SYSTEMS. NOT TESTED. 
import csv,webbrowser,datetime, os.path, sys
import tkinter as tk
#import os the accursed file opener
from functools import partial


def repeat_entry(exceptions, user_entry, csv_data):#Entry is name of app attempting to be entered, csv_data is a 2D array containing the links and names for all the websites. Function checks for repeated names or links

    for i in csv_data:

        if i[0].lower() == user_entry[0].lower():
            exceptions.config(text="EXCEPTION:\nEntered Program Name\n '" + user_entry[0] + "'\n is too similar currently \n stored program \n'" + i[0] + "'.")
            return False
        if remove_http(i[1])  == remove_http(user_entry[1]):
            exception_text = "EXCEPTION:\nEntered Link already stored\n in program named \n'" + i[0] + "'."
            exceptions.config(text=exception_text)
            exception_text = ""
            return False

    return True
def remove_http(link):

    if "https://" in link.lower():
        link = link[8:]
    if "http://" in link.lower():
        link = link = link[7:]

    return link
#
def csv_editor(title, link, operation, exceptions,labelViewListName,labelViewListLink):
    exceptions.config(text="")
    title = name.get()
    link = url.get()
    if operation == "write":
        csv_old = csv_reader()
        if repeat_entry(exceptions,[title,link],csv_old):
            with open('links.csv', 'w', newline='', encoding='utf-8') as csvfile:
                file = csv.writer(csvfile, quoting=csv.QUOTE_NONE, escapechar=' ')
                file.writerows(csv_old)
                file.writerow([title, link])
            exceptions.config(text="Program with title \n'" + title + "'\n entered successfully.")

    elif operation == "remove":
        csv_old = csv_reader()
        csv_old_filtered = []
        for i in range(0,len(csv_old)):
            if not (csv_old[i][0] == title or csv_old[i][1] == link):
                csv_old_filtered.append(csv_old[i])
        if len(csv_old) != len(csv_old_filtered):
            exceptions.config(text="Program with title \n'" + title + "' \nremoved successfully.")
        else:
            exceptions.config(text="Program with title \n'" + title + "' \nwas not found \n in storage.")
        with open('links.csv', 'w', newline='', encoding='utf-8') as csvfile:
            file = csv.writer(csvfile, quoting=csv.QUOTE_NONE, escapechar=' ')
            file.writerows(csv_old_filtered)

    elif operation == "new":
        with open('links.csv', 'w+') as csvfile:
            file = csv.writer(csvfile)
            file.writerows("")
        exceptions.config(text="Previous list\n successfully cleared")
    view_list(labelViewListName,labelViewListLink)
def csv_reader():
    with open('links.csv', 'r', newline='') as csvfile:
        file = csv.reader(csvfile)
        return_list = []
        for row in csvfile:
            return_list.append(row)
    return_list_b = []
    for i in range(0, len(return_list)):
        return_list[i] = return_list[i].split(",")
    for i in range(0,len(return_list)):
        for j in range(0,len(return_list[i])):
            return_list[i][j] = return_list[i][j].replace('\r',"")
            return_list[i][j] = return_list[i][j].replace('\n', "")
            return_list[i][j] = return_list[i][j].replace(' ', "")
    return return_list

def NCTT(exceptions):
    links = csv_reader()
    exceptions.config(text=str(len(links)) + " programs found. Enjoy!")
    for link in links:
        webbrowser.open(link[1])
    #for link in links:   The accursed file opener
    #   os.startfile(link[1])

def view_list(name,link):
    current_file = csv_reader()
    names = "Program Names:"
    links = "Links:"
    for a in current_file:
        names = names + "\n" + (a[0])
        links = links + "\n" + (a[1])


    name.config(text="--------------------\n"+ names)
    link.config(text="--------------------\n"+ links)





############
location = sys.argv[0]#MODIFY FOR OTHER OS FILE ARCITECTURE
location = location.strip("NCTT.py")#MODIFIED FROM .exe VERSION, CHANGE ".py" to ".exe:" FOR APPLICATION
location = ("C" +location + "links.csv")#MODIFY FOR OTHER OS FILE ARCITECTURE
############
if not os.path.isfile(location):
    with open("links.csv", "w") as null:
        pass
    webbrowser.open("https://www.youtube.com/watch?v=MfrApWZ5sSo&feature=youtu.be")


root = tk.Tk()
root.geometry('720x480')
root.title('New Computer Transfer Tool')





name = tk.StringVar()
url = tk.StringVar()
exception_var = tk.StringVar()
labelName = tk.Label(root, text="Enter Name").grid(row=1, column=1)
labelLink = tk.Label(root, text="Enter URL").grid(row=2, column=1)
labelRunNCTT = tk.Label(root, text="Running on New Computer?").grid(row=8, column=1)
labelLine = tk.Label(root, text="--------------------").grid(row=4, column=1)
labelLine = tk.Label(root, text="--------------------").grid(row=4, column=2)
labelNew = tk.Label(root, text="Want to make a new list?").grid(row=8, column=2)
labelLine = tk.Label(root, text="--------------------").grid(row=7, column=1)
labelLine = tk.Label(root, text="--------------------").grid(row=7, column=2)
labelErrorsHeader = tk.Label(root, text="Status:").grid(row=5, column=1)
labelErrors = tk.Label(root)
labelErrors.grid(row=5, column=2)

labelViewListName = tk.Label(root)
labelViewListName.grid(row=11, column=1)
labelViewListLink= tk.Label(root)
labelViewListLink.grid(row=11, column=2)

entryName = tk.Entry(root, textvariable=name).grid(row=1, column=2)
entryLink = tk.Entry(root, textvariable=url).grid(row=2, column=2)





remove = partial(csv_editor,name,url,"remove", labelErrors,labelViewListName,labelViewListLink)
write = partial(csv_editor,name,url,"write",labelErrors,labelViewListName,labelViewListLink)
new = partial(csv_editor,name,url,"new", labelErrors,labelViewListName,labelViewListLink)
NCTT = partial(NCTT,labelErrors)


buttonWrite = tk.Button(root, text="Write", command=write).grid(row=3, column=1)
buttonRemove = tk.Button(root, text="Remove", command=remove).grid(row=3, column=2)

buttonNCTT = tk.Button(root, text="Run NCTT!", command=NCTT).grid(row=9, column=1)#TEMP WRITE
buttonNew = tk.Button(root, text="Create New List", command=new).grid(row=9, column=2)


view_list(labelViewListName,labelViewListLink)

root.mainloop()


