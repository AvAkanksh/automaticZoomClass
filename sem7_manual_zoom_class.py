import os
import time
import random
from datetime import date
from termcolor import colored

colors_list = ['red','green','yellow','blue','magenta','cyan','white']

def rainbow_complete(string):
    for i in range(len(string)):
        print(colored(string[i],random.choice(colors_list)),end='')


power_electronics       = 'https://zoom.us/j/98518142431?pwd=Nk9xbWRIcFJzaVpic2RPMDZtRkRCdz09'
advance_ee_lab          = 'https://zoom.us/j/92744863311?pwd=VENNbXlFQjZSQkdlMXR1clYvRzV6Zz09'
electrical_machines     = 'https://zoom.us/j/93239768647?pwd=eGhWc25ySGZmVzRVZWVpYzR6K1Budz09'
medical_imaging         = 'https://zoom.us/j/95393449763?pwd=Ym4zcldRbEJ0L0dwYTdMd2MwTCtVUT09'
wireless_communication  = 'https://zoom.us/j/94030475656?pwd=SUFaaHl1ayt6UTUxekg4b0liRlBmQT09'
deep_learning           = 'https://zoom.us/j/98582805312?pwd=ZVRuM1BkS0NGV2VRanNpU29VaHd4QT09'
industrial_lecture      = 'https://zoom.us/j/99367974277?pwd=bGRYZXBrcWRFdHZzdmgrdCtUNmlTZz09'

# Sunday Monday Tuesday Wednesday Thursday Friday Saturday
#    0     1       2        3         4       5       6

url = None
currentTime = int(time.strftime("%H%M", time.localtime()))
day_of_week = date.today().weekday()
done = 0
t1 = time.time()
runtime = time.time()-t1
check_time = 1
count = 0
automatic = False

if(automatic == False):
    day_of_week = int(input('\nChoose the day : \n1)Monday \n2)Tueday \n3)Wednesday \n4)Thursday \n5)Friday \n (1-5): '))
    day_of_week -= 1
    currentTime = int(input("\nEnter the time in 24 hrs format \nExample :\n1)If the time is 9:23 am then enter 923 \n2)if the time is 2:15 pm then enter 1315 \n time :"))

while (((done) != 1) and (runtime < check_time)):

#  Monday Time table
    if (day_of_week == 0):
        if (900 <= currentTime <= 950):
            rainbow_complete('Medical Imaging Class')
            url = medical_imaging
            done = 1
        elif (1000 <= currentTime <= 1050):
            rainbow_complete('Wireless Communication')
            url = wireless_communication
            done = 1
        elif (1100 <= currentTime <= 1150):
            rainbow_complete('Deep Learning')
            url = deep_learning
            done = 1

#  Tuesday Time table
    elif (day_of_week == 1):
        if (1000 <= currentTime <= 1050):
            rainbow_complete('Power Electronics Class')
            url = power_electronics
            done = 1
        elif (1100 <= currentTime <= 1150):
            rainbow_complete('Medical Imaging Class')
            url = medical_imaging
            done = 1
        elif (1500 <= currentTime <= 1730):
            rainbow_complete('Advance EE LAB')
            url = advance_ee_lab
            done = 1

#  Wednesday Time table
    elif (day_of_week == 2):
        if (900 <= currentTime <= 950):
            rainbow_complete('Wireless Communication')
            url = wireless_communication
            done = 1
        elif (1000 <= currentTime <= 1050):
            rainbow_complete('Deep Learning')
            url = deep_learning
            done = 1

#  Thursday Time table
    elif (day_of_week == 3):
        if (900 <= currentTime <= 950):
            rainbow_complete('Power Electronics')
            url = power_electronics
            done = 1
        elif (1000 <= currentTime <= 1050):
            rainbow_complete('Medical Imaging Class')
            url = medical_imaging
            done = 1
        elif (1100 <= currentTime <= 1150):
            rainbow_complete('Wireless Communication')
            url = wireless_communication
            done = 1
        elif (1500 <= currentTime <= 1730):
            rainbow_complete('Medical Imaging Class')
            url = electrical_machines
            done = 1

#  Friday Time table
    elif (day_of_week == 4):
        if (900 <= currentTime <= 950):
            rainbow_complete('Deep Learning')
            url = deep_learning
            done = 1
        elif (1100 <= currentTime <= 1150):
            rainbow_complete('Power Electronics')
            url = power_electronics
            done = 1
        elif (1400 <= currentTime <= 1450):
            rainbow_complete('Power Electronics Tutorial')
            url = power_electronics
            done = 1
    runtime = time.time() - t1


if(url != None):
    os.system('xdg-open {}'.format(url))
    rainbow_complete('<'+'x'*40+'>')
    print('\n\t '+ colored('Launching the zoom class','green'))
    rainbow_complete('<'+'x'*40+'>')
    print('')
else:
    rainbow_complete('<'+'~'*40+'>')
    print('\n\tThere is '+ colored('No','red')+ ' class right now!')
    rainbow_complete('<'+'~'*40+'>')
    print('')