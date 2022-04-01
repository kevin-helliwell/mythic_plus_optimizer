import requests
import json
response_API = requests.get("https://raider.io/api/v1/characters/profile?region=us&realm=Zul'jin&name=Konnenh&fields=mythic_plus_best_runs")
data = response_API.text
parse_json = json.loads(data)

scores = []

for i in range(10):
    my_best_runs = parse_json["mythic_plus_best_runs"][i]["score"]
    scores.append(my_best_runs)
print(scores)





# Dungeons in order (DOS, HOA, MOTS, NW, PF, SD, SOA, TOP, TSOW, TSG)
# dungeon_times = [43, 31, 30, 36, 38, 41, 39, 37, 38, 30]

# dungeon_dict = {
#     "DOS":43,
#     "HOA":31,
#     "MOTS":30,
#     "NW":36,
#     "PF":38,
#     "SD":41,
#     "SOA":39,
#     "TOP":37,
#     "TSOW":38,
#     "TSG":30,
# }

# def baseline_completion_score(key_level):
    
#     if(type(key_level)!=int or key_level<2):
#         return "Please enter a valid key level."
        
#     elif(key_level>=2 and key_level<5):
#         return 37.5 + 7.5*1 + 7.5*key_level
    
#     elif(key_level<=5 and key_level<7):
#         return 37.5 + 7.5*2 + 7.5*key_level
    
#     elif(key_level<=7 and key_level<10):
#         return 37.5 + 7.5*3 + 7.5*key_level
    
#     else:
#         return 37.5 + 7.5*3 + 15 + 7.5*key_level

# # for i in range(2,16):
# #     print(baseline_completion_score(i))

# def timer_score(time_completed, dungeon):
        