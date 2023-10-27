# Interrups mit MicroPython

bitte [hier](https://docs.micropython.org/en/latest/reference/isr_rules.html) weiterlesen.

Tipps:

> * Keep the code as short and simple as possible.
> * Avoid memory allocation: no appending to lists or insertion into dictionaries, no floating point.
> * Consider using micropython.schedule to work around the above constraint.
> * Where an ISR returns multiple bytes use a pre-allocated bytearray. If multiple integers are to be shared between an ISR and the main program consider an array (array.array).
> * Where data is shared between the main program and an ISR, consider disabling interrupts prior to accessing the data in the main program and re-enabling them immediately afterwards (see Critical Sections).
> * Allocate an emergency exception buffer (see below).
