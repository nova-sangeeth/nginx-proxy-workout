FROM nginx:1.18.0-alpine

RUN rm -v /etc/nginx/conf.d/default.conf

COPY ./default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]