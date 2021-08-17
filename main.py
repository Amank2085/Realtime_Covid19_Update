import time
from tkinter import font
from typing import Text
import tkinter as tk
import plyer
import requests
import threading
from bs4 import BeautifulSoup

def getData(url):
        r = requests.get(url)
        return r.text

def get_covid_status_of_India():
    myHtmlData = getData('https://www.mygov.in/covid-19')
    soup = BeautifulSoup(myHtmlData, 'html.parser')

    all_details = ""

    active_case = soup.find("div", class_="information_row").find_all("div",class_="active-case")
#     print(active_case)

    for block in active_case:
        count = block.find("div", class_="block-active-cases").find("span",class_= "icount").get_text()
        text = block.find("div", class_="info_label").get_text()
        all_details = all_details + text + " : " + count + "\n"

    rest_case = soup.find("div", class_="information_row").find_all("div",class_="iblock")
#     print(rest_case)

    for block in rest_case:
        count = block.find("div", class_="iblock_text").find("span",class_= "icount").get_text()
        text = block.find("div", class_="iblock_text").find("div",class_="info_label").get_text()
        all_details = all_details + text + " : " + count + "\n"

    return all_details

# function use to reload the data from website
def refresh():
    newdata = get_covid_status_of_India()
    print("Refreshing....")
    mainLabel['text'] = newdata

# function for notification
def notify_me():
    while(True):
        plyer.notification.notify(
            title = "Covid 19 cases of INDIA",
            message = get_covid_status_of_India(),
            app_icon= "E:\Projects\Python Projects\Realtime CoronaVirus Outbreak Notification System\icon.ico",
            timeout = 10
        )
        time.sleep(30)
        

if __name__ == "__main__":
        itemStr=  get_covid_status_of_India()
        print(type(itemStr))
        print(len(itemStr))

# Creating Gui

root = tk.Tk()
root.geometry("900x800")
root.iconbitmap(
    "E:\Projects\Python Projects\Realtime CoronaVirus Outbreak Notification System\icon.ico")
root.title("CORONA DATA TRACKER - INDIA")
root.configure(background='white')
f = ("poppins",16,"bold")

banner = tk.PhotoImage(
    file="E:\Projects\Python Projects\Realtime CoronaVirus Outbreak Notification System\covidbanner.png")
bannerLabel = tk.Label(root, image= banner)
bannerLabel.pack()

mainLabel = tk.Label(root,text = get_covid_status_of_India(), font = f, bg = 'white')
mainLabel.pack();

reBtn = tk.Button(root, text = "REFRESH", font = f,relief="solid", command=refresh)
reBtn.pack()

# create a new thread
th1 = threading.Thread(target= notify_me)
th1.setDaemon(True)
th1.start()

root.mainloop()

