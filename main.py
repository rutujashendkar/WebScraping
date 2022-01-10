import selenium_Library as se
import logging

# Variables
base_path = r"C:\Users\rutuj\Downloads"
company_name = 'Reliance'
from_date = '01-05-2020'
to_date = '08-01-2021'
chrome_driver_path = r'C:/Users/rutuj/OneDrive/Desktop/chromedriver.exe'
link = 'https://www.sebi.gov.in/sebiweb/home/HomeAction.do?doListing=yes&sid=3&ssid=14&smid=8'

if __name__ == '__main__':
    # Creating Directory
    download_path = se.create_directory(base_path, company_name)

    # Starts the driver
    driver = se.start_driver(download_path, chrome_driver_path)

    # Opens link
    se.open_link(driver, link)

    # Performs action
    se.company_search(driver, company_name,from_date,to_date)

    # Downloads documents
    se.download_documents(driver)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


