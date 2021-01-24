# TCP(Transmission Control Protocol)

+ Three-way handshake process

1. The sender starts the conversation with following:
```markdown
1. sequence number(seq=521): Generate randomly
2. Syn flag(SYN=1): To synchronize its sequence number.
3. maximum segment size(MSS=1460 Bytes)
4. Window size(window=14600 Bytes): Buffer capacity.
```

2. The reciever responses a package with following:
```markdown
1. Sequence number(Seq=2000):Generate randomly
2. Syn flag(SYN=1)
3. MSS(MSS=500B)
4. Window size(window=10000B)
5. Acknowlegement number(ACK no.=522):sender's sequence number + 1
6. ACK flag(ACK=1)
```

3. Sender's second package:
```markdown
1. sequence number(Seq=522)
2. Acknowledgement Number(Ack no.=2001)
3. ACK flag(ACK=1)
```