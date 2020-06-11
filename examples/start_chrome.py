from chromepy.chrome import Chrome
from datetime import datetime
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-u', '--url', dest='url', help='Chrome url')
args = parser.parse_args()

chrome = Chrome.instance
chrome.get(args.url)

cmd = ''
while cmd.lower() != 'q':
    print('Chrome running ...')
    print('    ', datetime.now())
    print('    ', chrome.current_url)
    print('    ', chrome.command_executor._url)
    print('    ', chrome.session_id)
    cmd = input('Press (q) to quit chrome ... ')
    
chrome.quit()


