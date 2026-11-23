import bcrypt
from pathlib import Path

USER_FILE = Path(__file__).parent / "DATA" / r"C:\Users\Het\CST1510_CW2\users.txt"

def hash_password(password):
    binary_password = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(binary_password, salt)
    return(hashed_password.decode("utf-8"))

def register(username,password):
      with open(USER_FILE , "a")as f:
           hashed_password = hash_password(password)
           f.write(f"{username},{hashed_password}\n")
           print(f"User {username} registered successfully.")

if __name__ == "__main__":
   
    while True:
        choice = input("do you want to (1) Register or (2) login (3) exit")
        if choice == "1":
            username = input("Enter your username:")
            password = input("Enter your password:")
            register(username, password)
        elif choice == "2":
              username = input("Enter your username:")
              password = input("Enter your password:")

              with open(USER_FILE, "r") as f:
                   for line in f:
                        stored_username, stored_hashed_password = line.strip().split(",")
                        if username == stored_username:
                            if bcrypt.checkpw(password.encode("utf-8"), stored_hashed_password.encode("utf-8")):
                                print(f"User {username} logged in successfully.")
                            else:
                                print("Incorrect password.")
                            break 
                       
        elif choice == "3":
             print("Exiting the program.")
             break
                             
                                         
            
            
        