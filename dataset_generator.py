import hashlib
from effect_generators import *
from code_generators import *


def generate_random_hash(length: int = 64) -> str:
    """Generates a random hash of the specified length."""
    if length > 64:
        raise ValueError("The maximum length of a SHA256 hash is 64 characters.")
    random_string = str(random.getrandbits(256))
    full_hash = hashlib.sha256(random_string.encode()).hexdigest()
    return full_hash[:length]


def generate_random_ean13() -> str:
    """Generates a random 13-digit EAN code."""
    return str(random.randint(100000000000, 999999999999))


hash_length = 16  
dir_name = "qr_codes"
file_format = "jpeg"
files_count = 3
code_type = "qr" 


def generate_codes(hash_length: int, dir_name: str, file_format: str, files_count: int, code_type: str):
    os.makedirs(dir_name, exist_ok=True)  
    
    if code_type == "ean13":
        hash_function = generate_random_ean13
        gen_function = generate_EAN13

    elif code_type == "datamatrix":
        hash_function = generate_random_hash
        gen_function = generate_DataMatrix

    elif code_type == "qr":
        hash_function = generate_random_hash
        gen_function = generate_QR
        
    else:
        raise ValueError("Invalid code type. Allowed values: 'qr', 'ean13', 'datamatrix'.")

    for _ in range(files_count):
        encoding = hash_function()

        image = gen_function(encoding)
        image = image.convert('L')  # Convert to greyscale
        image = apply_random_effects(image) 
        
        file_name = f"{dir_name}/{encoding}.{file_format}"
        print(f"File created: {file_name}")
        image.save(file_name)

    print(f"{files_count} files have been created.")
