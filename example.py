import datx

c = datx.City("c:/work/tiantexin/17mon/mydata4vipday4.datx")

print(c.find("8.8.8.258"))
print(c.find("255.255.255.255"))

d = datx.District("c:/work/tiantexin/framework/library/ip/quxian.datx")
print(d.find("123.181.153.72"))

d = datx.BaseStation("c:/work/tiantexin/17mon/station_ip.datx")
print(d.find("223.221.121.0"))