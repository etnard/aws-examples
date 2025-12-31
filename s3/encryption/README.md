## Create new bucket

```sh
aws s3 mb s3://encryption-example-etnard
``` 

## Create a file

```sh
echo "hello world" > file.txt
```

## Upload file with SSE-S3 encryption

```sh
aws s3 cp file.txt s3://encryption-example-etnard
```

## Put Object with SSE-KMS

```sh
aws s3api put-object --bucket \
encryption-example-etnard \
--key file.txt \
--body file.txt \
--server-side-encryption aws:kms \
--ssekms-key-id example-key
```

## Download file to test encyrption

```sh
aws s3 cp s3://encryption-example-etnard/file.txt copy.txt
```

## Put Object with SSE-C

```sh
export BASE64_ENCODED_KEY=$(openssl rand -base64 32) 
echo $BASE64_ENCODED_KEY
```

```sh
export MD5_VALUE=$(echo $BASE64_ENCODED_KEY | md5sum | awk '{print $1}' | base64 -w0)
echo $MD5_VALUE
```

```sh
aws s3api put-object --bucket \
encryption-example-etnard \
--key file.txt \
--body file.txt \
--sse-customer-algorithm AES256 \
--sse-customer-key $BASE64_ENCODED_KEY \
--sse-customer-key-md5 $MD5_VALUE
```

## Put Object with SSE-C via AWS-S3

```sh
openssl rand -out ssec.key 32
```

```sh
aws s3 cp file.txt s3://encryption-example-etnard/file.txt \
--sse-c AES256 \
--sse-c-key fileb://ssec.key
```

```sh
aws s3 cp s3://encryption-example-etnard/file.txt copy_2.txt \
--sse-c AES256 \
--sse-c-key fileb://ssec.key
```