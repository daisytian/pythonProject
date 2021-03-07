
import re
def versionCompare(v1, v2):
  v1_list = v1.split(".")
  v2_list = v2.split(".")
  for i in range(len(v1_list)):
    if int(v1_list[i]) > int(v2_list[i]):
      if int(i) == int(3):
        return v1 + " 与 " + v2 + " 版本号一致，但是" + v1 + " 比 " + v2 + " 打包时间更近"
      return "版本号v1 "+v1+" 大"
    if int(v1_list[i]) < int(v2_list[i]):
        if int(i) == int(3):
          return v1+" 与 " + v2 +" 版本号一致，但是" +v2 +" 比 " + v1 +" 打包时间更近"
        return "版本号v1 "+v1+" 小"
  return "版本号v1与版本号v2相等"
# 测试用例
print(versionCompare(v1="3.4.1.20210301", v2="3.6.1.20210302"))
print(versionCompare(v1="3.7.1.20210302", v2="3.6.1.20210302"))
print(versionCompare(v1="3.3.1.20210302", v2="3.6.1.20210302"))
print(versionCompare(v1="3.4.1.20210304", v2="3.4.1.20210302"))
