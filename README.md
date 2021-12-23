# 🧨  RSubd v1.0

<h3> Script to scan subdomains of a domain </h3>
<br/>
</br>
<p align="center">
<img src="https://github.com/wrrulos/Imagenes-Github/blob/main/RSubd/1.PNG" title="RSubd">
</p>
<br/>

## 💻 Supported operating systems:

* ✅ Windows (8, 8.1, 10 and 11)
* ✅ Linux
* ✅ Termux

# 🔧 Installation 

```bash
# Clone the repository
$ git clone https://github.com/wrrulos/RSubd

# Go into the RSubd folder
$ cd RSubd

# Install the requirements
$ python3 -m pip install -r requirements.txt

```
# 🕹 Usage

```bash
$ python3 RSubd.py -h
usage: RSubd.py [-h] -d DOMAIN -l FILE [-s] [-sv LOGS_FILE]

Script to scan subdomains of a domain

options:
  -h, --help     show this help message and exit
  -d DOMAIN      Domain
  -l FILE        List of subdomains
  -s             Skip subdomains with the same ip
  -sv LOGS_FILE  Save the results to a file
  
```
Scan a domain using the subdomains list in the "default.txt" file
```
python3 RSubd.py -d facebook.com -l default.txt
```
Scan a domain using the subdomains list in the file "default.txt" and skip the subdomains with the same ips
```
python3 RSubd.py -d facebook.com -l default.txt -s
```
Scan a domain using the list of subdomains in the file "default.txt" and save the results in the file "logs.txt"
```
python3 RSubd.py -d facebook.com -l default.txt -sv logs.txt
```

## 📸 Screenshots

<img src="https://github.com/wrrulos/Imagenes-Github/blob/main/RSubd/2.PNG">

# Termux

<img src="https://github.com/wrrulos/Imagenes-Github/blob/main/RSubd/3.PNG">

## Licencia 

MIT License

Copyright (c) 2021 Pedro Vega

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

 
