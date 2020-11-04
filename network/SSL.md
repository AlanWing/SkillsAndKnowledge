+ SSL is an encryption-based security protocol, In 1999 SSL was updated to become TLS.
+ Some people still use SSL to refer to TLS, others use the term "SSL/TLS encryption".


+ TLS handshake
```markdown
1. client "Hello"   
    Client initiates the handshake by sending a "hello" message to the server, the message will include which TLS version the client supports, the cipher suites supported and "client random".

2. server "Hello"   
    To reply the client's message, the server will send a message which will contain the server's certificate, the cipher suit the server chosen according to the client's supports and "server random".

3. Authentication   
    The client will verify the server's certificate.

4. Premaster secret(预主密钥)    
    The client will send one more random string of bytes, "premaster secret", which is encrypted by public key and only can be decrypted by the private key of server.( The public key is token from the SSL certificate)

5. Private key used 
    The server will use the private key to decrypted the premaster secret.

6. Generate the session keys 
    Both clients and servers will generate the session keys using random string and premaster secret and they will be the same string.

7. Client is ready
    The client will send a "finished" message that is encrypted with a session key

8. Server is ready 
    The server will send a "finished" message that encrypted with a session key

9. Secure symmetric encryption achieved
    The handshake is completed, and communication continues using the session key.
```

+ symmetric encryption
Both sides use the same session keys after the connection, and the messages will be encrypted by session keys. However, the session keys are just temporary, which means it just work for the current session. In the next session, both sides will generate the new session keys.