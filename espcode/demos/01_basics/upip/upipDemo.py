# see: https://docs.micropython.org/en/latest/reference/packages.html

import upip

upip.help()
#upip.install(package_or_package_list, [path])
upip.install("micropython-pystone_lowmem")
import pystone_lowmem
pystone_lowmem.main()