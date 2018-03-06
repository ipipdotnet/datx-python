# Python解析datx格式的示例

<pre><code>
import datx

# 查询地级市精度的IP库
c = datx.City("c:/work/tiantexin/17mon/mydata4vipday2.datx")
print(c.find("8.8.8.258"))
print(c.find("255.255.255.255"))

# 查询国内区县库
d = datx.District("c:/work/tiantexin/framework/library/ip/quxian.datx")
print(d.find("123.181.153.72"))

# 查询基站IP库
d = datx.BaseStation("c:/work/tiantexin/17mon/station_ip.datx")
print(d.find("223.221.121.0"))
</code></pre>