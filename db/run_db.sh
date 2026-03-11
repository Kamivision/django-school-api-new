docker build -t db-img .

docker run -d --rm --name newdb-container db-img