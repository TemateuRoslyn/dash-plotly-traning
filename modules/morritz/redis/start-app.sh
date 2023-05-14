cd ./app

docker build --target dev . -t python
docker run -it -v ${PWD}:/work python sh

# /work # python --version
# Python 3.9.
