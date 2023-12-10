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
    fname = f'inputs/te{args.day}.txt' if test else f'inputs/in{args.day}.txt'
    pyfile = f'py_days/prob_{args.day}_{n}.py'
    if os.path.exists(pyfile):
        subprocess.run(
            ['cat', fname,  '|', 'python', pyfile],
            shell=True,
        )


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
    parser.add_argument('-t', '--test',
                        action='store_true',
                        help='run test input only')

    args = parser.parse_args()

    if args.download:
        dwld_input(args.year, args.day)

    if args.second:
        print(f'=========== Day {args.day} problem 1')
        run_prob(args.day, 1, test=True)
        if not args.test:
            run_prob(args.day, 1)

    if args.first:
        print(f'=========== Day {args.day} problem 2')
        run_prob(args.day, 2, test=True)
        if not args.test:
            run_prob(args.day, 2)

