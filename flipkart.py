import requests
from bs4 import BeautifulSoup as bs
from smtplib import SMTP

URL = 'https://www.flipkart.com/savya-home-apollo-hbcb-fabric-office-arm-chair/p/itm09573d0715a98?pid=OSCG2WPFZS3NGSZE&otracker=wishlist&lid=LSTOSCG2WPFZS3NGSZEZZWARM&fm=organic&iid=511c4d23-91bf-48be-91b6-6c5c6aab1185.OSCG2WPFZS3NGSZE.PRODUCTSUMMARY&ppt=dynamic&ppn=CART_PAGE&ssid=5p0unlutz40000001645366426570'

SMTP_SERVER ="smtp.gmail.com"
PORT = 587
EMAIL_ID = "vikhyatbhatnagarh@gmail.com"
PASSWORD = "germpgwmtzpxjwce"


def extract_price():
    page = requests.get(URL)

    soup = bs(page.content,"html.parser")

    price_cells = soup.findAll('div',{'class':'_30jeq3 _16Jk6d'})

    for price_cell in price_cells:
        val = price_cell.text

    numeric_val = val.split('₹')  

    actualvalList = numeric_val[1]

    final_val = int(actualvalList.replace(',',''))
   
    if(final_val <= 5990):
        server = SMTP(SMTP_SERVER,PORT)
        server.starttls()
        server.login(EMAIL_ID,PASSWORD)

        subject = "Alert for chair"
        body = "varPrice has fallen go and buy now at " + str(final_val) + "\n" + URL 
        msg = f"Subject: {subject}\n\n{body}"
        recipients=['vikhyatbhatnagarh@gmail.com',"santoshbhatnagar81@gmail.com"]
        server.sendmail(EMAIL_ID,recipients,msg)
        server.quit()

extract_price()
