# New Follower Twitter Bot | AWS Lambda + DynamoDB
A simple and fun way to learn how to use AWS Lambda and DynamoDB to host a twitter bot that sends direct messages to all your new twitter followers.

## Contents

- [Creating an AWS account](#creating-an-aws-account)
- [Creating twiiter bot](#creating-twiiter-bot)
	- [Twitter API Keys](#twitter-api-keys)
- [Necessary python packages](#necessary-python-packages)
	- [Tweepy](#tweepy)
	- [Boto 3](#boto-3)
- [Packaging for aws lambda deployment](#packaging-for-aws-lambda-deployment)
	- [Work with Virtual ENV](#work-with-virtual-env)
	- [Do it manually](#do-it-manually)
- [Deploying to AWS Lambda](#deploying-to-aws-lambda)
- [Contribution](#contribution)


### Creating an AWS account
Befor you get started, you'll need to get an [aws account](https://aws.amazon.com/) (assuming you don't already have one). I'm not going to sell you on aws. Amazon is highly capable of selling it to you, if they haven't already done so.

### Creating twiiter bot

For this repository we are assuming you can already setup (create) a basic twitter application. This entails going through twitter's application management portal in the [my apps](https://apps.twitter.com) page, setting up your application and getting your Consumer Key, Consumer Secret, OAuth Access Token, OAuth Access Token Secret, once your application has been setup.

If you're truly stuck and are a beginner, simply google **how to create a twitter app**. You should be up to speed in 5 minutes or less.

##### Twitter API Keys

Before getting started create a "keys.py" file in your keyStorage directory. In it insert the code below and replace the **XXX**'s with your relevant twitter application information. These keys can be found in your twitter application development settings under the [my apps](https://apps.twitter.com) page. 

```
keys = dict(
	consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX,
	consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX,
	access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX,
	access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
)
```

##### Note:
These keys are hidden and ignored by your git file to protect them and hence only store them on your local machine. Keeping these keys safe is your sole responsibility :cop: :lock: :running: :key:.

### Necessary python packages
This tutorial is built using several python packages, which are all easily installed using pip. Before getting started you will need the following packages:

##### Tweepy
Tweepy allows us to easily access the twitter API in a python friendly, well maintained package. To learn more you can read their [docs](http://docs.tweepy.org/en/v3.5.0/), or just install it and leave the reading to the :neckbeard:.

```
pip install tweepy
```

##### Boto 3
Boto 3 allows us to interact with dynamoDB through our aws account. To learn more you can read their [docs](http://boto3.readthedocs.io/en/latest/), or just install it already!!! :triumph:.

```
pip install boto3
```

### Packaging for aws lambda deployment
To zip files for python lambda, one cannot simply right click the directory and compress the folder. There are a number of ways to approach this, depending on how you are working. You can use virtual environments, or be a maverick :bow: and do things manually.

Given your lambda function and code is in a dir called "myLambdaDir" and your lambda handler is in a file called "lambda_handler.py", you can:

##### Work with Virtual ENV

```
cd ~/myLambdaDir

zip -9 myLambdaPackage.zip lambda_handler.py

cd $VIRTUAL_ENV/lib/python2.7/site-packages
zip -r9 ~/myLambdaDir/myLambdaPackage.zip *
cd $VIRTUAL_ENV/lib64/python2.7/site-packages
zip -r9 ~/myLambdaDir/myLambdaPackage.zip *
```

##### Do it manually
If you're on mac simply open your terminal and run:

```
$ python
```
Then:
```
>>>from distutils.sysconfig import get_python_lib
>>>print get_python_lib()
```

This command prints out a dir link to where you can find your systems site packages directory. mannually copy all the packages you're using within your bot's top level root directory (myLambdaDir).

Finally zip the entire package using the following command:

```
cd ~/myLambdaDir
zip -9 myLambdaPackage.zip lambda_handler.py

zip -r9 ~/myLambdaPackage.zip *
```
### Deploying to AWS Lambda
Deploying is as simple as uploading your zip file to your aws lambda function. How to create a lambda function is covered in detail through the available [AWS documentation](http://docs.aws.amazon.com/lambda/latest/dg/get-started-create-function.html).

### Contribution
Just sharing as I learn, I would appreciate any input on how to do this better, faster, or even "slicker". Lets teach as we learn.