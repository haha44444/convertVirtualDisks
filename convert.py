# -*- coding: utf-8 -*-
import os


def start():
    global input_disk_type, output_disk_type, del_input_file
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
    print("https://github.com/haha44444/convertVirtualDisks")
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
    print("转换后是否删除转换前的文件")
    print("是:0   否:1")
    del_input_file_num = input()
    if del_input_file_num == "0":
        del_input_file = True
    else:
        del_input_file = False


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
    cmd = "qemu-img convert -p -f {0} -O {1} {3}{2}.{0} {4}{2}.{1}".format(input_disk_type, output_disk_type,
                                                                           disk_file_name, path1, path2)
    return cmd


def main():
    file_list = convert_disks_file_name_list()
    for i in range(len(file_list)):
        file_name = file_list[i]
        # 去除扩展名
        file_name_without_suffix = file_name.split(".", 1)[0]
        # 拼接完整命令
        convert_cmd = convert(file_name_without_suffix)
        # 开始转换
        os.system(convert_cmd)
        # 删除转换前文件
        if del_input_file == True:
            os.remove(convert_file_path + "/" + file_name_without_suffix + "." + input_disk_type)
            print("已删除转换前的文件")
        else:
            pass
        print("转换完成，转换后的磁盘文件输出到convertedDisks文件夹中")


if __name__ == '__main__':
    start()
    main()
