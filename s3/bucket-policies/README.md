## Create new bucket

```sh
aws s3 mb s3://bucket-policy-example-etnard
``` 

## Create a bucket policy
### Replace `arn:aws:iam::123456789012:root` in `policy.json` with the arn from the other account
```sh
aws s3api put-bucket-policy --bucket bucket-policy-example-etnard --policy file://policy.json
```

## Get bucket policy

```sh
aws s3api get-bucket-policy --bucket bucket-policy-example-etnard
```