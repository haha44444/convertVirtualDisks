# 虚拟磁盘类型批量转换工具
* 通过qemu-img进行转换（重要！需要安装qemu-img工具并添加环境变量！）
* 支持以下文件互转 vhd、vmdk、qcow2、raw、vhdx、qcow、vdi、qed

## 使用方法：
1. 安装qemu-img，请自行搜索安装教程
2. 安装python3
3. `git clone https://github.com/haha44444/convertVirtualDisks.git`
4. 准备要转换的文件，放在`convertDisks`文件夹中
5. 开始转换：运行程序 `python convert.py`
6. 转换后的文件会输出到`convertedDisks`文件夹中