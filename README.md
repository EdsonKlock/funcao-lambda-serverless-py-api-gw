# Processo instalação serveeless

# istallar Node.js

https://nodejs.org/en

# Install serverless module via NPM:

https://www.serverless.com/framework/docs/getting-started

~ sudo npm install -g serverless

# Create a new serverless project
serverless

# Move into the newly created directory
~ cd your-service-name

# ao se logar no serverless
(base) ➜  ~ serverless logout
Serverless: You are already logged out
(base) ➜  ~ serverless       

Enable Serverless Dashboard to get enhanced monitoring, logs and secrets management: https://serverless.com/monitoring

Do you want to login/register to Serverless Dashboard? No

Do you want to deploy your project? No

Your project is ready for deployment

# confirmar versão 
~ serverless --version


# cria json
~ none da pasta npm init -y 

# istalar plugs vscode

~ serverless Snippets

~ sls-init-aws

# antes do deploy confirmar se AWS CLI esta configurado 

# consultar documentação 
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html

# configurar tudo no vscode, depois pronto 

comando ~ serverles deploy -v

ou ~ sls serverles deploy -v  (v retona informações do deply)



# deploy finalizado retorna resposta a baixo

(base) ➜  py-teste-api-hello serverless deploy
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Ensuring that deployment bucket exists
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service py-teste-api-hello.zip file to S3 (2.43 kB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
..............
Serverless: Stack update finished...
Service Information
service: py-teste-api-hello
stage: dev
region: us-east-1
stack: py-teste-api-hello-dev
resources: 23
api keys:
  None
endpoints:
  GET - https://yu0yivajff.execute-api.us-east-1.amazonaws.com/oi
  GET - https://yu0yivajff.execute-api.us-east-1.amazonaws.com/feriado
  GET - https://yu0yivajff.execute-api.us-east-1.amazonaws.com/tchau
functions:
  oi: oi
  feriado: feriado
  tchau: ttchau
layers:
  None
Serverless: Removing old service artifacts from S3...

This service is safe to upgrade to a v3 Serverless Framework release
Run "serverless upgrade --major" to upgrade
Check: https://github.com/serverless/serverless/releases/tag/v3.0.0 for list of all breaking changes
(base) ➜  py-teste-api-hello 














