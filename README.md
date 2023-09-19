# First_Machine_Learning_Project
My first ML Project

## Start Machine Learning Project
### Software & Account requirements
1. [Github Account](https://github.com/)
2. [Heroku Account](https://dashboard.heroku.com/)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT Cli](https://git-scm.com/downloads)
5. [GIT Documentation] (https://git-scm.com/docs/gittutorial) 

#### Creating virtual environment
```
conda create -p venv python==3.7 -y  ## to create in current folder
conda create -n venv python==3.7 -y  ## to create in software installed location folder
```
#### Activate environment
```
conda activate venv/
OR
conda activate venv
```
```
pip install -r requirements.txt
```
#### To add files to git
```
git add <file_name>
```
> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file


#### To check the git status
```
git status
```
#### To check all version maintained by git
```
git log
```
#### To create version/commit all changes by git
```
git commit -m "message"
```
#### To send version/changes to github
```
git push origin main
```
#### To check remote url
```
git remote -v
```  

To setup CI/CD pipeline in heroku we need 3 information

HEROKU_EMAIL = hemantkadam.737@gmail.com
HEROKU_API_KEY = <> # Add you Heroku Api key here
HEROKU_APP_NAME = ml-regression-appp


Build Docker Image
```
docker build -t <image_name>:<tagname>.
```
> Note : Image name for docker must be in lowercase

To list docker images
```
docker images
```


Run docker images
```
docker run -p 5000:5000 -e PORT=5000 f8dfdfjer454478
```

To check running containers in  docker
```
docker ps
```

To stop docker container
```
docker stop <container_id>
```
App deployed on Heroku Platform. We can check it on heroku platform.

```
python setup.py install
```
