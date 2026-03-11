docker build -t newschool-img .

docker run --rm \
-v $(pwd)/:/app/ \
-p 8000:8000 \
--name newschool-container \
--link newdb-container:newschool-container \
newschool-img