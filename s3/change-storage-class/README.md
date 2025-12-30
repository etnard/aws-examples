## Create a new S3 bucket

```sh
aws s3 mb s3://change-storage-class-examples-etnard
```

## Create a new file

```sh
echo "hello world" > hello.txt
```

# Upload file with different storage class

```sh
aws s3 cp hello.txt s3://change-storage-class-examples-etnard --storage-class STANDARD_IA
```

