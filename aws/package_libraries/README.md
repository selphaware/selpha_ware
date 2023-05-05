To start again. Stop all docker containers in PowerShell, run the following command:

docker ps -aq | ForEach-Object {docker stop $_}

Then run package_libraies.bat again
