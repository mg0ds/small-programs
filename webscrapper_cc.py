import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def brak_pytania(soup):
    brak_p = """teks
             do
             sprawdzenia"""

    try:
        odp = soup.find_all('div', {'class': 'text text--center'})
        txt = ""
        for _ in odp:
            txt += _.get_text()
        #print(txt.split())
        ile_pasuje = 0
        for wyraz_pyt in brak_p.split():
            for wyraz_szukam in txt.split():
                if wyraz_pyt.lower() == wyraz_szukam.lower():
                    ile_pasuje += 1
        if ile_pasuje > int(len(txt.split()) * 0.5):
            #print("Pasuje! Brak pytania")
            #print(f"ile pasuje: {ile_pasuje},  row len: {len(txt.split())}")
            return True
    except:
        print("Brak pytania lub coś jest źle")
        return False


def pytanie(soup):
    try:
        odp = soup.find_all('div', {'class': 'text text--center text--small text--alternative text--uppercase'})
        txt = ""
        for _ in odp:
            txt += _.get_text()
        return txt
    except:
        print("Nie znajduje pytania lub coś jest źle!")
        return False


def szukaj_pytania(friends, pyt):
    znalezione = []
    ile_pasuje = 0
    znalezione.append(pyt)
    for i, row in enumerate(friends):
        if row.split()[0][0] == "-" and len(row) > 4:
            #print(row)
            for wyraz_pyt in pyt.split():
                for wyraz_szukam in row[1:].split():
                    if wyraz_pyt.lower() == wyraz_szukam.lower():
                        ile_pasuje += 1
            if ile_pasuje > int(len(row.split())*0.4):
                print("Chyba pasuje?")
                print(f"ile pasuje: {ile_pasuje},  row len: {len(row.split())}")
                print(f"Znalezione pytanie:\n{row}")
                print(f"Odpowiedz: {friends[i+1]}")
                znalezione.append(row)
                znalezione.append(friends[i+1])
            ile_pasuje = 0
    if len(znalezione) == 1:
        znalezione.append("Nie dopasowałem pytania :( Sam se szukaj!")
    return znalezione


# sending message
odbiorcy = ["mail@cos.com", "mail2@cos.com"]
message = MIMEMultipart()
message["from"] = "ktos"
message["to"] = ", ".join(odbiorcy)
message["subject"] = "CC konkurs JEST PYTANIE!"

# load question and answer list
friends = []
with open("f1.txt", "r", encoding='UTF-16') as f:
    for row in f.readlines():
        friends.append(row)
    f.close()

options = Options()
options.headless = True
os.environ['PATH'] += r":/Users/xx/webdrivers"
driver = webdriver.Chrome(options=options)

pyt_wyslane = False
czas_ok = True

while czas_ok:

    file1 = open("log.txt", "a")  # append mode

    print("Sprawdzam...")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)

    driver.get('https://jakasstrona.com/#/home')
    sleep(3)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    if brak_pytania(soup):
        file1.write(f"\n{str(now)} - Nie ma pytania")
        print("Nie ma pytania")
        print()
        pyt_wyslane = False
    elif pytanie(soup):
        print("Jest pytanie!!")
        pyt = pytanie(soup)
        print(pyt)
        wynik = szukaj_pytania(friends, pytanie(soup))
        file1.write(f"\n{str(now)} - Jest pytanie!\n{wynik}")
        if not pyt_wyslane:
            message.attach(MIMEText(
                f"""\n{str(now)} - Jest pytanie!\n
            Pytanie ze strony: {wynik[0]}\n
            Dopasowanie pytania i odpowiedzi:
            {' '.join(wynik[1:])}
            https://jakasstrona.com/#/home""")
            )
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login("mojmail@gdzies.com", "tajnykod")
                smtp.send_message(message)
                print("email Sent")
                file1.write(f"\n{str(now)} - Jest pytanie!\n{wynik}\n********** email sent **********")
            pyt_wyslane = True
    else:
        print("Cos jest nie tak!")
        file1.write(f"\n{str(now)} - Coś jest nie tak!")
        message.attach(MIMEText(f"\n{str(now)} - Coś jest nie tak!"))
        if not pyt_wyslane:
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login("mojmail@gdzies.com", "tajnykod")
                smtp.send_message(message)
                print("email Sent")
                file1.write(f"Coś jest nie tak!")
            pyt_wyslane = True

    file1.close()

    if current_time > "20:10:00":
        czas_ok = False
    sleep(120)

print("Koniec czasu na dziś!")
quit()
