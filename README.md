# Python Parse datx file 

## Installing
<pre>
<code>pip install ipip-datx</code>
</pre>
## Code Example
  <pre><code>
import datx
c = datx.City("/path/to/mydata4vipday2.datx")
print(c.find("8.8.8.258"))
print(c.find("255.255.255.255"))
  </pre></code>
Output for IP 8.8.8.8 Results
    <pre><code>
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
    "ANYCAST" // anycast
]
  </code>  </pre>

<pre><code>
# For China district datx file
d = datx.District("/path/to/quxian.datx")
print(d.find("123.121.117.72"))

# For China Base Station datx file
d = datx.BaseStation("/path/to/station_ip.datx")
print(d.find("223.221.121.0"))
</code></pre>