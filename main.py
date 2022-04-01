import requests
import json
response_API_best = requests.get("https://raider.io/api/v1/characters/profile?region=us&realm=Zul'jin&name=Konnenh&fields=mythic_plus_best_runs")
data_best = response_API_best.text
parse_json_best = json.loads(data_best)

def get_info_best():
    for i in range(0,10):
        name = parse_json_best["mythic_plus_best_runs"][i]["short_name"]
        level = parse_json_best["mythic_plus_best_runs"][i]["mythic_level"]
        clear = parse_json_best["mythic_plus_best_runs"][i]["clear_time_ms"]
        par = parse_json_best["mythic_plus_best_runs"][i]["par_time_ms"]
        score = parse_json_best["mythic_plus_best_runs"][i]["score"]
        affixes = parse_json_best["mythic_plus_best_runs"][i]["affixes"][0]["name"]
        print(name,level,clear,par,score,affixes)

# get_info_best()

response_API_alt = requests.get("https://raider.io/api/v1/characters/profile?region=us&realm=Zul'jin&name=Konnenh&fields=mythic_plus_alternate_runs")
data_alt = response_API_alt.text
parse_json_alt = json.loads(data_alt)

def get_info_alt():
    for i in range(0,10):
        name = parse_json_alt["mythic_plus_alternate_runs"][i]["short_name"]
        level = parse_json_alt["mythic_plus_alternate_runs"][i]["mythic_level"]
        clear = parse_json_alt["mythic_plus_alternate_runs"][i]["clear_time_ms"]
        par = parse_json_alt["mythic_plus_alternate_runs"][i]["par_time_ms"]
        score = parse_json_alt["mythic_plus_alternate_runs"][i]["score"]
        affixes = parse_json_alt["mythic_plus_alternate_runs"][i]["affixes"][0]["name"]
        print(name,level,clear,par,score,affixes)

# get_info_alt()

dungeon_names=[]
affixes_best = []
key_levels_best = []
scores_best = []
affixes_alt = []
key_levels_alt = []
scores_alt = []

for i in range(0,10):
    dungeon_names.append(parse_json_best["mythic_plus_best_runs"][i]["short_name"])
    affixes_best.append(parse_json_best["mythic_plus_best_runs"][i]["affixes"][0]["name"])
    key_levels_best.append(parse_json_best["mythic_plus_best_runs"][i]["mythic_level"])
    scores_best.append(parse_json_best["mythic_plus_best_runs"][i]["score"])
    affixes_alt.append(parse_json_alt["mythic_plus_alternate_runs"][i]["affixes"][0]["name"])
    key_levels_alt.append(parse_json_alt["mythic_plus_alternate_runs"][i]["mythic_level"])
    scores_alt.append(parse_json_alt["mythic_plus_alternate_runs"][i]["score"])

print(f"{dungeon_names}" f"\n{affixes_best}" f"\n{key_levels_best}" f"\n{scores_best}" f"\n{dungeon_names}" f"\n{affixes_alt}" f"\n{key_levels_alt}" f"\n{scores_alt}")

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

# print(baseline_completion_score(15))