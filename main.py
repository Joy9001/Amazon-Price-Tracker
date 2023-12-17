from bs4 import BeautifulSoup
import requests
import smtplib
import os

BASE_PRICE = int(input("Enter The Base Price: "))

my_gmail = os.environ.get("YOUR_GMAIL")
my_outlook = os.environ.get("YOUR_OUTLOOK")
password_gmail = os.environ.get("YOUR_GMAIL_PASSWORD")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept-Language": "en-IN,en;q=0.9"
}

link = input("Enter your Product Link From Amazon: \n")

try:
    response = requests.get(url=link, headers=headers).text
    soup = BeautifulSoup(response, "html.parser")

    get_price = soup.select_one(selector="span span .a-price-whole").getText()
    price = float(get_price.split(".")[0].replace(',', ''))

    if price < BASE_PRICE:
        message = f"Subject: AMAZON PRICE DROP ALART \n\n Redragon Kumara K552 Rainbow LED Backlit TKL Ten Key-Less Mechanical Wired Gaming Keyboard Without Numlock Keys (Black) is NOW {price}! \n!!! BUY NOW !!! \n{link}"

        smtp_server = "smtp.gmail.com"
        try:
            server = smtplib.SMTP(host=smtp_server, port=587)
            server.starttls()
            server.login(user=my_gmail, password=password_gmail)
            server.sendmail(from_addr=my_gmail, to_addrs=my_outlook, msg=message)
            print("Email sent successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Price Hasn't Decreased! I'll Notify When Found A Lower Price Than The Base Price!\n")

except requests.exceptions.MissingSchema:
    print("Invalid URL! You missed 'https://...' ")
except AttributeError:
    print("Please Enter A Valid Link From Amazon!")
except requests.exceptions.InvalidSchema:
    print("Please Enter A Valid Link ! No connection adapters were found!")
