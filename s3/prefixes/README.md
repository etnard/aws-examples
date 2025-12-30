## Create a new S3 bucket

```sh
aws s3 mb s3://prefixes-examples-etnard
```

## Create a folder

```sh
aws s3api put-object --bucket prefixes-examples-etnard --key="hello/" 
```

## Create a lot of folders

```sh
aws s3api put-object --bucket prefixes-examples-etnard --key="epsilon/sandbox/delta/theta/kappa/kernel/epsilon/beta/kappa/binary/omega/beta/beta/omega/epsilon/epsilon/vector/beta/cipher/delta/omega/kernel/gamma/cipher/theta/sigma/lambda/entropy/lambda/entropy/epsilon/hash/zeta/alpha/eta/kernel/theta/vector/kernel/epsilon/kappa/zeta/kappa/binary/vector/runtime/gamma/lambda/gamma/sigma/zeta/epsilon/packet/sigma/kernel/zeta/omega/alpha/packet/theta/theta/beta/entropy/delta/eta/beta/runtime/entropy/packet/theta/hash/alpha/omega/theta/matrix/beta/delta/beta/hash/eta/epsilon/sandbox/runtime/zeta/epsilon/hash/runtime/vector/sigma/beta/epsilon/binary/kappa/packet/kernel/epsilon/cipher/eta/theta/packet/delta/binary/sigma/alpha/hash/gamma/eta/vector/beta/vector/gamma/beta/sigma/runtime/delta/gamma/kernel/kernel/kernel/runtime/beta/eta/sandbox/theta/epsilon/sandbox/gamma/kernel/beta/omega/cipher/eta/kernel/beta/gamma/binary/binary/runtime/theta/beta/kernel/kernel/theta/matrix/sigma/entropy/theta/kappa/epsilon/epsilon/epsilon/vector/zeta/eta/entropy/hash/packet/binary/hash/binary/b"
```