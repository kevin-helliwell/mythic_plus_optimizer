import requests
import json

# MAIN

response_API_best = requests.get("https://raider.io/api/v1/characters/profile?region=us&realm=Zul'jin&name=Konnenh&fields=mythic_plus_best_runs%3Aall")
data_best = response_API_best.text
parse_json_best = json.loads(data_best)

def get_info_best(dict):

    dict["name"] = parse_json_best["mythic_plus_best_runs"][0]["short_name"]
    dict["key_level"] = parse_json_best["mythic_plus_best_runs"][0]["mythic_level"]
    dict["clear_time_ms"] = parse_json_best["mythic_plus_best_runs"][0]["clear_time_ms"]
    dict["par_time_ms"] = parse_json_best["mythic_plus_best_runs"][0]["par_time_ms"]
    dict["score"] = parse_json_best["mythic_plus_best_runs"][0]["score"]
    dict["main_affix"] = parse_json_best["mythic_plus_best_runs"][0]["affixes"][0]["name"]
    
    if (dict["clear_time_ms"]/dict["par_time_ms"] <= 0.6):
            dict["stars"]=3
    elif(dict["clear_time_ms"]/dict["par_time_ms"] > 0.6 and dict["clear_time_ms"]/dict["par_time_ms"] <=0.8):
            dict["stars"]=2
    elif(dict["clear_time_ms"]/dict["par_time_ms"] > 0.8 and dict["clear_time_ms"]/dict["par_time_ms"] <= 1):
            dict["stars"]=1
    else:
            dict["stars"]=0
    return dict 

# print(get_info_best({}))

def get_info_worst(dict):
    dict["name"] = parse_json_best["mythic_plus_best_runs"][9]["short_name"]
    dict["key_level"] = parse_json_best["mythic_plus_best_runs"][9]["mythic_level"]
    dict["clear_time_ms"] = parse_json_best["mythic_plus_best_runs"][9]["clear_time_ms"]
    dict["par_time_ms"] = parse_json_best["mythic_plus_best_runs"][9]["par_time_ms"]
    dict["score"] = parse_json_best["mythic_plus_best_runs"][9]["score"]
    dict["main_affix"] = parse_json_best["mythic_plus_best_runs"][9]["affixes"][0]["name"]
    
    if (dict["clear_time_ms"]/dict["par_time_ms"] <= 0.6):
            dict["stars"]=3
    elif(dict["clear_time_ms"]/dict["par_time_ms"] > 0.6 and dict["clear_time_ms"]/dict["par_time_ms"] <=0.8):
            dict["stars"]=2
    elif(dict["clear_time_ms"]/dict["par_time_ms"] > 0.8 and dict["clear_time_ms"]/dict["par_time_ms"] <= 1):
            dict["stars"]=1
    else:
            dict["stars"]=0
    return dict

# print(get_info_worst({}))

# ALTERNATE

response_API_alt = requests.get("https://raider.io/api/v1/characters/profile?region=us&realm=Zul'jin&name=Konnenh&fields=mythic_plus_alternate_runs")
data_alt = response_API_alt.text
parse_json_alt = json.loads(data_alt)

def get_info_best_alt(dict):
    dict["name"] = parse_json_alt["mythic_plus_alternate_runs"][0]["short_name"]
    dict["key_level"] = parse_json_alt["mythic_plus_alternate_runs"][0]["mythic_level"]
    dict["clear_time_ms"] = parse_json_alt["mythic_plus_alternate_runs"][0]["clear_time_ms"]
    dict["par_time_ms"] = parse_json_alt["mythic_plus_alternate_runs"][0]["par_time_ms"]
    dict["score"] = parse_json_alt["mythic_plus_alternate_runs"][0]["score"]
    dict["main_affix"] = parse_json_alt["mythic_plus_alternate_runs"][0]["affixes"][0]["name"]
    
    if (dict["clear_time_ms"]/dict["par_time_ms"] <= 0.6):
            dict["stars"]=3
    elif(dict["clear_time_ms"]/dict["par_time_ms"] > 0.6 and dict["clear_time_ms"]/dict["par_time_ms"] <=0.8):
            dict["stars"]=2
    elif(dict["clear_time_ms"]/dict["par_time_ms"] > 0.8 and dict["clear_time_ms"]/dict["par_time_ms"] <= 1):
            dict["stars"]=1
    else:
            dict["stars"]=0
    return dict

# print(get_info_best_alt({}))

