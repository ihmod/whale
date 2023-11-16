import requests
import time
import random

bj = 'KQDZE'  # 邀请码

times = 12 # 邀请的人数，建议不要太多

def a():
    #  随机手机
    Phone_name = ["oppo-pedm00","oppo-peem00","oppo-peam00","oppo-x907","oppo-x909t",
                      "vivo-v2048a","vivo-v2072a","vivo-v2080a","vivo-v2031ea","vivo-v2055a",
                      "huawei-tet-an00","huawei-ana-al00","huawei-ang-an00","huawei-brq-an00","huawei-jsc-an00",
                      "xiaomi-mi 10s","xiaomi-redmi k40 pro+","xiaomi-mi 11","xiaomi-mi 6","xiaomi-redmi note 7",
                      "meizu-meizu 18","meizu-meizu 18 pro","meizu-mx2","meizu-m355","meizu-16th plus",
                      "samsung-sm-g9910","samsung-sm-g9960","samsung-sm-w2021","samsung-sm-f7070","samsung-sm-c7000",
                      "oneplus-le2120","oneplus-le2110","oneplus-kb2000","oneplus-hd1910","oneplus-oneplus a3010",
                      "sony-xq-as72","sony-f8132","sony-f5321","sony-i4293","sony-g8231",
                      "google-pixel","google-pixel xl","google-pixel 2","google-pixel 2 xl","google-pixel 3"]
    Phone = random.choice(Phone_name)

    #  邮箱的实现
    email = "".join(random.choice("1234567890") for i in range(10))
    xx = "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for i in range(4))
    email = email+'%40'+xx+'.com'  # 随机挑选十个数字和四个字母组成邮箱，其中数字可以改成字母

    data = 'passwd=e10adc3949ba59abbe56e057f20f883e&email='+email+'&invite_code='+bj  # 发送的内容，密码我就写的123456，想改自己MD5加密一下

    #  获取时间戳
    t = str(int(round(time.time() * 1000)))
    # 随机获取id
    id = "".join(random.choice("123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ") for i in range(32))

    # 拼接网页
    url = 'https://sm01.googls.net/account/register?' \
               'platform=2&api_version=14&' \
               'app_version=1.44&lang=zh&_key=&' \
               'market_id=1000&' \
               'pkg=com.bjchuhai&' \
               'device_id=rk_'+id+'&' \
               'model= '+Phone+'&' \
               'sys_version=7.1.2&' \
               'ts='+t+'&' \
               'sub_pkg=com.bjchuhai&' \
               'version_code=44'

    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '0',
        'Host': 'sm01.googls.net',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.5.0'
    }
    requests.post(url=url, data=data, headers=header)  # 发送post

if __name__ == '__main__':
    j=0
    for i in range(1, times+1):
        a()
        print("\n\t已邀请{}个人".format(i))
