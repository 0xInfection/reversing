import re, html
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

readmeurl = 'https://raw.githubusercontent.com/mytechnotalent/Reverse-Engineering-Tutorial/master/README.md'

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

def processfName(filen: str):
    '''
    Processes file names to convert them to files
    '''
    fm = filen.lower().replace(' ', '-')
    fm = fm.replace('-–-', '-').replace('---', '-')
    fm = fm.replace(':', '').replace('.',
        '').replace(',', '').replace('[',
        '').replace(']', '').replace('/', '')
    fm += '.md'
    return fm

def processContent(source: str):
    '''
    Processes content for getting images and code properly
    '''
    # processing images
    soup = BeautifulSoup(source, 'html.parser')
    for img in soup.find_all('img'):
        if not img.get('data-delayed-url'):
            lnk = html.unescape(img.get('src'))
        else:
            lnk = html.unescape(img.get('data-delayed-url'))
        ntag = soup.new_tag('img', src=lnk)
        img.replaceWith(ntag)
    return soup.__str__()

def grabContent(pgsrc: str, fname: str):
    '''
    Grabs blog content off the linkedin page
    '''
    rex = r"<section class=\"article-body\" data-redirect-url=.+?>(<p>.*)</section><div class=(?:\"ugc-post-bar\"><h3 class=\"ugc-post-bar__published_by|\"author-info author-info__container)"
    patt = re.compile(rex, re.DOTALL | re.MULTILINE)
    content = processContent(re.search(patt, pgsrc).group(1))
    content = '<h1>{}</h1>{}'.format(fname, content)
    print('\n\n'+content+'\n\n')
    with open('pages/{}'.format(processfName(fname)), 'w+') as wf:
        wf.write(content)

def grabLinks(source: str):
    '''
    Grabs links to the linkedin site
    '''
    patt = re.compile(r'(?i)click\s\[[a-z]{4}\]\((.*?)\)', re.MULTILINE)
    fname = re.compile(r'(?i)^##\s*Lesson\s*\d{1,4}:.+?\((.*?)\)', re.MULTILINE)
    rexmatch = [i for i in patt.finditer(source)]
    rexname = [i for i in fname.finditer(source)]
    for match, name in zip(rexmatch, rexname):
        if match.group(1).startswith('https://www.linkedin.com/pulse/'):
            print("Visiting link:", match.group(1))
            driver.get(match.group(1))
            grabContent(driver.page_source, name.group(1))

if __name__ == '__main__':
    # visit raw URL
    print("Visiting homepage...")
    driver.get(readmeurl)
    grabLinks(driver.page_source)
    driver.quit()
