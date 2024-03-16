import os
import re

def getImages(directory):
    image_dict = {}
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            filename_lower = filename.lower()
            prefix = filename_lower.split('-')[0]
            number_match = re.search(r'\d+', filename_lower)
            if number_match:
                number = int(number_match.group())
                if prefix not in image_dict:
                    image_dict[prefix] = []
                image_dict[prefix].append(('imgs/' + filename, number))
    # Sort images based on the number
    for prefix in image_dict:
        image_dict[prefix].sort(key=lambda x: x[1])
        image_dict[prefix] = [image[0] for image in image_dict[prefix]]
    return image_dict