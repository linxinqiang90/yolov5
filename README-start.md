####train
```shell
python train.py --img-size 640 --batch-size 3 --epochs 600 --data jewelry.yaml --weights weights/yolov5l6.pt --single-cls
```

####resume
```shell
python train.py --img-size 640 --batch-size 5 --epochs 600 --data jewelry.yaml --resume runs/train/exp53/weights/last.pt --single-cls 
```

####inference
```shell
python detect.py --weight runs/train/exp45/weights/best.pt --source 1.jpg
```

####hyp 最佳超参训练(--evolve)
```shell
 python train.py --img 800 --batch-size 4 --epochs 50 --data jewelry.yaml --weights weights/yolov5m.pt --single-cls --evolve
```

####coco json to txt
```shell
python utils/cocojson2text.py --json_path ./dataset/jewelry/train_annotation_coco.json --save_path ./dataset/jewelry/labels/train/
python utils/cocojson2text.py --json_path ./dataset/jewelry/val_annotation_coco.json --save_path ./dataset/jewelry/labels/val/
```