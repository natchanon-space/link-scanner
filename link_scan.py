from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
import urllib.error
import sys

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

def is_valid_url(url: str) -> bool:
    """Check whether url is good link or not.
    Any error code except 403 (Permission Denied) is a bad link.

    Returns:
        True if the URL is OK, False otherwise
    """
    try:
        req = urllib.request.Request(url, method="HEAD")
        _ = urllib.request.urlopen(req)
    except urllib.error.HTTPError as error:
        if error.code != 403:
            return False
    return True

def invalid_urls(urllist: List[str]) -> List[str]:
    """Validate the urls in urllist.

    Returns:
        a new list containing the invalid or unreachable urls.
    """
    urls = []
    for l in urllist:
        if not is_valid_url(l):
            urls.append(l)
    return urls

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:  python3 link_scan.py [url]")
    else:
        url = sys.argv[1]
        urls = get_links(url)
        for l in urls:
            print(l)

        print()
        print("Bad Links:")
        for l in invalid_urls(urls):
            print(l)
