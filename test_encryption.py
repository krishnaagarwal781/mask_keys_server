from keyguardian.encryption import clock, declock

def test_clock_declock():
    # Sample data
    original_data = "khapre lodu"
    
    # Encrypt the data
    encrypted_data = clock(original_data)
    print("Encrypted Data:", encrypted_data)
    
    decrypted_data = declock(encrypted_data)
    print("Decrypted Data:", decrypted_data)
    
    assert decrypted_data == original_data

if __name__ == "__main__":
    test_clock_declock()
