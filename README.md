# Py-JFrog-Fetch-Build

This is an small Python based utility to fetch the latest build information from JFrog for a particular repo and also download the JAR/WAR/ARTIFACT from JFrog for hosting. 

Basically a support script for your CI-CD pipeline orchestration

# Why this when we have the JFrog API's? 

This script is intended for the end-users who work on OSS version of JFrog Artifactory. The REST API capabilities are limited/restricted for OSS version of JFrog.

# What does this script do?

1. make a REST API call and get the list of builds from a particular repo. 
2. use the python libraies to sort the JSON data and extract the latest artifact information. 
3. make a REST API call and download the artifact, save it to the File System


#                 Feel free to enhance this code
