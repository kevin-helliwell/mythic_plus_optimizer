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

get_info_best()

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

get_info_alt()