import time
import csv
import datetime as dt
def datain():
    try:

        inp=input("how was your day? ")
    except EOFError:
        print("Please enter a valid input.")
    
    # hr=int(time.strftime("%I"))
    # min = int(time.strftime("%M"))
    # ti=time.strftime("%p")
    # rntime=hr,":",min,ti

    time=dt.date.now()    

    good=["happy", "great", "awesome", "joy", "fun", "amazing", "excited", "smile", "good"]
    bad=["sad", "upset", "depressed", "bad", "cry", "lonely", "tired", "hopeless"]
    angry=["angry", "mad", "furious", "annoyed", "irritated", "hate", "rage"]
    inp = inp.lower()
        
    mood = "neutral"

    for word in good:
        if word in inp:
            mood = "happy"
            break

    for word in bad:
        if word in inp:
            mood = "sad"
            break

    for word in angry:
        if word in inp:
            mood = "angry"
            break



    with open('direcotry.csv', 'a')as f:
        writ=csv.writer(f)
        writ.writerow([time, mood,inp])
        print([time, mood,inp])


def dataout():
    try:
        with open('direcotry.csv', 'r')as f:
            read=csv.reader(f)
            for row in read:
                print(row)

    except FileNotFoundError:
        print("No data found. Please enter data first.")


def dataspec():
    try:
        with open('direcotry.csv', 'r')as f:
            print('''On  which basis you wold like to search\n1. Date/n2. Mood\n''')
            data=csv.reader(f)
            try: 
                inp=int(input("Enter :- "))
            except ValueError:
                print("enter Either 1 or 2")
            except EOFError:
                print("please enter something")

            if inp==1:
                try:
                    ab=input("enter date on which the record was stored :- ")
                except EOFError:
                    print('enter data ')

                for i in data:
                    if i[0]==ab:
                        print(i)
                else:
                    print('no data found for this date')

            elif inp==2:
                try:
                    abc=input("enter mood you want to find :- ")
                except EOFError:
                    print('enter data ')

                for i in data:
                    if i[1]==abc:
                        print(i)
                    else:
                        print('no data found for this mood')
                
    except FileNotFoundError:
        print("No data found. Please enter data first.")

def menu():
    while True:
        print("\nMENU :- ")
        print('1. Mood detector')
        print('2. Get all entries uptil now')
        print('3. Get entries specificaly')
        print('4. exit\n')
        try:
            wot=int(input('What would you like to do :- '))
        except EOFError:
            print("enter data please")
        if wot==1:
            datain()

        elif wot==2:
            dataout()
        
        elif wot==3:
            dataspec()
        
        elif wot==4:
            break
        
        else:
            print('enter valid option only')
        
        ad=input('want to do something more?(Y/N)')
        if ad.lower()=="y":
            continue
        else:
            break

menu()
print('Man you are the real G aapne use kari meri banai hui cheej')