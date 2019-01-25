Local package check
=======================
Checks versions of packages on local machine, now prepare support matrices in a minute!

[![asciicast](https://asciinema.org/a/wNBnXQNNAq8hcS0fRFQyOVHL2.svg)](https://asciinema.org/a/wNBnXQNNAq8hcS0fRFQyOVHL2)

Menu
-----
```
usage: pkg_check.py [-h] [--input INPUT] [--output OUTPUT]

optional arguments:
  -h, --help       show this help message and exit
  --input INPUT    input file (contains package names)
  --output OUTPUT  output file (contains compared packages)
```

Usage
-------

This can be used without specifying `--input` parameter, this will take `input.txt` file by default -  
```
python pkg_compare.py --output output.txt
```

Further, this can be used with customizable parameter like,
```
python pkg_compare.py --input input2.txt --output output.txt
```

