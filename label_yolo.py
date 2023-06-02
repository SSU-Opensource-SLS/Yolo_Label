import json
import os
from PIL import Image

input_dir = "./output"
image_dir = "./images"
output_dir = "./labels"

# 경로가 존재하지 않으면 생성
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def preprocess_bbox(box, size):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x = (box[0] + box[2]) / 2.0
    y = (box[1] + box[3]) / 2.0
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = round(x * dw, 6)
    w = round(w * dw, 6)
    y = round(y * dh, 6)
    h = round(h * dh, 6)
    return (x, y, w, h)

# JSON 파일과 이미지 파일 매칭
json_files = [filename for filename in os.listdir(input_dir) if filename.endswith(".json")]

# 입력 디렉토리의 모든 JSON 파일에 대해 처리
for json_file in json_files:
    json_path = os.path.join(input_dir, json_file)
    image_file = os.path.splitext(json_file)[0] + ".jpg"
    image_path = os.path.join(image_dir, image_file)

    if os.path.exists(image_path):
        # JSON 파일 열기
        with open(json_path) as file:
            data = json.load(file)

        # 이미지 파일 크기 추출
        image = Image.open(image_path)
        width = int(image.size[0])
        height = int(image.size[1])

        # bbox 정보 추출 및 전처리
        bboxes = [preprocess_bbox(annotation["bbox"], (width, height)) for annotation in data["label_info"]["annotations"]]

        # 결과를 텍스트 파일로 저장
        output_filename = os.path.splitext(json_file)[0] + ".txt"
        output_path = os.path.join(output_dir, output_filename)
        with open(output_path, "w") as output_file:
            for idx, bbox in enumerate(bboxes):
                output_file.write(f"0 {bbox[0]} {bbox[1]} {bbox[2]} {bbox[3]}\n")

        print(f"Saved preprocessed bbox information for {json_file} as {output_filename}")
    else:
        print(f"Image file {image_file} does not exist.")