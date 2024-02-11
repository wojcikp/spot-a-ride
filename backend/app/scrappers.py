from bs4 import BeautifulSoup
import requests
from django.utils import timezone

from .models import SearchedOffer, SpottedOffer


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



def scrapper_scheduled_job():
    print('SCRAPPER JOB', timezone.now())

    searched_offers = SearchedOffer.objects.all()

    for searched_offer in searched_offers:
        url = build_url(
            brand=searched_offer.brand,
            model=searched_offer.model,
            production_year_from=searched_offer.production_year_from,
            production_year_to=searched_offer.production_year_to,
            mileage_limit=searched_offer.mileage_limit,
            price_limit=searched_offer.price_limit
        )
        new_offers = scrap(url)
        spotted_offers = SpottedOffer.objects.filter(searched_offer=searched_offer)
        spotted_offers_to_compare = [
            {
                'otomoto_url': offer.otomoto_url,
                'otomoto_id': offer.otomoto_id,
                'otomoto_title': offer.otomoto_title,
                'production_year': offer.production_year,
                'mileage': offer.mileage,
                'price': offer.price,
            } for offer in spotted_offers
        ]
        new_offers_to_compare = [{key: value for key, value in offer.items() if key not in {'img'}} for offer in new_offers]

        mark_offers_as_gone(spotted_offers, new_offers_to_compare, spotted_offers_to_compare)

        spot_new_offers(new_offers_to_compare, spotted_offers_to_compare, new_offers, searched_offer)


def build_url(brand, model=None, production_year_from=None, production_year_to=None, mileage_limit=None, price_limit=None):
    url = 'https://www.otomoto.pl/osobowe/' + f'{brand}/'

    if model:
        url = url + f'{model}/'
    if production_year_from:
        url = url + f'od-{production_year_from}'
    if production_year_to or mileage_limit or price_limit:
        url = url + '?search'
    if production_year_to:
        url = url + f'%5Bfilter_float_year%3Ato%5D={production_year_to}&search'
    if mileage_limit:
        url = url + f'%5Bfilter_float_mileage%3Ato%5D={mileage_limit}&search'
    if price_limit:
        url = url + f'%5Bfilter_float_price%3Ato%5D={price_limit}'

    return url


def scrap(base_url):
    html = requests.get(base_url)
    soup = BeautifulSoup(html.text, 'html.parser')
    scrapped_offers = []

    last_page = soup.find_all(class_='ooa-1xgr17q')
    pages = int(last_page[-1].text) if len(last_page) else 1

    for page in range(pages):
        url = f'{base_url}&page={page+1}'
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')

        cars = soup.find_all('article', class_='ooa-yca59n e1oqyyyi0')
        for car in cars:

            img = car.find('img')['src'] if car.find('img') else None
            otomoto_url = car.find('a')['href'] if car.find('a') else None
            otomoto_id = car['data-id']
            otomoto_title = car.find('h1').text
            year = int(car.find(attrs={'data-parameter': 'year'}).text)
            mileage = int(car.find(attrs={'data-parameter': 'mileage'}).text.replace('km', '').replace(' ', ''))
            price = int(car.find('h3', class_='e1oqyyyi16 ooa-1n2paoq er34gjf0').text.replace(' ', ''))

            scrapped_offers.append({
                'otomoto_url': otomoto_url,
                'otomoto_id': otomoto_id,
                'otomoto_title': otomoto_title,
                'img': img,
                'production_year': year,
                'mileage': mileage,
                'price': price,
            })

    return scrapped_offers


def mark_offers_as_gone(spotted_offers, new_offers_to_compare, spotted_offers_to_compare):
    MISSING_HTML_PAGE_MARK_AS_GONE_LIMIT = 10
    offers_to_mark_as_gone = []
    offers_gone_in_a_row_counter = 0

    for i, spotted_offer in enumerate(spotted_offers_to_compare):
        if spotted_offer not in new_offers_to_compare and spotted_offers[i].date_disappeared is None:
            offers_to_mark_as_gone.append(spotted_offers[i])

    for i, offer in enumerate(offers_to_mark_as_gone):
        if i < len(offers_to_mark_as_gone) - 1:
            if offers_to_mark_as_gone[i + 1].id - offer.id == 1:
                offers_gone_in_a_row_counter += 1

    if offers_gone_in_a_row_counter < MISSING_HTML_PAGE_MARK_AS_GONE_LIMIT:
        for offer in offers_to_mark_as_gone:
            offer.date_disappeared = timezone.now()
            offer.save()
            print('offer disappeared', offer)


def spot_new_offers(new_offers_to_compare, spotted_offers_to_compare, new_offers, searched_offer):
    for i, new_offer in enumerate(new_offers_to_compare):
        if new_offer not in spotted_offers_to_compare:
            SpottedOffer.objects.create(
                user=searched_offer.user,
                searched_offer=searched_offer,
                otomoto_url=new_offer.get('otomoto_url'),
                otomoto_id=new_offer.get('otomoto_id'),
                otomoto_title=new_offer.get('otomoto_title'),
                brand=searched_offer.brand,
                model=searched_offer.model,
                img=new_offers[i].get('img'),
                production_year=new_offer.get('production_year'),
                mileage=new_offer.get('mileage'),
                price=new_offer.get('price'),
            )
            print('found new offer', new_offers[i])
