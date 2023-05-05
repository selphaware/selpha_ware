Run package_libraries.bat which will prompt you for the single library to be installed.
This will generate a zip file in the output directory which can be uploaded to S3

---

To start again and ensure there are no container conflicts. Stop all docker containers in PowerShell, run the following command:

docker ps -aq | ForEach-Object {docker stop $_}

Then run package_libraies.bat again

---

If process is halted midway, run the following command:

docker rm -f lambda-packager-container

Then run package_libraies.bat again
