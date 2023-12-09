import argparse
import subprocess
import importlib
import os

def dwld_input(year, day):
    
    """session_cookie.txt should contain the cookie from your 
    browser of aoc website"""

    with open('session_cookie.txt') as f:
        cookie = f.readline().strip()

    site = 'https://adventofcode.com/{}/day/{}/input'.format(year,day)
    out_file = 'inputs/in{}.txt'.format(day)

    try:
        with open(out_file) as f:
            if len(f.readlines()) > 2:
                return
    except: pass

    with open(out_file, 'w') as f:
        subprocess.run(
            ['curl', '--cookie', 'session={}'.format(cookie), site],
            stdout=f, shell=True
        )


def run_prob(day, n):
    fname = 'inputs/in{}.txt'.format(args.day)
    pyfile = 'py_days/prob_{}_{}.py'.format(args.day, n)
    if os.path.exists(pyfile):
        subprocess.run(['cat', fname,  '|', 'python', pyfile], shell=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='RunPyDays',
        description='Run a specfic python problem of AOC',
        epilog='Good Luck!'
    )
    parser.add_argument('year', metavar='Y',
                        type=int, help='advent of code year')
    
    parser.add_argument('day', metavar='D',
                        type=int, help='day of the problem')
    parser.add_argument('-d', '--download',
                        action='store_true',
                        help='download input file for this day')
    parser.add_argument('-s', '--second',
                        action='store_false',
                        help='run only second problem')
    parser.add_argument('-f', '--first',
                        action='store_false',
                        help='run only first problem')

    args = parser.parse_args()

    if args.download:
        dwld_input(args.year, args.day)

    if args.second:
        print(f'======= Day {args.day} solution to problem 1')
        run_prob(args.day, 1)
    if args.first:
        print(f'======= Day {args.day} solution to problem 2')
        run_prob(args.day, 2)