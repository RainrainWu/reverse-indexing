curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"file":"example file 1"}' \
    http://localhost:5000/files

curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"file":"test file two"}' \
    http://localhost:5000/files

curl -X POST \
    -H "Content-Type: application/json; charset=UTF-8" \
    -d '{"file":"Hebräisch? for third poke"}' \
    http://localhost:5000/files

curl -X GET \
    -H "Content-Type: application/json" \
    -d '{"token":"file"}' \
    http://localhost:5000/files

curl -X GET \
    -H "Content-Type: application/json" \
    -d '{"token":"test"}' \
    http://localhost:5000/files