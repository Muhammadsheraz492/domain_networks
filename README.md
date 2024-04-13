# MySpider

MySpider is a web scraping tool built with Scrapy for extracting data from domainnetworks.com.

## Installation

1. Clone the repository:

git clone https://github.com/Muhammadsheraz492/domain_networks.git


2. Install the required dependencies:


## Usage

1. Modify `payloads.json` with your desired payloads for the POST requests.

2. Run the spider:


scrapy crawl myspider 

This will scrape the data and save it to `domainnetworks2.json`.

## Custom Settings

The spider is configured with custom settings to overwrite the output file and format it as JSON. You can modify these settings in the spider's code (`myspider/spiders/myspider.py`) if needed.

## Data Structure

The scraped data includes the following fields:

- Company Name
- Website URL
- Phone
- Address
- City
- State
- Postal Code
- URL

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
