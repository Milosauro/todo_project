### build dockerfile
docker-compose build

### run up compose server
docker-compose up -d

### shutdown container
docker-compose down -v

### run uvicorn
uvicorn app.main:app --host 0.0.0.0