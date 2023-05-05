@echo off
echo Building Docker image...
docker build -t lambda-packager .

echo Running Docker container...
docker run --name lambda-packager-container -d -v %cd%:/data -v %cd%/output:/output lambda-packager tail -f /dev/null

echo Enter the library to install:
set /p library=

echo Executing the shell script inside the Docker container...
docker exec lambda-packager-container /bin/bash /data/package_libraries_inside_docker.sh %library%

echo Copying the zip file to the local machine...
docker cp lambda-packager-container:/output/library_with_deps_%library%.zip %cd%/output/

echo Stopping and removing the Docker container...
docker rm -f lambda-packager-container

echo Done! The zip files are ready to be uploaded as Lambda layers.
