# Bandwagon server
+ config
```python
{
    "server":"104.243.27.161",
    "server_port":9702,
    "mode":"tcp_and_udp",
    "local_address":"127.0.0.1",
    "local_port":1080,
    "password":"Long1997",
    "timeout":60,
    "method":"chacha20-ieft-poly1305"
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

