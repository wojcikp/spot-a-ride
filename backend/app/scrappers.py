from bs4 import BeautifulSoup
import requests
import re


MARKI = ('Abarth', 'Acura', 'Aiways', 'Aixam', 'Alfa Romeo', 'Alpine', 'Asia', 'Aston Martin', 'Audi', 'Austin', 'Autobianchi', 
         'Baic', 'Bentley', 'BMW', 'BMW-ALPINA', 'Brilliance', 'Bugatti', 'Buick', 'BYD', 'Cadillac', 'Casalini', 'Caterham', 
         'Cenntro', 'Changan', 'Chatenet', 'Chevrolet', 'Chrysler', 'Citroën', 'Cupra', 'Dacia', 'Daewoo', 'Daihatsu', 'DeLorean', 
         'DFSK', 'DKW', 'Dodge', 'DR MOTOR', 'DS Automobiles', 'FAW', 'Ferrari', 'Fiat', 'Ford', 'Gaz', 'Geely', 'Genesis', 
         'GMC', 'GWM', 'Honda', 'Hongqi', 'Hummer', 'Hyundai', 'iamelectric', 'Ineos', 'Infiniti', 'Inny', 'Isuzu', 
         'Iveco', 'Jaguar', 'Jeep', 'Jetour', 'Kia', 'KTM', 'Lada', 'Lamborghini', 'Lancia', 'Land Rover', 'LEVC', 'Lexus', 
         'Ligier', 'Lincoln', 'Lotus', 'LTI', 'Lucid', 'Lynk & Co', 'MAN', 'Maserati', 'Maxus', 'Maybach', 'Mazda', 'McLaren', 
         'Mercedes-Benz', 'Mercury', 'MG', 'Microcar', 'MINI', 'Mitsubishi', 'NIO', 'Nissan', 'Nysa', 'Oldsmobile', 'Opel', 'Peugeot', 
         'Piaggio', 'Plymouth', 'Polestar', 'Polonez', 'Pontiac', 'Porsche', 'RAM', 'Renault', 'Rolls-Royce', 'Rover', 'Saab', 'Seat', 
         'Seres', 'Shuanghuan', 'Skoda', 'Skywell', 'Smart', 'SsangYong', 'Subaru', 'Suzuki', 'Syrena', 'Tarpan', 'Tata', 'Tesla', 
         'Toyota', 'Trabant', 'Triumph', 'Uaz', 'Vauxhall', 'VELEX', 'Volkswagen', 'Volvo', 'Warszawa', 'Wartburg', 'Wołga', 'XPeng', 
         'Zaporożec', 'Zastava', 'ZEEKR', 'Żuk')



def my_scheduled_job():
    print('CRON JOB')


def build_url(brand, model=None, production_year_from=None, production_year_to=None, mileage_limit=None, price_limit=None):
    url = 'https://www.otomoto.pl/osobowe/' + f'{brand}/'

    if model:
        url = url + f'{model}/'
    if production_year_from:
        url = url + f'od-{production_year_from}?'
    if production_year_to or mileage_limit or price_limit:
        url = url + '?search'
    if production_year_to:
        url = url + f'%5Bfilter_float_year%3Ato%5D={production_year_to}&search'
    if mileage_limit:
        url = url + f'%5Bfilter_float_mileage%3Ato%5D={mileage_limit}&search'
    if price_limit:
        url = url + f'%5Bfilter_float_price%3Ato%5D={price_limit}'

    return url


def scrap():
    base_url = build_url('Skoda', 'octavia', '2010', '2018', '180000', '85000')
    html = requests.get(base_url)
    soup = BeautifulSoup(html.text, 'html.parser')

    last_page = soup.find_all(class_='ooa-1xgr17q')
    pages = 0

    if len(last_page):
        pages = int(last_page[-1].text)

    for page in range(pages):
        url = f'{base_url}&page={page+1}'
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')

        cars = soup.find_all('article', class_='ooa-yca59n e1oqyyyi0')
        for car in cars:
            print(car.find('img')['src'])
            print(car.find('a')['href'])
            print(car['data-id'])
            print(car.find('h1').text)
            print(car.find(attrs={'data-parameter': 'year'}).text)
            print(car.find(attrs={'data-parameter': 'mileage'}).text)
            print(car.find('h3', class_='e1oqyyyi16 ooa-1n2paoq er34gjf0').text)
            print('+++++++++++++++++++++++++++++++++++++++++')
            print()



if __name__ == '__main__':
    scrap()
