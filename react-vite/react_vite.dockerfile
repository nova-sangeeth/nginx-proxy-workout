FROM --platform=amd64 node:16-bullseye-slim 

ENV NODE_ENV development

WORKDIR /app

COPY package.json .

COPY yarn.lock .

RUN yarn install

COPY . .

EXPOSE 5173