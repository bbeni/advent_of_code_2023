import argparse
import os
import subprocess


def run(day, n=0):
    uiua_file = f'uiua_days/day{day}_{n}.ua'
    if n == 0:
        uiua_file = f'uiua_days/day{day}.ua'

    if os.path.exists(uiua_file):
        subprocess.run(['uiua', 'run', uiua_file], shell=True)
    else:
        print("\033[0;34mWarning:\033[0m didn't find " + uiua_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='run_uiua_day.py',
        description='Run a specfic problem of AOC',
        epilog='Good Luck! UIUA'
    )
    parser.add_argument('day', metavar='D',
                        type=int, help='day of the problem')
    parser.add_argument('-s', '--second',
                        action='store_false',
                        help='run only second problem')
    parser.add_argument('-f', '--first',
                        action='store_false',
                        help='run only first problem')
    args = parser.parse_args()

    ## just one file
    uiua_file_simple = f'uiua_days/day{args.day}.ua'
    if os.path.exists(uiua_file_simple):
        run(args.day)
    else:
        if args.second:
            run(args.day, 1)
        if args.first:
            run(args.day, 2)


