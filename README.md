# words counter service

The Service Receives a text input and counts the number of appearances for each word in the input.

The endpoint should be able to accept the input in 3 ways:
  * A simple string sent in the request.
 * A file path for a file in the server’s filesystem (the contents will be used as input).
  * A URL (the data returned from the URL will be used as input).

the service can process large files by process multiple lines of the file at a time as a chunk, we can reduce these operations.

## Prerequisites
Make sure you have installed all of the following prerequisites on your development machine:

* Docker
* Compose

## Quick Install



```bash
cd {project_path}
docker-compose up
```

## Lets Play

1. count words from simple string in body : 

```bash
curl --location --request POST 'http://0.0.0.0:5000/api/word/counter' \
--header 'Content-Type: application/json' \
--data-raw '{
    "word": "Hi! My name is(what?), my name is(who?), my name is Slim Shady"
}'
```

2. count words from file system path in body:  

```bash
curl --location --request POST 'http://0.0.0.0:5000/api/word/counter' \
--header 'Content-Type: application/json' \
--data-raw '{
    "word": "/var/www/app/bucket/test.txt"
}'
```


3. count words from url in body:  

```bash
curl --location --request POST 'http://0.0.0.0:5000/api/word/counter' \
--header 'Content-Type: application/json' \
--data-raw '{
    "word": "http://norvig.com/big.txt"
}'
```
4. search for word count if it exist ( try to insert words to get some data before you run queries) 

```bash
curl --location --request GET 'http://0.0.0.0:5000/api/word/statistics/{any_word}'
```


## Stack

* **Flask**
* **Redis DB** 
* **Pytest**






## License
[MIT](https://choosealicense.com/licenses/mit/)