for left in range(7):
  for right in range(left, 7): # notice that we start with left because 0,1 is same as 1,0 in a domino tile
    print("[" + str(left) + "|" + str(right) + "]", end=" ")
  print()


teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
  for away_team in teams:
    if home_team != away_team: # you can't play a team against itself
      print(home_team + " vs " + away_team) 