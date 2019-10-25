import os
import sys
import subprocess
from datetime import datetime
import argparse
import urllib.request
import time
from tqdm import tqdm

def instagram_scrape(target_accounts, basepath):
    for target_acc in tqdm(target_accounts):
        directory = basepath + '/' + target_acc
        if not os.path.exists(directory):
            os.makedirs(directory)
        command = ['instagram-scraper', str(target_acc), '-t', 'image', '-d', directory , '--latest', '-m', str(2)]
        p = subprocess.Popen(command, stdout=subprocess.PIPE)
        output, err = p.communicate()
        time.sleep(1)

def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', type=str, help='Output base path.', default='./outputs_'+str(datetime.now().strftime('%Y-%m-%d-%H')))
    parser.add_argument('-f', type=str, help='target accounts txt file', default='target_accounts.txt')
    # parser.add_argument('-m', type=str, help='max number of target page posts', default='10')
    return parser.parse_args(argv)

if __name__ == '__main__':
    
    args = parse_arguments(sys.argv[1:])

    target_accounts = list() # user1,user2,user3,...
    map_names = dict()

    with open('target_accounts.txt', 'r') as file:
        # file = file.read().replace('\n', ' ').replace(' ', '').split(',')
        for i in file:
            try:
                i = i.replace('\n', ' ').replace(' ', '').split(',')
                target_accounts.append(i[0])
                map_names[str(target_accounts)] = i[1]
            except Exception as e:
                print('Error : ', e)

    print('target accounts : ', target_accounts)

    instagram_scrape(target_accounts, args.o)

    # for key,value in map_names.items():
    #     os.rename(os.path.join(args.o, key), os.path.join(os.path.join(args.o, value)))
