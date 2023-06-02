# Yolo_Label

1. data_split.py

1-1. ./images에 있는 사진들을 train, test, valid로 분류한다.


2. json_gen.py

2-1. data_split.py로 분류된 train, test, valid를(json) gt_json 으로 나타낸다. 

3. label_yolo.py

3-1. data_split.py ./labels에 있는 json파일과 ./images 에 있는 파일의 이름을 비교하여 동일한 모델을 찾는다.

3-2. 해당 모델이 minx,miny,maxx,maxy로 분류 되어 있는 bbox 모델일 경우에 yolo 형식의 txt 파일로 나타낸다.

3-3. cn이 1개일때만 사용해야한다.

