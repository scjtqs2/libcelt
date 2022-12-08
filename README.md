# libcelt
celt-0.7.1 的c源码编译 

官方源码下载地址：https://www.celt-codec.org/downloads/

这里编译出来的产物主要是用于 golang的cgo调用。

# 编译方式
1. 使用官方源码自带的make方式：
```shell
# 使用root权限
sudo -i 
git clone https://github.com/scjtqs2/libcelt.git
cd libcelt/celt-0.7.1
# 确保你的环境具备编译工具make、gcc等
./configure
make
make install
```
2. 使用scons打包成静态依赖文件，方便golang的cgo调用，以及静态编译。
```shell
# 使用root权限
sudo -i 
git clone https://github.com/scjtqs2/libcelt.git
cd libcelt
# 安装 scons
apt install gcc scons -y
scons -f scons/scons_golang_celt_lib.py
# 生成 libcelt0.a 文件
cp libcelt0.a /usr/local/lib/  # 或者 /usr/lib/ 放入系统的依赖库存放的地方就行
```