# -*- coding: utf-8 -*-
import os


def start():
    global input_disk_type, output_disk_type
    # 创建文件夹
    if not os.path.exists("./convertDisks"):
        os.mkdir("convertDisks")
    else:
        pass
    if not os.path.exists("./convertedDisks"):
        os.mkdir("convertedDisks")
    else:
        pass
    print("##################################################")
    print("虚拟磁盘类型批量转换工具")
    print("作者：haha44444")
    print("支持以下磁盘类型的转换")
    print("vhd、vmdk、qcow2、raw、vhdx、qcow、vdi、qed")
    print("##################################################")
    print("")
    print("")
    print("输入转换前的文件类型，必须为以下类型中的一种")
    print("vhd vmdk qcow2 raw vhdx qcow vdi qed")
    input_disk_type = input()
    print("输入转换后的文件类型，必须为以下类型中的一种")
    print("vhd vmdk qcow2 raw vhdx qcow vdi qed")
    output_disk_type = input()


def convert_disks_file_name_list():
    global convert_file_path
    # 要转换的虚拟磁盘文件所在的目录
    convert_file_path = './convertDisks'
    file_name = os.listdir(convert_file_path)
    return file_name


def convert(disk_file_name):
    # 不完整命令
    path1 = convert_file_path + "/"
    path2 = "./convertedDisks/"
    cmd = "qemu-img convert -p -f {0} -O {1} {3}{2}.{0} {4}{2}.{1}".format(input_disk_type, output_disk_type, disk_file_name, path1, path2)
    return cmd


def main():
    for i in range(len(convert_disks_file_name_list())):
        file_name = convert_disks_file_name_list()[i]
        # 去除扩展名
        file_name_without_suffix = file_name.split(".", 1)[0]
        # 拼接完整命令
        convert_cmd = convert(file_name_without_suffix)
        # 开始转换
        os.system(convert_cmd)


if __name__ == '__main__':
    start()
    main()
    print("转换完成，转换后的磁盘文件输出到convertedDisks文件夹中")
