import re
import requests
import json
import csv
import bs4


def comment_fetch(page_url):

    try:
        page_response = requests.get(page_url)

        soup = bs4.BeautifulSoup(page_response.content, 'html5lib')

        alt_url = soup.find("link", attrs={"rel": "shortlink"})["href"]
        title = soup.find("h1", class_="entry-title").string

        page_id = alt_url.split('=')[1]

        api_url = f'https://fitgirl-repacks-site.disqus.com/count-data.js?1={page_id}%20http%3A%2F%2Ffitgirl-repacks.site%2F%3Fp%3D{page_id}'

        js_response = requests.get(api_url)
        js_body = str(js_response.content)
        pattern = re.compile(r'("comments":)(\d+)')
        comments = re.search(pattern, js_body).group(2)
        with open("data.csv", "a") as file:
            print(f'{title} {comments}')
            csv_writer = csv.writer(file)
            csv_writer.writerow([title, comments])
    except Exception:
        print('pass')


def initializer():
    for page_no in range(1, 31):
        url = f"https://fitgirl-repacks.site/all-my-repacks-a-z/?lcp_page0={page_no}#lcp_instance_0"
        response1 = requests.get(url)

        soup = bs4.BeautifulSoup(response1.content, "html5lib")

        ul = soup.find('ul', class_='lcp_catlist')
        for li in ul.children:
            site_url = li.a['href']

            print(site_url)
            comment_fetch(site_url)


initializer()
