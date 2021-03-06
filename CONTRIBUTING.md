贡献代码指南
===============

baidupy 项目欢迎任何人提交 issue 和 Pull Requests 贡献代码，在您创建 Pull Requests 之前，请注意一下事项。

## 开发环境搭建

使用 `virtualenv` 创建和系统库隔离的 Python 开发环境，并安装所有依赖:

```bash
cd baidupy
virtualenv .
source bin/activate
python setup.py develop
```

为了方便测试，需要安装 nose, httmock 以及 tox:

```bash
pip install nose httmock tox
```

> Tips: 安装 [autoenv](https://github.com/kennethreitz/autoenv) 可以让您在进入 baidupy 文件夹时自动激活虚拟环境，省去每次手动执行 `source bin/activate`

## lint

baidupy 遵循 [PEP8](http://legacy.python.org/dev/peps/pep-0008/) 代码风格规范，您贡献的代码应当尽可能遵循 PEP8。
同时，您可以安装 `flake8` 并开启其 git hook 功能自动在每次 commit 之前 lint 代码。

```bash
pip install flake8
flake8 --install-hook
```

推荐的 git hook 配置为（文件路径为 baidupy/.git/hooks/pre-commit）：

```python
#!/usr/bin/env python
import sys
import os
from flake8.hooks import git_hook

COMPLEXITY = os.getenv('FLAKE8_COMPLEXITY', 10)
STRICT = os.getenv('FLAKE8_STRICT', True)
IGNORE = os.getenv('FLAKE8_IGNORE')
LAZY = os.getenv('FLAKE8_LAZY', False)


if __name__ == '__main__':
    sys.exit(git_hook(
        complexity=COMPLEXITY,
        strict=STRICT,
        ignore=IGNORE,
        lazy=LAZY,
        ))
```

## 自动化测试

在您完成对代码的改进和完善之后，请使用 tox 完成自动化测试，确保全部测试通过。

```bash
tox
```

baidupy 希望支持的 Python 版本有 2.7, 3.3, 3.4, 3.5, pypy 和 pypy3.
如果您的本地 Python 环境没有安装全面，请尽可能测试全面您已经安装的 Python 版本。
如您本地安装了 Python 2.7 和 Python 3.5，则运行：

```bash
tox -e py27,py35
```

如果出现测试失败，请检查您的修改过的代码或者检查测试用例的代码是否需要更新。

> Tips: 您可以使用 `nosetests --pdb` 在测试失败的时候自动进入 pdb 进行调试。

## Pull Requests

在您完成上述所有步骤后，您可以在 [baidupy](https://github.com/hunter007/baidupy.git) 项目上提交您的 Pull Requests.

在所有环节完成之后，wechatpy 项目成员会尽快 review 您的 Pull Requests，予以合并或和您进行进一步的讨论。

Thanks.
