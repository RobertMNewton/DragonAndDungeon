from components.sprite import Sprite

class Terrain:
    # terrain tile sprites
    grass = Sprite("assets/grassland_textures/grass_grassy.png", trans_c=(255, 255, 255))
    grass_path_1 = Sprite("assets/grassland_textures/grass_path_1.png", trans_c=(255, 255, 255))
    grass_path_2 = Sprite("assets/grassland_textures/grass_path_2.png", trans_c=(255, 255, 255))
    grass_path_corner_1 = Sprite("assets/grassland_textures/grass_path_corner_1.png", trans_c=(255, 255, 255))
    grass_path_corner_2 = Sprite("assets/grassland_textures/grass_path_corner_2.png", trans_c=(255, 255, 255))
    grass_path_corner_3 = Sprite("assets/grassland_textures/grass_path_corner_3.png", trans_c=(255, 255, 255))
    grass_path_corner_4 = Sprite("assets/grassland_textures/grass_path_corner_4.png", trans_c=(255, 255, 255))
    grass_rock_big = Sprite("assets/grassland_textures/grass_rock_big.png", trans_c=(255, 255, 255))
    grass_rock_cluster_1 = Sprite("assets/grassland_textures/grass_rock_cluster_1.png", trans_c=(255, 255, 255))
    grass_rock_cluster_2 = Sprite("assets/grassland_textures/grass_rock_cluster_2.png", trans_c=(255, 255, 255))
    grass_rock_small = Sprite("assets/grassland_textures/grass_rock_small.png", trans_c=(255, 255, 255))
    grass_rock_tall = Sprite("assets/grassland_textures/grass_rock_tall.png", trans_c=(255, 255, 255))
    grass_skull = Sprite("assets/grassland_textures/grass_skull.png", trans_c=(255, 255, 255))


    # terrain tiles organised as list
    terrain_tiles = \
    [
        grass, grass_path_1, grass_path_2, grass_path_corner_1, grass_path_corner_2, grass_path_corner_3,
        grass_path_corner_4, grass_rock_big, grass_rock_cluster_1, grass_rock_cluster_2, grass_rock_small,
        grass_rock_tall, grass_skull
    ]

