import json


map_data = {0: {}}

MAP_HORIZONTAL_TILES = 128
MAP_VERTICAL_TILES = 128

for x in range(-(MAP_HORIZONTAL_TILES // 2), MAP_HORIZONTAL_TILES // 2):
    map_data[0][x] = {}
    for y in range(-(MAP_VERTICAL_TILES // 2), MAP_VERTICAL_TILES // 2):
        map_data[0][x][y] = "grass"

json.dump(map_data, open("map.json", "w"))
