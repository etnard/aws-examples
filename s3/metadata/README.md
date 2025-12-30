## Create a new S3 bucket

```sh
aws s3 mb s3://metadata-examples-etnard
```

## Create a new file

```sh
echo "hello world" > hello.txt
```

## Upload file with metadata

```sh
aws s3api put-object --bucket metadata-examples-etnard --key hello.txt --body hello.txt --metadata Planet="Earth"
```

## Get metadata through head-object

```sh
aws s3api head-object --bucket metadata-examples-etnard --key hello.txt
```