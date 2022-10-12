# 本地测试 Lambda 函数

- version 0 是原始版本
- 为了便于函数的调试，不要每次都安装 pytorch 等 package，因此创建了 version 1
- 这里仅对 version 1 进行说明

## version 1

首先进入 base_image 文件夹，构建基础镜像。后续如果有新的 python package 的需求，可以直接添加在 `pip install` 的后面。

```shell
docker build -t myruntime:base .
```

其次进入 pytorch_test 文件夹，构建函数镜像。

```
docker build -t myruntime:v1 .
```

在这个文件夹中注意的几点：

- Dockerfile 的基础镜像是前面一次的基础镜像。
- 将 `app.py` 添加到了工作路径中。
- CMD 中的 `app.handler` 其中，app指的是`app.py` ,`handler` 指的是`app.py`中的函数名。如果有需求可以进行替换与修正。

## 测试

在一个终端中run这个镜像。

```
docker run -p 9000:8080 myruntime:v1
```

另一个终端中发送函数的请求：

```
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```

应该可以看到类似的响应：

```
{"message": "Hello torch.Size([1, 2, 3])!"}
```

## TRAIN

使用 Lambda 进行模型训练的简单示例
