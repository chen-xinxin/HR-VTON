# 保存HR-VTON的复现
## Installation

Clone this repository:

```
git clone https://github.com/sangyun884/HR-VITON.git
cd ./HR-VITON/
```

Install PyTorch and other dependencies:

```
conda create -n {env_name} python=3.8
conda activate {env_name}
conda install pytorch torchvision torchaudio cudatoolkit=11.1 -c pytorch-lts -c nvidia
pip install opencv-python torchgeometry Pillow tqdm tensorboardX scikit-image scipy
```

## Dataset
We train and evaluate our model using the dataset from [VITON-HD: High-Resolution Virtual Try-On via Misalignment-Aware Normalization](https://github.com/shadow2496/VITON-HD).

To download the dataset, please check the following link https://github.com/shadow2496/VITON-HD.

We assume that you have downloaded it into `./data`.

## Inference

Here are the download links for each model checkpoint:

- Try-on condition generator: [link](https://drive.google.com/file/d/1XJTCdRBOPVgVTmqzhVGFAgMm2NLkw5uQ/view?usp=sharing)
- Try-on condition generator (discriminator): [link](https://drive.google.com/file/d/1T4V3cyRlY5sHVK7Quh_EJY5dovb5FxGX/view?usp=share_link)
- Try-on image generator: [link](https://drive.google.com/file/d/1T5_YDUhYSSKPC_nZMk2NeC-XXUFoYeNy/view?usp=share_link)
- AlexNet (LPIPS): [link](https://drive.google.com/file/d/1FF3BBSDIA3uavmAiuMH6YFCv09Lt8jUr/view?usp=sharing), we assume that you have downloaded it into `./eval_models/weights/v0.1`.

```python
python3 test_generator.py --occlusion --cuda {True} --test_name {test_name} --tocg_checkpoint {condition generator ckpt} --gpu_ids {gpu_ids} --gen_checkpoint {image generator ckpt} --datasetting unpaired --dataroot {dataset_path} --data_list {pair_list_textfile}
```

## Train try-on condition generator

```python
python3 train_condition.py --cuda {True} --gpu_ids {gpu_ids} --Ddownx2 --Ddropout --lasttvonly --interflowloss --occlusion
```

## Train try-on image generator

```python
python3 train_generator.py --cuda {True} --name test -b 4 -j 8 --gpu_ids {gpu_ids} --fp16 --tocg_checkpoint {condition generator ckpt path} --occlusion
```
This stage takes approximately 4 days with two RTX 3090 GPUs. Tested environment: PyTorch 1.8.2+cu111.

To use "--fp16" option, you should install apex library.

## License

All material is made available under [Creative Commons BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). You can **use, redistribute, and adapt** the material for **non-commercial purposes**, as long as you give appropriate credit by **citing our paper** and **indicate any changes** that you've made.

