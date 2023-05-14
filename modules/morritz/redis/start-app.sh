cd ./app

docker build . -t merritz-app
docker run -it -p 5000:5000 --net redis merritz-app