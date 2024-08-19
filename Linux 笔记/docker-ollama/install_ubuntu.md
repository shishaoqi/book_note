docker pull ubuntu:22.04


docker run -d -v -p 11430:11434 --name ubuntu220404-ollama ubuntu:22.04


docker run -d -v ./models:/root/.ollama -p 11430:11430 --name ubuntu220404-ollama ubuntu:22.04


docker run -it -d -v ./models:/root/.ollama -p 11430:11430 --name ubuntu220404-ollama ubuntu:22.04 /bin/bash


docker exec -it ubuntu220404-ollama bash