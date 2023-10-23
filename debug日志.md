### HR-VTON

报错`RuntimeError: Caught RuntimeError in pin memory thread for device 0.`

**解决方法**：把workers从4改成0，正确运行。

`ModuleNotFoundError: No module named 'torchgeometry'`

**解决方法**：`pip install torchgeometry`即可

`ModuleNotFoundError: No module named 'apex'`

**解决方法**：

```
git clone https://www.github.com/nvidia/apex
cd apex
python setup.py install
```

`ModuleNotFoundError: No module named 'IPython'`

**解决方法**：`conda install ipython`