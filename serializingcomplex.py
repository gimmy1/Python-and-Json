# Encoding Custom Types
# Here we will use Python's complex class as an example
import json
z = 3 + 8j
type(z) # "<class: complex>"

# json.dumps(z) # class complex is NOT Json serializable

# What to do? Well we can create a custom function and class to handle this! Yes! How?
def complex_encode(z):
    if isinstance(z, complex):
        return {"__complex__": True, "real": z.real, "imag": z.imag}
    else: # Otherwise we can handle this by ourselves
        type_name = z.__class__.__name__
        raise TypeError(f"Object of type {type_name} is Not Json serializable")

# We will then pass the function into the default function
function_encode = json.dumps(z, default=complex_encode) # {"__complex__": True, "real": z.real, "imag": z.imag}

# An alternative option is to subclass JSONEncoder
class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):
            return {"__complex__": True, "real": z.real, "imag": z.imag }
        else: # Allow the JSONEncoder class to deal with issues
            super().default(self, z)


class_encoder = json.dumps(z, cls=ComplexEncoder) # {"__complex__": True, "real": z.real, "imag": z.imag}
encoder = ComplexEncoder()
encoder.encode # {"__complex__": True, "real": z.real, "imag": z.imag}

# Decoding Custom Data Types
# A method, or hack, is to offer metadata.
# Why metadata? Because we can verify type in JSON and offer a solution. Otherwise we may be confused to the type
# For example - We will read in a complex_data.json with a "__complex__": True
def decode_complex(dct):
    if "__complex__" in dct:
        return complex(dct["real"], dct["imag"])
    return dct # otherwise return dct and offer no Decoding

# Everytime the load operator parses the arguments, you are given a moment to intercede and provide a custom solution
with open("complex_data.json") as data_file:
    data = data_file.read()
    z_decoded = json.loads(data, object_hook=decode_complex)

type(z_decoded) # "<class: list>
type(z_decoded[0]) # "<class: complex>"
