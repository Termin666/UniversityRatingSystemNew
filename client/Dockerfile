FROM node:18-alpine as base

ARG DEPLOY_ENV

ENV DEPLOY_ENV=${DEPLOY_ENV}


FROM base as builder

WORKDIR /app/

COPY . /app/

RUN npm install


FROM base as final

COPY --from=builder /app/node_modules/ /app/node_modules/
COPY . ./app/

RUN apk update && apk add --no-cache dos2unix && \
    find /app/src -type f -exec dos2unix {} \;

RUN sed -i -e 's/\r$//' /app/entrypoint.sh

WORKDIR /app/

RUN chmod -R 775 /app/entrypoint.sh

RUN addgroup -S app && \
    adduser -S app -G app -h /app -DH

RUN mkdir .npm/ node_modules/.cache/ && \
    chown app:app -R .npm/ && \
    chown app:app -R node_modules/.cache/



RUN ls -lar

RUN if [ ! -x /app/entrypoint.sh ]; then exit 1; fi
