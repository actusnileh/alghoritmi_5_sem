FROM node:18-alpine

WORKDIR /frontend

RUN npm install -g pnpm

COPY package.json ./

RUN pnpm install

COPY . .

EXPOSE 3410
