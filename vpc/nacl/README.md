# Create NACL
```sh
aws ec2 create-network-acl --vpc-id vpc-0c08208063fd93b91
```

# Add NACL Rule

```sh
aws ec2 create-network-acl-entry \
--network-acl-id acl-06a4c3141e930ad93 \
--ingress \
--rule-number 90 \
--protocol -1 \
--port-range From=0,To=65535 \
--cidr-block . . . \
--rule-action deny
```

# Get the latest AMI for Amazon Linux 2

```sh
aws ssm get-parameters \
--names /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 \
--region us-east-1 \
--query "Parameters[0].Value" \
--output text
```