import argparse
import subprocess
import os

def dwld_input(year, day):
    
    """session_cookie.txt should contain the cookie from your 
    browser of aoc website"""

    with open('session_cookie.txt') as f:
        cookie = f.readline().strip()

    site = f'https://adventofcode.com/{year}/day/{day}/input'
    out_file = f'inputs/in{day}.txt'

    if os.path.exists(out_file):
        with open(out_file) as f:
            if len(f.readlines()) > 2:
                return

    with open(out_file, 'w') as f:
        subprocess.run(
            ['curl', '--cookie', f'session={cookie}', site],
            stdout=f, shell=True
        )


def run_prob(day, n, test=False):

    te0 = f'inputs/te{args.day}.txt'
    te1 = f'inputs/te{args.day}_1.txt'
    te2 = f'inputs/te{args.day}_2.txt'
    in0 = f'inputs/in{args.day}.txt'

    
    '''heuristic what test input to take, specific files have higher prio.
       i.e. te_{day}_1.txt, te_{day}_2.txt > te.txt'''

    if not test:
        fname = in0
    elif n==1 and os.path.exists(te1):
        fname = te1
    elif n==2 and os.path.exists(te2):
        fname = te2
    else:
        fname = te0
    
    
    pyfile = f'py_days/prob_{args.day}_{n}.py'
    if os.path.exists(pyfile):
        subprocess.run(
            ['cat', fname,  '|', 'python', pyfile],
            shell=True,
        )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='run_py_day.py',
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
    parser.add_argument('-t', '--test',
                        action='store_true',
                        help='run test input only')
    parser.add_argument('-r', '--real',
                        action='store_true',
                        help='run real input only')

    args = parser.parse_args()

    if args.download:
        dwld_input(args.year, args.day)

    if args.second:
        print(f'=========== Day {args.day} problem 1')
        if not args.real:
            run_prob(args.day, 1, test=True)
        if not args.test:
            run_prob(args.day, 1)

    if args.first:
        print(f'=========== Day {args.day} problem 2')
        if not args.real:
            run_prob(args.day, 2, test=True)
        if not args.test:
            run_prob(args.day, 2)

