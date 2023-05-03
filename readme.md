## Docker
### build
```sh
docker build -t compile-prompt .
```

```sh
docker run --rm -v $(pwd):/app/host compile-prompt --input host/inputpath.txt --output host/outputpath.txt
```
or just run the sh script:

```sh
chmod +x promptcompiler.sh
```

```sh
./promptcompiler.sh
```

create a symbolic link to it so that you can run it anywhere with ```promptcompiler input.txt output.txt```
```sh
sudo ln -sf /path/to/your/promptcompiler.sh /usr/local/bin/promptcompiler
```
## How to use
If you have a textfile with a path within curly braces, it will replace that with the contents of the file.
example

inputfile.txt:

```
{path/to/filetoimport.txt}
```

path/to/filetoimport.txt:

```
123
```

result:

inputfile.txt:

```
123
```