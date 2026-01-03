# Create a user with no permissions
### Create a user with no permissions

```sh
aws iam create-user --user-name sts-machine-user
aws iam create-access-key --user-name sts-machine-user --output table
```

### OPTIONAL: Copy the access key and secret access key here

**WARNING:** THIS WILL OVERWRITE THE DEFAULT PROFILE, GOTO NEXT STEP IF YOU **DO NOT** WANT TO DO THAT
```sh
aws configure
```

### Open and edit credentials file to create a new profile
**VSCODE**
```sh 
code ~/.aws/credentials
```
**OR IF IN REMOTE EVIROMENT**
```sh 
open ~/.aws/credentials
```
~/.aws/credentials:
```
[default]
aws_access_key_id = . . .
aws_secret_access_key = . . .
[sts-machine-user]
aws_access_key_id = . . .
aws_secret_access_key = . . .
```
### Check new profile

```sh
aws sts get-caller-identity --profile sts-machine-user
```

### Check if you have access to s3

```sh
aws s3 ls --profile sts-machine-user
```
> An error occurred (AccessDenied) . . . is not authorized to perform: s3:ListAllMyBuckets because no identity-based policy allows the s3:ListAllMyBuckets action

# Create a role
Create a role that will access a new resource

```sh
chmod u+x bin/deploy
./bin/deploy
```

# Use new user credentials and assume role

```sh
aws iam put-user-policy \
--user-name sts-machine-user \
--policy-name StsAssumePolicy \
--policy-document file://policy.json
```

```sh
aws sts assume-role \
--role-arn arn:aws:iam::[REMOVED ACCOUNT ID]:role/sts-examples-stack-StsRole-KZkHB9bNvWWr \
--role-session-name s3-sts-example \
--profile sts-machine-user
```

```sh
aws sts get-caller-identity --profile assumed
```

```sh
aws s3 ls --profile assumed
```
