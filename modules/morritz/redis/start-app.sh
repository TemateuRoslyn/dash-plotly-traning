cd ./app

# docker build --target dev . -t python
# docker run -it -v ${PWD}:/work python sh

docker build . -t merritz-app
docker run -it -p 5000:5000 --net redis merritz-app