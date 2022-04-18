FROM --platform=amd64 node:14-bullseye-slim 

WORKDIR /app

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean 

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 5000

# CMD ["node", "index.js"]