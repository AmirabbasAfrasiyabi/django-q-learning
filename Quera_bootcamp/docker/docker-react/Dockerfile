FROM node:20-alpine

RUN addgroup -S app && adduser -S app -G app

RUN mkdir -p /app && chown -R app:app /app

WORKDIR /app
RUN mkdir data
USER app


COPY --chown=app:app package*.json ./
RUN npm install

COPY --chown=app:app . .

ENV API_URL=http://localhost:3000
EXPOSE 3000

CMD ["npm", "start" ]

