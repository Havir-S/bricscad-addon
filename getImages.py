import os

def getImages(directory):
    image_dict = {}
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            filename_lower = filename.lower()
            prefix = filename_lower.split('-')[0]
            if prefix not in image_dict:
                image_dict[prefix] = []
            image_dict[prefix].append('imgs/' + filename)
    return image_dict