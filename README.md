# 一键超人！

让你感受一键「自欺欺人」的快感！

![demo](./demo.png)

## 如何使用？

### 准备

1. 安装 [Python3](https://www.python.org/downloads/)
2. 安装 [Git](https://git-scm.com/downloads)
3. 在 GitHub 上创建一个新项目并 Clone 到本地，这里例如叫做 `one-click-man-hello-world`，并 Clone 到了 `~/one-click-man-hello-world`

### 安装并使用

```shell script
# 修改路径即可
repo_path="~/one-click-man-hello-world"

pip3 install --user git+https://github.com/thoxvi/one-click-man@master#egg=one-click-man --upgrade
# 执行
ocm $repo_path
# 等待漫长的写入
cd $repo_path && git push
# 一般需要半小时左右生效，请耐心等待
```

## 恢复

删除/隐藏目标项目即可。

## 最后

觉得有趣的话请给一颗 Star 哦～

`♪( ´▽｀)`
