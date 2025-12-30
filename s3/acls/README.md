## Create new bucket

```sh
aws s3api create-bucket --bucket acl-example-etnard --region us-east-1
```

## Turn off Block Public Access for ACLs

```sh
aws s3api put-public-access-block \
--bucket acl-example-etnard \
--public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=true,RestrictPublicBuckets=true"
```

## Check Block Public Access for ACLs

```sh
aws s3api get-public-access-block --bucket acl-example-etnard
```

## Change ownership controls

```sh
aws s3api put-bucket-ownership-controls \
--bucket acl-example-etnard \
--ownership-controls="Rules=[{ObjectOwnership=BucketOwnerPreferred}]"
```

## Check bucket ownersip controls

```sh
aws s3api get-bucket-ownership-controls --bucket acl-example-etnard
```

## Get cannonical user id for the account you want to add to ACL
### iam
```sh 
aws sts get-caller-identity \
--query Account \
--output text
```
### root
```sh 
aws s3api list-buckets \
--max-items 10 \
--page-size 10 \
--query Owner.ID \
--output text
```

## Change ACL to allow for access from another AWS account
### Can also pass in json with `--access-control-policy` instead 
```sh
aws s3api put-bucket-acl --bucket amzn-s3-demo-bucket --grant-full-control emailaddress=user1@example.com,emailaddress=user2@example.com --grant-read uri=http://acs.amazonaws.com/groups/global/AllUsers
```

## Get bucket ACL

```sh
aws s3api get-bucket-acl --bucket acl-example-etnard
```