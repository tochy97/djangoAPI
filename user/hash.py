import hashlib
from cryptography.fernet import Fernet
from datetime import datetime

def CreateHash(input):
    if isinstance(input, list):
        input = list(input)
    output = hashlib.sha3_512()
    for x in input:
        output.update(x.encode())
    output = output.hexdigest()
    return output

def NewUser(input):
    hash_input = [input["username"], input["password"]]
    input["hash"] = CreateHash(hash_input)
    id_input = [input["username"]]
    input["id"] = CreateHash(id_input)
    return input

def CheckUser(input):
    hash_input = [input["user"], input["password"]]
    input["hash"] = CreateHash(hash_input)
    return input