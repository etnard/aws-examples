# Website 1
## Create new bucket

```sh
aws s3 mb s3://cors-example-etnard
``` 

## Change Block Public Access

```sh
aws s3api put-public-access-block \
--bucket cors-example-etnard \
--public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=false,RestrictPublicBuckets=false"
```

## Check Block Public Access

```sh
aws s3api get-public-access-block --bucket cors-example-etnard
```

## Create a bucket policy
```sh
aws s3api put-bucket-policy --bucket cors-example-etnard --policy file://policy.json
```

## Turn on static website hosting

```sh
aws s3api put-bucket-website --bucket cors-example-etnard --website-configuration file://website.json
```

## Upload our index.html file and include a resource that would be cross-origin

```sh
aws s3 cp index.html s3://cors-example-etnard
```

## Go to the website
### Link changes depends on region, http://cors-example-etnard.s3-website`-`us-east-1.amazonaws.com might have to be a `.`
```sh
http://cors-example-etnard.s3-website-us-east-1.amazonaws.com
```

# Website 2

## Create new bucket

```sh
aws s3 mb s3://cors-policy-example-etnard
``` 

## Change Block Public Access

```sh
aws s3api put-public-access-block \
--bucket cors-policy-example-etnard \
--public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=false,RestrictPublicBuckets=false"
```

## Check Block Public Access

```sh
aws s3api get-public-access-block --bucket cors-policy-example-etnard
```

## Create a bucket policy
```sh
aws s3api put-bucket-policy --bucket cors-policy-example-etnard --policy file://bucket-policy.json
```

## Turn on static website hosting

```sh
aws s3api put-bucket-website --bucket cors-policy-example-etnard --website-configuration file://website.json
```

## Upload our index.js file and include a resource that would be cross-origin

```sh
aws s3 cp index.js s3://cors-policy-example-etnard
```

## Create Api Gateway with mock response and then test the endpoint

```sh
curl -X POST \
  -H "Content-Type: application/json" \
  https://hu78kj7je2.execute-api.us-east-1.amazonaws.com/prod/index
```

## Set CORS on bucket

```sh
aws s3api put-bucket-cors --bucket cors-example-etnard --cors-configuration file://cors.json
```

