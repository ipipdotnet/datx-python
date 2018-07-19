# Python解析datx格式的示例 

## 安装说明
<pre>
<code>pip install ipip-datx</code>
</pre>
## 代码示例
<pre><code>
import datx

# 查询地级市精度的IP库
c = datx.City("/path/to/mydata4vipday2.datx")
print(c.find("8.8.8.258"))
print(c.find("255.255.255.255"))

#### Example
    <pre>
[
    "GOOGLE.COM", // country_name
    "GOOGLE.COM", // region_name
    "",             // city_name
    "google.com", // owner_domain
    "level3.com", // isp_domain
    "", // latitude
    "", // longitude
    "", // timezone
    "", // utc_offset
    "", // china_admin_code
    "", // idd_code
    "", // country_code
    "", // continent_code
    "IDC", // idc
    "", // base_station
    "", // country_code3
    "", // european_union
    "", // currency_code
    "", // currency_name
    "ANYCAST"
]
    </pre>

# 查询国内区县库
d = datx.District("/path/to/quxian.datx")
print(d.find("123.121.117.72"))

# 查询基站IP库
d = datx.BaseStation("/path/to/station_ip.datx")
print(d.find("223.221.121.0"))
</code></pre>