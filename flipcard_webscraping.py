import requests
from bs4 import BeautifulSoup
import pandas as pd 


def tshirts(page):
    url = f'https://www.flipkart.com/mens-tshirts/pr?sid=clo%2Cash%2Cank%2Cedy&offer=nb%3Amp%3A04174a7017&marketplace=FLIPKART&restrictLocale=true&fm=personalisedRecommendation%2FC2&iid=R%3Ato%3Bpt%3Ahp%3Buid%3A623b124a-d795-11ec-aa84-f955e0a0d169%3B.cid%3AS_F_N_clo_ash_ank_edy__o_nb_mp_04174a7017__NONE_ALL%3Bnid%3Aclo_ash_ank_edy_%3Bet%3AS%3Beid%3Aclo_ash_ank_edy_%3Bmp%3AF%3Bct%3Ao%3B&ppt=None&ppn=None&ssid=wpre3894v40000001652979714345&otracker=hp_reco_Trending%2BOffers_2_9.dealCard.OMU_cid%3AS_F_N_clo_ash_ank_edy__o_nb_mp_04174a7017__NONE_ALL%3Bnid%3Aclo_ash_ank_edy_%3Bet%3AS%3Beid%3Aclo_ash_ank_edy_%3Bmp%3AF%3Bct%3Ao%3B_5&otracker1=hp_reco_WHITELISTED_personalisedRecommendation%2FC2_Trending%2BOffers_DESKTOP_HORIZONTAL_dealCard_cc_2_NA_view-all_5&cid=cid%3AS_F_N_clo_ash_ank_edy__o_nb_mp_04174a7017__NONE_ALL%3Bnid%3Aclo_ash_ank_edy_%3Bet%3AS%3Beid%3Aclo_ash_ank_edy_%3Bmp%3AF%3Bct%3Ao%3B&page={page}'

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')


    return soup

def extract(soup):
    divs = soup.find_all('div', class_ = '_1xHGtK')
    #return len(divs) 
    for items in divs:
        title = items.find('a', class_ = 'IRpwTa').text
        #print(title)
        company = items.find('div', class_ = '_2WkVRV').text
        #print(company)

        #Original Price 
        #(try and except) ব্যাবহার করার কারণ হল যেন কোন ভুল না আসে।
        try:
            Original_price = items.find('div', class_ = '_30jeq3').text.replace('₹', '')
        except:
            Original_price = ''
        #Discound Price
        try:
            discound_price = items.find('div', class_ = '_3I9_wc').text.replace('₹', '')
        except:
            discound_price = ''
        #discound Price
        try:
            discound = items.find('div', class_ = '_3Ay6Sb').text.replace('off', '')
        except:
            discound = ''    

        #print(discound) 
        # একটি dictionari তৈরি করা হল 
        tshirt = {
            'Product Name': title,
            'Company': company,
            'Original_Price': Original_price,
            'discound_Price': discound_price,
            'discound': discound,
        } 
        tshirt_list.append(tshirt) 

    return  
#ডাটা ফ্রেম তৈরি করার জন্য একটি লিস্ট 
tshirt_list = []

for i in range(1, 20):
    print(f'Scrapping Page {i}!!')
    c = tshirts(i) 
    extract(c)
#print((tshirt_list))
# data fream create and convert to csv file.
df = pd.DataFrame(tshirt_list)
df.to_csv('Tshirts.csv')


