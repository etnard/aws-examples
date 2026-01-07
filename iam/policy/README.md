# Install yq (Mike Farah)

```sh
curl -L https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 -o yq
sudo install -o root -g root -m 0755 yq /usr/local/bin/yq
```

# Convert to JSON
## Command
```sh
yq -o json policy.yaml > policy.json
```
## Bash Script
```sh
./update
```

# Create IAM Policy
```sh
aws iam create-policy \
--policy-name policy-example-s3 \
--policy-document file://policy.json
```

```sh
aws iam create-policy-version \
--policy-arn arn:aws:iam::. . .:policy/policy-example-s3 \
--policy-document file://policy.json \
--set-as-default 
```

```sh
aws iam attach-user-policy \
--user-name aws-examples \
--policy-arn arn:aws:iam::. . .:policy/policy-example-s3
```

# Delete IAM Policy

```sh
aws iam delete-policy-version --policy-arn arn:aws:iam::. . .:policy/policy-example-s3 --version-id v5
```