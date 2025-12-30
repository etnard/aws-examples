## Create a new S3 bucket

```md
aws s3 mb s3://checksums-examples-etnard
```

## Create a file to do a checksum on

```
echo "hello world" > myfile.txt
```

## Get the checksum for MD5
# 6f5902ac237024bdd0c176cb93063dc4  myfile.txt
```
md5sum myfile.txt
```

## Upload our file to s3 and look at its etag
# "ETag": "\"6f5902ac237024bdd0c176cb93063dc4\"",
```
aws s3 cp myfile.txt s3://checksums-examples-etnard
aws s3api head-object --bucket checksums-examples-etnard --key myfile.txt
```

## Lets upload a file with a different type of checksum
# af083b2d
# rwg7LaA=

```
bundle exec ruby crc.rb myfile.txt
echo af083b2d | perl -e 'print pack("H*", <STDIN>)' | base64
```

```
aws s3api put-object \
  --bucket checksums-examples-etnard \
  --key myfilecrc32.txt \
  --body myfile.txt \
  --checksum-algorithm CRC32 \
  --checksum-crc32 rwg7LQ==
```