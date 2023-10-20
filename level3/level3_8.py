def decode_string(encoded_string):
    parts = encoded_string.split('0')
    first_name = parts[0]
    last_name = parts[1]
    id_value = parts[-1]

    decoded_data = {
        "first_name": first_name,
        "last_name": last_name,
        "id": id_value
    }
    
    return decoded_data

# Example usage
encoded_string = "Robert000Smith000123"
decoded_data = decode_string(encoded_string)
print(decoded_data)
