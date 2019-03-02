Local package check
=======================
Checks versions of packages on local machine, now prepare support matrices in a minute!

[![asciicast](https://asciinema.org/a/qiBeZaZtdyzT14WsZ6CR6QbSf.svg)](https://asciinema.org/a/qiBeZaZtdyzT14WsZ6CR6QbSf)

Menu
-----
```
usage: pkg-check.py [-h] [--input INPUT] [--output OUTPUT]

optional arguments:
  -h, --help       show this help message and exit
  --input INPUT    input file (contains package names)
  --output OUTPUT  output file (contains compared packages)
```

Usage
-------

This can be used without specifying `--input` parameter, this will take `input.txt` file by default -  
```
python pkg-compare.py --output output.txt
```

Further, this can be used with customizable parameter like,
```
python pkg-compare.py --input input2.txt --output output.txt
```

