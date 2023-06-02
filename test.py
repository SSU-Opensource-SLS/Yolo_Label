import os

folder_path = "./labels"

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    with open(file_path, "r") as file:
        line = file.readline().strip()
        data = line.split()
        index = int(data[0])
        info = [float(x) for x in data[1:]]
        
        if index == 1 and any(x < 0 for x in info):
            print("File with index 1 and negative values:", filename)