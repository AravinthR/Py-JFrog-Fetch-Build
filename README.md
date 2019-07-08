# Py-JFrog-Fetch-Build

This is an small Python based utility to fetch the latest build information from JFrog for a particular repo and also download the JAR/WAR/ARTIFACT from JFrog for hosting. 

Basically a support script for your CI-CD pipeline orchestration

# Why this when we have the JFrog API's? 

This script is intended for the end-users who work on OSS version of JFrog Artifactory. The REST API capabilities are limited/restricted for OSS version of JFrog.

# What does this script do?

1. make a REST API call and get the list of builds from a particular repo. 
2. use the python libraies to sort the JSON data and extract the latest artifact information. 
3. make a REST API call and download the artifact, save it to the File System


# python packages 

I have used the packages which come along with Python installer. The same can be achieved by using pandas, bs4, and many more packages. But, I work from a restricted environment without internet connectivity. So, I have used lambdas, arraylist, dictonaries, json, requests to achieve the same.

#                 Feel free to enhance this code
 As mentioned, I haven't used any external/additional libraries which require installation outside of Python. I look forward to enhancement of this code in a similar fashion. Why use a custom package when you can code it yourself? :) 
