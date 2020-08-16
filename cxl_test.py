import os
import re

if __name__ == '__main__':
    path  = 'c/wer/dasdfasd'
    pos = path.rfind('/')
    dir_search = re.compile(r''+path[:pos]+'(.*)')
    match = dir_search.search(path)
    if match:
        print('yes')
        print(match.group(1))
