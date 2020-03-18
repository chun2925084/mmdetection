# Recongnition on Parasite

Use MMdetection to recongnition the type of Parasite.

## Installation

Please refer to [INSTALL.md](docs/INSTALL.md) for installation and dataset preparation.

## Get Started

Please see [GETTING_STARTED.md](docs/GETTING_STARTED.md) for the basic usage of MMDetection.

## How to Run


### Setup

To packet the library

```
python setup.py install

```

### Train

Remember to change the path in config file in config/ 

Single GPU

```
python tools/train.py config/faster_rcnn_r50_fpn_1x.py

```

Multi GPUS

```
CUDA_VISIBLE_DEVICES=0,1 python tools/train.py config/faster_rcnn_r50_fpn_1x.py --gpu 2

```

### Test

```
python tools/test.py config/faster_rcnn_r50_fpn_1x.py work_dirs/faster_rcnn_r50_fpn_r50_1x/epoch_12.pth --eval bbox --out fileout.pkl

```

Show testing images ( Do not use --eval and --show at the same time )

```
python tools/test.py config/faster_rcnn_r50_fpn_1x.py work_dirs/faster_rcnn_r50_fpn_r50_1x/epoch_12.pth --show --out fileout.pkl

```

## License

This project is released under the [Apache 2.0 license](LICENSE).

## Contributing

We appreciate all contributions to improve MMDetection. Please refer to [CONTRIBUTING.md](.github/CONTRIBUTING.md) for the contributing guideline.


