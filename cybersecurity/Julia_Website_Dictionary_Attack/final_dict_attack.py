import threading
import mechanicalsoup
import time

class passAttempt(threading.Thread):
    kill_all = False
    matched_password = ''
    attempts = 0
    def __init__(self, word_list):
        threading.Thread.__init__(self)
        self.word_list = word_list

    def run(self):
        url = 'https://undauntedmettle.com/chapters/chapter-1/'
        with open(self.word_list, 'r') as f:
            for pw in f:
                if passAttempt.kill_all:
                    break
                else:
                    passAttempt.attempts += 1
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
                        passAttempt.kill_all = True
                        passAttempt.matched_password = pw
                        break

if __name__ == '__main__':
    startTime = time.time()
    threads = []

    # for ascii in range(65, 91):  # A - Z
    for ascii in range(65, 76):  # only A - L
        file = 'word_list\\word_list_' + chr(ascii) + '.txt'
        attempt_thread = passAttempt(file)
        threads.append(attempt_thread)
        attempt_thread.start()

    while threads:
        for thread in threads:
            if not thread.isAlive():
                threads.remove(thread)

    print('Happy hunting!')
    print(f'Password matched: { passAttempt.matched_password }')
    print(f'Password attempts: { passAttempt.attempts }')
    print('Time elapsed: {}'.format(time.time() - startTime))
