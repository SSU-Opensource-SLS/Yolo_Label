import os
import shutil
import json

# JSON 파일 경로
json_file_path = 'test_list.json'

# 원본 이미지 폴더 경로
source_folder = './images'

# 이동할 이미지 폴더 경로
destination_folder = './images_3'

# JSON 파일 열기
with open(json_file_path) as json_file:
    data = json.load(json_file)
    # JSON 데이터에서 이미지 파일 경로 추출하여 이동
    for image_file in data:
        source_file_path = os.path.join(source_folder, image_file)
        destination_file_path = os.path.join(destination_folder, image_file)
        shutil.move(source_file_path, destination_file_path)