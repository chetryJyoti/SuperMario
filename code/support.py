
# for importing files in a proper mannner in the game

import pygame
from os import walk

def import_folder(path):
    surface_list=[]
    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf=pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
            
    return surface_list

# def import_folder(path):
#     for info in walk(path):
#         print (info)
# import_folder('G:\PYGAME\Super_mario\graphics\character')