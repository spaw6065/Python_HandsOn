# Get 2 Team player’s name and find the following:
# 1 Total no of players in 1 st team
# 2 1st team players name
# 3 Total no of players in 2nd team
# 4 2nd team players name
Team_1_players = list()
Team_2_players = list()
while True:
    Team_1_players.append(input("Enter team 1 player names"))
    print("Enter x to end and any key to continue")
    if input()=='x':
        break

while True:
    Team_2_players.append(input("Enter team 2 player names"))
    print("Enter x to end and any key to continue")
    if input()=='x':
        break

print("Total players in team 1",len(Team_1_players))
print("Total players in team 2",len(Team_2_players))
print("Names of Team 1 players",Team_1_players)
print("Names of Team 2 players",Team_2_players)


