
import pandas as pd
from datetime import date, timedelta



class Scraper:
    def __init__(self, url, report_date):
        self.url = url
        self.report_date = report_date

    def scrape(self):
        while True:
            try:
                df= pd.read_csv(self.url.format(today=str(self.report_date)))
                print('SAVING file')
                df.to_csv(f'apple_mobility_trends_{self.report_date}.csv')
                break
            except:
                print(f'No data available till {str(self.report_date)}')
                self.report_date = self.report_date - timedelta(days=1)
                print(f'\nChecking for {str(self.report_date)}')



if __name__ == '__main__':
    
    URL="https://covid19-static.cdn-apple.com/covid19-mobility-data/2210HotfixDev19/v3/en-us/applemobilitytrends-{today}.csv"
    report_date = date.today()
    
    sc=Scraper(
        url=URL,
        report_date=report_date
    )

    sc.scrape()