def get_info_worst_alt(dict):
    dict["name"] = parse_json_alt["mythic_plus_alternate_runs"][9]["short_name"]
    dict["key_level"] = parse_json_alt["mythic_plus_alternate_runs"][9]["mythic_level"]
    dict["clear_time_ms"] = parse_json_alt["mythic_plus_alternate_runs"][9]["clear_time_ms"]
    dict["par_time_ms"] = parse_json_alt["mythic_plus_alternate_runs"][9]["par_time_ms"]
    dict["score"] = parse_json_alt["mythic_plus_alternate_runs"][9]["score"]
    dict["main_affix"] = parse_json_alt["mythic_plus_alternate_runs"][9]["affixes"][0]["name"]
    
    if (dict["clear_time_ms"]/dict["par_time_ms"] <= 0.6):
            dict["stars"]=3
    elif(dict["clear_time_ms"]/dict["par_time_ms"] > 0.6 and dict["clear_time_ms"]/dict["par_time_ms"] <=0.8):
            dict["stars"]=2
    elif(dict["clear_time_ms"]/dict["par_time_ms"] > 0.8 and dict["clear_time_ms"]/dict["par_time_ms"] <= 1):
            dict["stars"]=1
    else:
            dict["stars"]=0
    return dict

# print(get_info_worst_alt({}))

def get_info_best_total():
    dict1={}
    dict2={}
    get_info_best(dict1)
    get_info_best_alt(dict2)
    dict3=[dict1,dict2]
    return dict3

print(get_info_best_total())

def get_info_worst_total():
    dict1={}
    dict2={}
    get_info_worst(dict1)
    get_info_worst_alt(dict2)
    dict3=[dict1,dict2]
    return dict3

print(get_info_worst_total())

# NOTE: FIND A WAY TO SEPARATE INTO TYRANNICAL AND FORTIFIED SPECIFIC LISTS

# for i in range(len(get_info_worst_total())):
#     print(get_info_worst_total()[i].get("main_affix"))
#     print(get_info_worst_total()[i].get("score"))


















































# def get_info_alt():
#     for i in range(0,10):
#         name = parse_json_alt["mythic_plus_alternate_runs"][i]["short_name"]
#         level = parse_json_alt["mythic_plus_alternate_runs"][i]["mythic_level"]
#         clear = parse_json_alt["mythic_plus_alternate_runs"][i]["clear_time_ms"]
#         par = parse_json_alt["mythic_plus_alternate_runs"][i]["par_time_ms"]
#         score = parse_json_alt["mythic_plus_alternate_runs"][i]["score"]
#         affixes = parse_json_alt["mythic_plus_alternate_runs"][i]["affixes"][0]["name"]
#         print(name,level,clear,par,score,affixes)

# get_info_alt()

# dungeon_names=[]
# affixes_best = []
# key_levels_best = []
# scores_best = []
# affixes_alt = []
# key_levels_alt = []
# scores_alt = []

# for i in range(0,10):
#     dungeon_names.append(parse_json_best["mythic_plus_best_runs"][i]["short_name"])
#     affixes_best.append(parse_json_best["mythic_plus_best_runs"][i]["affixes"][0]["name"])
#     key_levels_best.append(parse_json_best["mythic_plus_best_runs"][i]["mythic_level"])
#     scores_best.append(parse_json_best["mythic_plus_best_runs"][i]["score"])
#     affixes_alt.append(parse_json_alt["mythic_plus_alternate_runs"][i]["affixes"][0]["name"])
#     key_levels_alt.append(parse_json_alt["mythic_plus_alternate_runs"][i]["mythic_level"])
#     scores_alt.append(parse_json_alt["mythic_plus_alternate_runs"][i]["score"])

# print(f"{dungeon_names}" f"\n{affixes_best}" f"\n{key_levels_best}" f"\n{scores_best}" f"\n{dungeon_names}" f"\n{affixes_alt}" f"\n{key_levels_alt}" f"\n{scores_alt}")

def baseline_completion_score(key_level):

    if(type(key_level)!=int or key_level<2):
        return "Please enter a valid key level."

    elif(key_level>=2 and key_level<5):
        return 0.6667*(37.5 + 7.5*1 + 7.5*key_level)

    elif(key_level>=5 and key_level<7):
        return 0.6667*(37.5 + 7.5*2 + 7.5*key_level)

    elif(key_level>=7 and key_level<10):
        return 0.6667*(37.5 + 7.5*3 + 7.5*key_level)

    else:
        return 0.6667*(37.5 + 7.5*3 + 15 + 7.5*key_level)

# time_ratio = worst_run_dict.get("clear_time_ms")/worst_run_dict.get("par_time_ms")
# def time_bonus_score():
    
#     if(time_ratio<=0.6):
#         return 7.5
#     elif(time_ratio>0.6 and time_ratio<=1):
#         return 7.5*(time_ratio)
#     elif(time_ratio>1 and time_ratio<=1.4):
#         return 15*(time_ratio-1)
#     else:
#         return 0
    