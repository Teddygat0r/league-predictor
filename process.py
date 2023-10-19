import json

# Specify the path to your JSON file
json_file_path = 'esports-data/tournaments.json'
team_file_path = 'esports-data/teams.json'

# Open and read the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)
with open(team_file_path, 'r') as file:
    teams = json.load(file)

def getTeam(id): 
    for team in teams:
        if team["team_id"] == id:
            return team
    return None

# Iterate through the list of objects and print the "slug" property

print("\n\n\n\n")
print(data[0]["stages"][1]["sections"][0]["matches"][1]["teams"][0]["result"])
print(getTeam(data[0]["stages"][1]["sections"][0]["matches"][1]["teams"][0]["id"]))
print(data[0]["stages"][1]["sections"][0]["matches"][1]["teams"][1]["result"])
print(getTeam(data[0]["stages"][1]["sections"][0]["matches"][1]["teams"][1]["id"]))