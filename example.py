import datx

# 查询地级市精度的IP库
c = datx.City("/path/to/mydata4vipday2.datx")
print(c.find("8.8.8.258"))
print(c.find("255.255.255.255"))

# 查询国内区县库
d = datx.District("/path/to/quxian.datx")
print(d.find("123.121.117.72"))

# 查询基站IP库
d = datx.BaseStation("/path/to/station_ip.datx")
print(d.find("223.221.121.0"))