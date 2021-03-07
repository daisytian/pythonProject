
import re
def versionCompare(v1, v2):
  v1_check = re.match("\d+(\.\d+){0,3}", v1)
  v2_check = re.match("\d+(\.\d+){0,3}", v2)
  if v1_check is None or v2_check is None or v1_check.group() != v1 or v2_check.group() != v2:
    return "版本号格式不对，正确的应该是x.x.x.x"
  v1_list = v1.split(".")
  v2_list = v2.split(".")
  v1_len = len(v1_list)
  v2_len = len(v2_list)
  if v1_len > v2_len:
    for i in range(v1_len - v2_len):
      v2_list.append("0")
  elif v2_len > v1_len:
    for i in range(v2_len - v1_len):
      v1_list.append("0")
  else:
    pass
  for i in range(len(v1_list)):
    if int(v1_list[i]) > int(v2_list[i]):
      if int(i) == int(3):
        return v1 + "与" + v2 + " 版本号一致，但是" + v1 + "比" + v2 + " 打包时间更近"
      return "版本号v1 "+v1+" 大"
    if int(v1_list[i]) < int(v2_list[i]):
        if int(i) == int(3):
          return v1+"与" + v2 +" 版本号一致，但是" +v2 +" 比" + v1 +" 打包时间更近"
        return "版本号v1 "+v1+" 小"
  return "版本号v1与版本号v2相等"
# 测试用例
print(versionCompare(v1="a.4.1", v2="3.6.1.20210302"))
print(versionCompare(v1="3.7.1.20210302", v2="3.6.1.20210302"))
print(versionCompare(v1="3.3.1.20210302", v2="3.6.1.20210302"))
print(versionCompare(v1="3.4.1.20210304", v2="3.4.1.20210302"))
#print(result)
