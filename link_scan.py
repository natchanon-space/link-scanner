from typing import List
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def get_links(url: str) -> List[str]:
    """Find all links on page at the given url.

    Returns:
        a list of all unique hyperlinks on the page,
        without page fragments or query parameters.
    """
    driver = webdriver.Chrome()
    driver.get(url)
    a_tag = driver.find_elements(By.TAG_NAME, 'a')
    urls = set()
    for url in a_tag:
        url = str(url.get_attribute('href'))
        if url == "None":
            continue
        url = url.split("#")[0]
        url = url.split("?")[0]
        urls.add(url)
    driver.close()
    return list(urls)

if __name__ == "__main__":
    for l in get_links("https://cpske.github.io/ISP/"):
        print(l)
