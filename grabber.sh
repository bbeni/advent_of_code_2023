AOC_COOKIE="..." # get this from the cookies tab in network tools on the AOC website
YEAR="2023"
DAY="9"
echo $DAY
echo $YEAR
curl --cookie "session=$AOC_COOKIE" https://adventofcode.com/$YEAR/day/$DAY/input > in.txt
#curl --cookie "session=$AOC_COOKIE" "$(echo `date +https://adventofcode.com/%Y/day/%d/input` | sed 's/\/0/\//g')" > in.txt