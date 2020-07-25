from bs4 import BeautifulSoup
from requests import get
from time import sleep

counter = 0
links = []
while True:
    url = f"https://www.craigslist.org/about/best/all/index{counter}.html#page-top"
    try:
        s1 = BeautifulSoup(get(url).content, "html.parser")
        s2 = s1.find("table", {"class":"bestoftoc"})
        s3 = s2.find_all("tr")[1::]
        s4 = [row.find_all("td")[1].find("a")["href"] for row in s3]

        links.extend(s4)

        counter += 25

        print(f"DONE {url}")
        sleep(2)
    except:
        print(f"FUCKED UP {url}")
        break

script = open("data.js", "w")
script.write(f"var links = {links} \n\nexport default links")
