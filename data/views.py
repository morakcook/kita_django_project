from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def news_search(request):
    keyword = request.GET.get('q', '')
    news_list =[]

    if keyword:
        url = f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        for news_item in soup.find_all('a', class_='news_tit'):
            title = news_item.get('title')
            link = news_item.get('href')

            #관련 뉴스 아이템의 설명 추출
            description = news_item.find_next_sibling('div', class_='news_dsc').get_text(strip=True)
            news_list.append({'title': title, 'link': link, 'description': description})

    return render(request, 'data/newssearch.html', {'news_list': news_list})
