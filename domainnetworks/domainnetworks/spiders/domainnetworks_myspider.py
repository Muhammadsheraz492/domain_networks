import scrapy
import json

from pip._internal.utils import urls


class YourSpider(scrapy.Spider):
    name = 'myspider'
    custom_settings = {
        'FEEDS': {
            'domainnetworks2.json': {
                'format': 'json',
                'overwrite': True,
            },
        },
    }

    def start_requests(self):
        url = 'https://domainnetworks.com/elasticsearch/search'
        with open('payloads.json', 'r') as file:
            data = json.load(file)
        headers = {
            'authority': 'domainnetworks.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            # 'cookie': 'domainnetworks_live_u2main=us_domainnetworks_live_1713009247344x173870921006891170_1713009247350x795759194572729900; domainnetworks_live_u2main.sig=vo2d7QjhbEO4QFlHPJ_KEqdnnkc; domainnetworks_u1main=1713009247344x173870921006891170; _ga=GA1.1.1099251296.1713009249; _ga_FNFB358G15=GS1.1.1713023621.2.0.1713023621.0.0.0; arp_scroll_position=5028',
            'origin': 'https://domainnetworks.com',
            'referer': 'https://domainnetworks.com/',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'x-bubble-breaking-revision': '5',
            'x-bubble-fiber-id': '1713023628046x517002664547929340',
            'x-bubble-pl': '1713009663834x721',
            'x-bubble-r': 'https://domainnetworks.com/search',
            'x-requested-with': 'XMLHttpRequest',
        }

        for payload in data:

            yield scrapy.Request(
                url,
                method='POST',
                headers=headers,
                body=json.dumps(payload),
                callback=self.parse,
                dont_filter=True

            )

    def parse(self, response):
        # _data=json.loads(response.text)
        data={}

        Json_data = json.loads(response.text)
        json_data = Json_data['hits']['hits']
        print(len(json_data))
        for dat in json_data:
            print(dat)
            if dat['_source'].get('name_text') is not None:
               data['Company Name'] = dat['_source'].get('name_text', '')

               if dat['_source'].get('website_text', '') != '':
                   data['Website Url'] =f"https://{dat['_source'].get('website_text', '')}/"


               data['phone_text']=dat['_source'].get('phone_text', '') if '_source' in dat and 'phone_text' in dat['_source'] else ''
               data['Address']=dat['_source'].get('street_text', '') if '_source' in dat and 'street_text' in dat['_source'] else ''
               data['City']=dat['_source'].get('city_text', '') if '_source' in dat and 'city_text' in dat['_source'] else '',
               data['State']=dat['_source'].get('state_text', '') if '_source' in dat and 'state_text' in dat['_source'] else '',
               data['Postal Code']=dat['_source'].get('postal_code_text', '') if '_source' in dat and 'postal_code_text' in dat['_source'] else '',
               data['Url'] = f"https://domainnetworks.com/business-listing/{dat['_source']['bid_text']}" if '_source' in dat and 'bid_text' in  dat['_source'] else ''
               yield data

