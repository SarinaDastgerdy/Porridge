import argparse
from porridge import Porridge

PASSWORDS_FILE = "stored_passwords.txt"

# Function to store a password
def store_password(password, key, secret):
    try:
        # Initialize Porridge with key and secret
        porridge = Porridge(f'{key}:{secret}')
        
        # Hash the password using Porridge
        hashed_password = porridge.boil(password)
        
        # Write hashed password to file
        with open(PASSWORDS_FILE, "a") as f:
            f.write(f"{hashed_password}\n")
        
        print("Success")
    except Exception as e:
        print(f"Error: {e}")

# Function to verify a password
def verify_password(password, key, secret):
    try:
        # Initialize Porridge with key and secret
        porridge = Porridge(f'{key}:{secret}')

        # Read stored passwords from file
        with open(PASSWORDS_FILE, "r") as f:
            stored_passwords = f.read().splitlines()
        

        # Check if password matches any stored password
        for stored_password in stored_passwords:
            # Verify the password using Porridge
            if porridge.verify(password, stored_password):
                print("Verified")
                return 1
        
        # If password does not match any stored password
        print("Not Found")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Store and verify password using Porridge")
    
    # Add subparsers for different commands
    subparsers = parser.add_subparsers(dest="command")
    
    # Subparser for 'store' command
    store_parser = subparsers.add_parser("store", help="Store password")
    store_parser.add_argument("password", help="Password to be stored")
    store_parser.add_argument("key", help="Key for Porridge")
    store_parser.add_argument("secret", help="Secret for Porridge")
    
    # Subparser for 'verify' command
    verify_parser = subparsers.add_parser("verify", help="Verify password")
    verify_parser.add_argument("password", help="Password to be verified")
    verify_parser.add_argument("key", help="Key for Porridge")
    verify_parser.add_argument("secret", help="Secret for Porridge")
    
    try:
        args = parser.parse_args()
    except SystemExit:
        parser.error('Invalid input format. Use: porridge.py store/verify <password> <key> <secret>')

    if args.command == "store":
        store_password(args.password, args.key, args.secret)

    elif args.command == "verify":
        verify_password(args.password, args.key, args.secret)
