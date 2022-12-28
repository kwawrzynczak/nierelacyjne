docker run --name cassandra-1 -d cassandra:4
docker run --name cassandra-2 -d --link cassandra-1:cassandra cassandra:4 