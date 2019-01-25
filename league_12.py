import sys
longest = 4
teams = sys.stdin.readlines()
for team in teams:
   team = " ".join(team.split()[1:-8])
   if len(team) > longest:
      longest = len(team)

print("{:3s} {:<{}s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}".format("POS", "CLUB", longest, "P", "W", "D", "L", "GF", "GA", "GD", "PTS"))

for team in teams:
   team = team.split()
   print("{:>3s} {:{}s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}".format(team[0], " ".join(team[1:-8]), longest, team[-8], team[-7], team[-6], team[-5], team[-4], team[-3], team[-2], team[-1]))
