`evaluate.py`：计算SSIM、LPIPS、MSE（均方误差）和Inception Score等指标，对生成的图像与真实图像之间的差异进行评估，并将评估结果写入文件中（`lpips.txt`：记录每张预测图像的LPIPS分数；`eval.txt`：记录评估的结果，包括SSIM、MSE、LPIPS以及Inception Score的均值和标准差）

`cp_dataset.py`/`cp_dataset_test.py`：加载数据

`get_norm_const.py`：计算判别器拒绝的归一化常数

`get_parse_agnostic.py`：根据人体解析图，遮盖原始人物图像的手臂、躯干和颈部（像素值设为-）

`utils.py`：包含了一些工具函数

`networks.py`：定义试穿条件生成器的结构和一些基础网络

`network_generator.py`：定义试穿图像生成器和判别器

`train_generator.py`:训练试穿图像生成器

`test_generator.py`：测试试穿图像生成器

`train_condition.py`:训练试穿条件生成器

`test_condition.py`:测试试穿条件生成器