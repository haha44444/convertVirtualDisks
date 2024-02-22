### English | [中文简体](https://github.com/haha44444/convertVirtualDisks/blob/master/README_zh-cn.md)
# Virtual disk type batch conversion tool
* Convert via qemu-img (Important! You need to install the qemu-img tool and add environment variables!)
* Supports mutual conversion of the following files: vhd, vmdk, qcow2, raw, vhdx, qcow, vdi, qed

## Usage:
1. To install qemu-img, please search for the installation tutorial yourself.
2. Install python3.7 or later
3. `git clone https://github.com/haha44444/convertVirtualDisks.git`
4. Prepare the files to be converted and place them in the `convertDisks` folder
5. Start conversion: run the program `python convert.py`
6. The converted files will be output to the `convertedDisks` folder

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=haha44444/convertVirtualDisks&type=Date)](https://star-history.com/#haha44444/convertVirtualDisks&Date)
