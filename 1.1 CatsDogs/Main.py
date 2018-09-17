#Luis Ochoa
#80504534
#mw 10:30-12
import os
import random


def get_dirs_and_files(path):
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path + '/' + directory)]
    file_list = [directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory)]

    return dir_list, file_list


def classify_pic(path):
    # To be implemented by Diego: Replace with ML model
    if "dog" in path:
        return 0.5 + random.random() / 2

    return random.random() / 2


def process_dir(path):

    dir_list, file_list = get_dirs_and_files(path)

    cat_list = []
    dog_list = []

    # Your code goes here

    # listdir returns the files and folders in a file
    for each in os.listdir(path):
        #checking if its a file or another folder
        if os.path.isfile(os.path.join(path, each)):
            if ".jpg"  in each:
                #checks if its a picture file
                temp = classify_pic(os.path.join(path, each))
                #sorting based on the number returned by classify_pic
                if temp >= .5:
                    dog_list.append(os.path.join(path, each))
                else:
                    cat_list.append(os.path.join(path, each))
        else:
            #recursively calling if there is a folder in the path
            temp_list = process_dir(os.path.join(path,each))
            cat_list.extend(temp_list[0])
            dog_list.extend(temp_list[1])
    return cat_list, dog_list




def main():
    start_path = './' # current directory

    a,b = process_dir(start_path)
    for item in a:
        print (item)

    for items in b:
        print (items)
main()

