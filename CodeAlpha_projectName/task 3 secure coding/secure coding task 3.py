username = input("Enter Username: ")
password = input("Enter Password: ")

query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"

print("\nGenerated SQL Query:")
print(query)
