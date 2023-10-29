from customnetwork import customnetwork
customnetwork.start()

import mip
mip.install("pkg_resources")
mip.install("umqtt.simple")
mip.install("github:brainelectronics/micropython-i2c-lcd")
mip.install("github:pfalcon/picoweb/picoweb/__init__.py", target="lib/picoweb")
mip.install("github:pfalcon/picoweb/picoweb/utils.py", target="lib/picoweb")
mip.install("github:pfalcon/pycopy-lib/ulogging/ulogging.py")
mip.install("github:pfalcon/utemplate/utemplate/compiled.py", target="lib/utemplate")
mip.install("github:pfalcon/utemplate/utemplate/recompile.py", target="lib/utemplate")
mip.install("github:pfalcon/utemplate/utemplate/source.py", target="lib/utemplate")
mip.install("https://gitlab.com/WiLED-Project/ubutton/-/raw/master/ubutton.py")