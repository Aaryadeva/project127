from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:\Users\rajee\Desktop\game\project127\chromedriver.exe")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers = ["Proper name", "Distance", "Mass", "Radius"]
    star_data = []
    for i in range(0, 428):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for tr_tag in soup.find_all("th", attrs={"class", "headerSort"}):
            th_tags = tr_tag.find_all("th")
            temp_list = []
            for index, tr_tag in enumerate(th_tags):
                if index == 0:
                    temp_list.append(th_tags.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(th_tags.contents[0])
                    except:
                        temp_list.append("")
            star_data.append(temp_list)
    with open("scrapper_stars.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)
scrape()