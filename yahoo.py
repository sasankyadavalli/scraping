import requests
from bs4 import BeautifulSoup

url = "https://in.finance.yahoo.com/losers?count=100&offset=100"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find('div', class_="Ovx(a) Ovx(h)--print Ovy(h)")
results.prettify()
rows = results.find_all('tr', class_='simpTblRow')
for row in rows:
    data = row.find_all('td')
    if(len(data)) > 0:
        print('symbol: ',data[0].text)
        print('name: ',data[1].text)
        print('price: ',data[2].text)
        print('change: ',data[3].text)
        print('% change: ',data[4].text)
        print('volume: ',data[5].text)
        print('avg volume: ',data[6].text)
        print('market cap: ',data[7].text)
        print('pe ratio: ',data[8].text)
    # output = row.find_all('td', class_='Va(m)')
    # for ele in output:
    #     a = ele.text.split("\n")
    #     print(a[0])

        # #print(ele)
        # symbol = ele.find(attrs={"aria-label": "Symbol"})
        # print(symbol)
        # print(ele.find(attrs={"aria-label": "Symbol"}))
        # name = ele.find(attrs={"aria-label": "Name"})
        # price = ele.find(attrs={"aria-label": "Price"})
        # change = ele.find(attrs={"aria-label": "Change"})
        # cent_change = ele.find(attrs={"aria-label": "% change"})
        # volume = ele.find(attrs={"aria-label": "Volume"})
        # avg_vol = ele.find(attrs={"aria-label": "Avg vol (3-month)"})
        # market_cap = ele.find(attrs={"aria-label": "Market cap"})
        # pe_ratio = ele.find(attrs={"aria-label": "PE ratio (TTM)"})
        # print("symbol: ",symbol)
        # print("name: ",name)
        # print("price: ",price)
        # print("change: ",change)
        # print("cent_change: ",cent_change)
        # print("volume: ",volume)
        # print("avg_vol: ",avg_vol)
        # print("market_cap: ",market_cap)
        # print("pe_ratio: ",pe_ratio)
    print("==================================================================")
#print(results)
#print(soup)