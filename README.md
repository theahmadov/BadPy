# badpy (Created By Error)

badpy is a python package with modules required for hacking.

## Installation

Use the package manager pip3 to install badpy.

```bash
pip3 install badpy
```

## Usage

```python
dork(url,show) # dork module is finding websites admin panel
"""
show = True or False it means if show = True print brute force and outputs will be colorfully. Like [!][WARNING] will be yellow and [+] will be green... otherwise i mean if show=False these will just one output (the result). And noncolorfull. Even you can make result equal to string veriable. Look down for examples.
"""
locate(ip,cmd)
"""
ip = ip
cmd = command to get information about ip adress.
here is all commands :
countrycode : Country Code
country     : Country
region      : Region
city        : City
regionno    : RegionName
postal      : Postal Code (zip)
timezone    : Timezone
mobile      : Mobile
operator    : Operator (isp)
porxy       : Proxy
"""
```

### Google Dorking Module (1.0)
```python
from badpy import * # importing badpy module

# Option 1
dork("http://thesaderror.cf/",True) # with this module you can see brute force and output will be colorfull.
# Option 2
n = dork("http://thesaderror.cf/",False) # this is for make output simple. And you can make output equal to a veriable.
print(n)
```

### IP Information Gathering (1.1)
```python
from badpy import * # importing badpy module

print(locate("172.253.11.2","country"))
# for commands please look up
"""
here is all commands :
countrycode : Country Code
country     : Country
region      : Region
city        : City
regionno    : RegionName
postal      : Postal Code (zip)
timezone    : Timezone
mobile      : Mobile
operator    : Operator (isp)
porxy       : Proxy
"""
```

## Contact : 
Github  : [TheSadError](https://github.com/TheSadError/)\
Gmail   : syntaxerrorses@gmail.com

# Log :
```
[1.0] Dork Module
```
## License
[MIT](https://choosealicense.com/licenses/mit/)

# For Educational Purposes