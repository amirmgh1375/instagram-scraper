import os
import sys
import subprocess
from datetime import datetime
import argparse
import urllib.request
import time
from tqdm import tqdm

def instagram_scrape(target_accounts, basepath, max_num_posts):
    for target_acc in tqdm(target_accounts):
        directory = basepath + '/' + target_acc
        if not os.path.exists(directory):
            os.makedirs(directory)
        command = ['instagram-scraper', str(target_acc), '-m', max_num_posts, '-t', 'image', '-d', directory]
        p = subprocess.Popen(command, stdout=subprocess.PIPE)
        output, err = p.communicate()
        time.sleep(1)

def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', type=str, help='Output base path.', default='./outputs_'+str(datetime.now().strftime('%Y-%m-%d-%H')))
    parser.add_argument('-m', type=str, help='max number of target page posts', default='10')
    return parser.parse_args(argv)

if __name__ == '__main__':
    
    args = parse_arguments(sys.argv[1:])

    target_accounts = [] # user1,user2,user3,...

    with open('target_accounts.txt', 'r') as file:
        file = file.read().replace('\n', ' ').replace(' ', '').split(',')
        for i in file:
            target_accounts.append(i)

    print('target accounts : ', target_accounts)

    instagram_scrape(target_accounts, args.o, args.m)

