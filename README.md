# Python Django 示例程序
## 项目介绍
本项目是一个使用[Django](https://www.djangoproject.com/)框架编写的简单的[Python](https://www.python.org/)示例程序，目录结构：
```
.
|──── python_django
|  └──── ...
|──── Procfile
|──── README.md
|──── manage.py
|──── requirements.txt
└──── runtime.txt
```
## 项目要求
需要在项目中添加3个文件：

* `runtime.txt`
* `requirements.txt`
* `Procfile`

`runtime.txt`里面记录的是需要用到的运行时版本。到目前为止，coding的演示平台只支持Python（`2.4.4` - `3.4.1`）之间的版本，但是官方推荐使用 `Python-2.7.8` 和 `python-3.4.1`。本例中，使用的Python版本是`3.4.1`，`runtime.txt`中只写一行：
```
python-3.4.1
```

`requirements.txt`里记录的是项目中需要用到的Python依赖（到目前为止，coding使用`Setuptool 3.6`或者`Pip 1.5.6`来管理和解决Python依赖）。本例中，只使用了版本为`1.7`的Django，`requirements.txt`如下所示，也只有一行：
```
Django==1.7
```

有了Python运行时环境和项目需要的Python依赖，`Procfile`里是启动Django应用的命令，同样只有一行，本例中如下：
```bash
web: python manage.py runserver $VCAP_APP_HOST:$PORT
```
注：`web:`指明当前运行的进程的类型为web类型，请参考[Procfile文件介绍](http://docs.coding.io/references/procfile)；`$VCAP_APP_HOST`和`$PORT`是当前系统的环境变量，请参考[环境变量](http://docs.coding.io/references/env#vcap_app_host)。

本文档参考[Python 语言支持](http://docs.coding.io/languages/python)，最后更新于2015年4月15日。
## 本地测试

* 安装 [Python](https://www.python.org/) 和 [Virtualenv](https://pypi.python.org/pypi/virtualenv)，查看[参考文档](http://install.python-guide.org)。
* 执行下面命令创建一个 [Virtualenv](https://pypi.python.org/pypi/virtualenv) 并在里面启动项目：

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```
* 访问 <http://127.0.0.1:8000> 查看效果。