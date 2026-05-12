import requests
from bs4 import BeautifulSoup

def search_incruit(keyword, pages):
    jobs = [] 
    
    for i in range(5):
        page = i * 30
        url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno={page}"
        # url_2 = f"https://www.saramin.co.kr/zf_user/search/recruit?search_area=main&search_done=y&search_optional_item=n&searchType=search&searchword={keyword}&recruitPage={page}"
        # url_3 = f"https://www.jobkorea.co.kr/Search?stext={keyword}&tabType=recruit&Page_No={page}"

        response = requests.get(url)
        response_2 = requests.get(url_2)
        response_3 = requests.get(url_3)

        soup = BeautifulSoup(response.text, "html.parser")
        lis = soup.find_all("li", class_="c_col")

        for li in lis:
            try: # 만약 구조가 다른 광고 게시물 등이 섞여 있을 때 에러가 나지 않도록 try-except로 감싸는 것이 좋습니다.
                company = li.find("a", class_="cpname").text.strip()
                title = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a").text.strip()
                location = li.find("div", class_="cl_md").find_all("span")[0].text.strip()
                link = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a").get("href")
                
                job_data = {
                    "company": company,
                    "title": title,
                    "location": location,
                    "link": link
                }
                jobs.append(job_data)
            
            except Exception as e:
                # 구조가 맞지 않는 태그(예: 빈 리스트나 배너)는 건너뜁니다.
                pass

    return jobs

# 실행 테스트
# print(search_incruit("파이썬", 2))