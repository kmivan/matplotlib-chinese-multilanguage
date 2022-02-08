# Matplotlib 的多语言支持

该包将自动为matplotlib包添加不同语言所需的字体。作为示例，本包已包含中文支持。

## 依赖库
- matplotlib
- yaml

如果你使用的是Anaconda发行版的python环境，那么这两个包是自带的。否则，你可以使用`pip`进行安装
```sh
pip install matplotlib
pip install pyyaml
```

## 使用方法
将`matplotlib_multilanguage`添加到工程目录下，在你的文件中添加如下代码
```python
from matplotlib_multilanguage import set_font

set_font()
```

## 工作原理
执行`set_font()`时，传入地区代号`lc`，默认值为`locale.getdefaultlocale()[0]`（即当前系统所在地区，例如中文中国的代号为'zh_CN'）。`set_font`函数将根据`lc`值从配置文件`fontmap.yaml`中读取对应的字体。

首先根据字体名`font-names`获取支持的字体。当支持的字体中没有我们想要的字体时，将在`<datapath>/font/ttf`中搜索字体文件`font-filenames`。

如果仍然找不到，则自动将附带的字体文件从`fonts`目录复制到`<datapath>/font/ttf`目录，然后重启程序，新的字体将生效。

## 示例
如`test.py`所示
