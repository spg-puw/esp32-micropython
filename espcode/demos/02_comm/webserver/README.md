# Webserver

## PicoWeb Framework

Das PicoWeb Framework kann benutzt werden, es müssen die Abhängigkeiten wie folgt installiert werden:

```python
import mip
mip.install("github:pfalcon/picoweb/picoweb/__init__.py", target="lib/picoweb")
mip.install("github:pfalcon/picoweb/picoweb/utils.py", target="lib/picoweb")
mip.install("github:pfalcon/utemplate/utemplate/compiled.py", target="lib/utemplate")
mip.install("github:pfalcon/utemplate/utemplate/recompile.py", target="lib/utemplate")
mip.install("github:pfalcon/utemplate/utemplate/source.py", target="lib/utemplate")
mip.install("github:pfalcon/pycopy-lib/ulogging/ulogging.py")
```
