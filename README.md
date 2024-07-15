# dyBlack404 Tool

## Coded By 0xdyBlack404
### 
### 
### 
### 
### 
### 
### 
### 

![Just Bg](https://backiee.com/static/wallpapers/1000x563/297788.jpg)

## Installation

install requests library from [requests](https://pypi.org/project/requests/) .

```bash
pip install requests
```

## Using 
<!-- start:code block -->

# Normal Scaning 

```bash
./dyBlack.py -u https://exampel/image?file=DYBLACK404 
```

# Add a number of ../

```bash
./dyBlack.py -u https://exampel/image?file=DYBLACK404 -l 15
```

# Add file to fuzz 

```bash
./dyBlack.py -u https://exampel/image?file=DYBLACK404 -f "/etc/passwd" 
```

# Add a keyword to the file

```bash
./dyBlack.py -u https://exampel/image?file=DYBLACK404 -f "/etc/passwd" -r "root"
```

# Add Null Byte bypass

```bash
./dyBlack.py -u https://exampel/image?file=DYBLACK404 -a "%00.jpg"
```

<!-- end:code block -->

| short flag | all flag  |
| :--------: | :-------: |
| -u         | --url     |
| -l         | --loop    |
| -f         | --file    |
| -r         | --respons |
| -a         | --add     |


