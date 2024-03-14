import configparser
import pyautogui

def read_config(filename='config.txt'):
    config = configparser.ConfigParser()
    config.read(filename)
    x_coord = int(config.get('Coordinates', 'x_coord'))
    y_coord = int(config.get('Coordinates', 'y_coord'))
    x_coord_center = int(config.get('Coordinates', 'x_coord_center'))
    y_coord_center = int(config.get('Coordinates', 'y_coord_center'))

    geometry_x = int(config.get('Coordinates', 'geometry_x'))
    geometry_y = int(config.get('Coordinates', 'geometry_y'))
    geometry_size_x = int(config.get('Coordinates', 'geometry_size_x'))
    geometry_size_y = int(config.get('Coordinates', 'geometry_size_y'))
    



    return x_coord, y_coord, x_coord_center, y_coord_center, geometry_x, geometry_y, geometry_size_x, geometry_size_y
