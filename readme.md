## Docker
### build
```sh
docker build -t compile-prompt .
```
### run
```sh
docker run --rm -v $(pwd):/app/host compile-prompt --input host/inputpath.txt --output host/outputpath.txt
```

## How to use
If you have a textfile with a path within curly braces, it will replace that with the contents of the file.
example

inputfile.txt:

```
here is a text file's contents:

{path/to/filetoimport.txt}

Do the following:
```

path/to/filetoimport.txt:

```
123
```

result:

outputfile.txt:

```
here is a text file's contents:

123

Do the following:
```
