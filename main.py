from bs4 import BeautifulSoup
import requests

# with open('C:\\Users\\ROY JAKE\\Desktop\\Pure_Projects\\Qrates\\index.html', 'r') as html_file:
#     content = html_file.read()
#     soup = BeautifulSoup(content, 'lxml')
#     ul_tags = soup.find_all('ul')
#     print(ul_tags[3])

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}


akan_html_text = requests.get('https://akannews.com/nnuro-a-y%ce%b5de-kanyan-nna-mu-nkitahodie-so-nsunsuanso-b%e1%b4%90ne-ne-ahintas%ce%b5m-a-%ce%b5w%e1%b4%90-ho/', headers=headers).text
soup = BeautifulSoup(akan_html_text, 'lxml')

header = soup.find('div', class_='entry-header')
header1 = header.find('h1').text
# header2 = header.find('h2').text


content = soup.find('div', class_='content-inner')
content1 = content.find_all('p')
with open('.\\scrapping.txt', 'a', encoding='utf-8') as scraping_document:
    scraping_document.write('\n' + '\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\' + '\n')
    scraping_document.write(header1 + '\n')
    # scraping_document.write(header2 + '\n')

    for p in content1:
        scraping_document.write( p.text + '\n')

print('scraping done')