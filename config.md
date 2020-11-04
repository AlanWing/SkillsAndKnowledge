# Bandwagon server
+ config
```python
{
    "server":"104.243.27.161",
    "mode":"tcp_and_udp",
    "server_port":12345,
    "local_port":1080,
    "password":"Long1997",
    "timeout":60,
    "method":"aes-256-gcm"
}
```
+ **ssh** 
```bash
ssh -p26709 root@104.243.27.161
```

+ **start shadowsocks service on server**
```
ssserver -c /etc/shadowsocks.json
```

+ **start shadowsocks service on local**
```
sslocal -c /etc/shadowsocks.json
```

