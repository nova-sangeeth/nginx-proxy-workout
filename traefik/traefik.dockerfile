FROM traefik:v2.7
RUN mkdir -p /etc/traefik/acme \
  && touch /etc/traefik/acme/acme.json \
  && chmod 600 /etc/traefik/acme/acme.json 
RUN mkdir logs 
COPY ./traefik.yml /etc/traefik
