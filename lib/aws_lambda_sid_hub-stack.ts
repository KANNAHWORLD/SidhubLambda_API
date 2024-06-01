import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as apigateway from 'aws-cdk-lib/aws-apigateway';
import * as ec2 from 'aws-cdk-lib/aws-ec2';


export class AwsLambdaSidHubStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);


    // Add packages not found on basic Lambda runtime by adding layers
    const requestsLayer = new lambda.LayerVersion(this, 'RequestsLayer', {
      code: lambda.Code.fromAsset('layers/python.zip'),
      compatibleRuntimes: [lambda.Runtime.PYTHON_3_11, lambda.Runtime.PYTHON_3_12]
    });

    // Create the lambda function by using the layer and code from the src folder
    const lambdaFunc = new lambda.Function(this, "LambdaFunc", {
      runtime: lambda.Runtime.PYTHON_3_11,
      handler: "main.handler",
      code: lambda.Code.fromAsset("./image/src"),
      memorySize: 1024,
      layers: [requestsLayer],
      timeout: cdk.Duration.seconds(280),
    });

    // For now this is commented out so that the code can run without docker
    // const dockerFunc = new lambda.DockerImageFunction(this, "DockerFunc", {
    //   code: lambda.DockerImageCode.fromImageAsset("./image"),
    //   memorySize: 2024,
    //   timeout: cdk.Duration.seconds(280),
    //   architecture: lambda.Architecture.X86_64,
    // });

    // Creates API Gateway function with the lambda function
    const api = new apigateway.LambdaRestApi(this, "SidHubAPI", {
      handler: lambdaFunc,
      proxy: false,
    });

    // Creates reosource /Projects
    const resources = api.root.addResource("Projects");

    // Creates resource /Projects/{project}, path parameter for the resource
    const project_type = resources.addResource("{project}")
    project_type.addMethod("POST");
  }
}