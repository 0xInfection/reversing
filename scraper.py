import re, html, html2markdown, requests, random, os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

readmeurl = 'https://raw.githubusercontent.com/mytechnotalent/Reverse-Engineering-Tutorial/master/README.md'

# emulating a browser here
fheaders = {
    'User-Agent'        : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
    'Accept'            : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language'   : 'en-US,en;q=0.9',
    'Accept-Encoding'   : 'gzip, deflate, br',
    'Sec-Fetch-Mode'    : 'navigate',
    'Sec-Fetch-Dest'    : 'document',
    'Sec-Fetch-Site'    : 'none',
    'Sec-Fetch-User'    : '?1',
    'DNT'               : '1',
    'Connection'        : 'close'
}

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

def processfName(filen: str):
    '''
    Processes file names to convert them to files
    '''
    fm = filen.lower().replace(' ', '-').replace('-–-', '-').replace(
        '---', '-').replace(':', '').replace('.', '').replace(
        ',', '').replace('[', '').replace(']', '').replace('/', ''
        ).replace('"', '').replace('?', '').replace('&', '').replace('=', '')
    fm += '.md'
    return fm

def downloadImage(link: str):
    '''
    Downloads an image from a given URL
    '''
    filename = 'imgs/{}.jpg'.format(random.getrandbits(30))
    with open(filename, 'wb+') as imgf:
        imgf.write(requests.get(link, headers=fheaders).content)
    return filename

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
        ntag = soup.new_tag('img', src=downloadImage(lnk))
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
    dirname = 'pages/{}'.format(processfName(fname))
    toadd = '* [{}]({})'.format(fname, dirname)
    with open(dirname, 'w+') as wf:
        wf.write(html2markdown.convert(content))
    with open('SUMMARY.md', 'a') as wf:
        wf.write(toadd+'\n')

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
    # init summary.md
    with open("SUMMARY.md", 'w') as wf:
        wf.write('# Summary\n\n')
    # create images dir
    if os.path.exists('imgs/'):
        os.rmdir('imgs/')
    os.makedirs('imgs/')
    # visit raw URL
    print("Visiting homepage...")
    driver.get(readmeurl)
    grabLinks(driver.page_source)
    driver.quit()
