# Welcome to your CDK TypeScript project

This is a blank project for CDK development with TypeScript.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

## Useful commands

* `npm run build`   compile typescript to js
* `npm run watch`   watch for changes and compile
* `npm run test`    perform the jest unit tests
* `npx cdk deploy`  deploy this stack to your default AWS account/region
* `npx cdk diff`    compare deployed stack with current state
* `npx cdk synth`   emits the synthesized CloudFormation template
# SidhubLambda_API

To deploy this project from and create the appropriate layers, run the following 
`cd layers`
`mkdir python`
`cd python`
`pip3 install requests -t`
`cd ..`
`zip -r python.zip python`

The above installs dependencies that are not part of the Python runtime on AWS Lambda. Once the dependencies
are installed, change directories to project root directory and 
`cdk deploy`
