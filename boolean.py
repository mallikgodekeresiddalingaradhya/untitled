print (42 == 42)
print (42 == 99)
print (2 != 3)
print (2 != 2)

name = "Alice"
password = "s3cr3t"
if name == "Alice":
    print ("Hello, Alice!")
    if password == "s3cr3t" :
        print ("Access granted.")
    else:
        print ("Access denied.")
        
        
name = "Bob"
age = 3000
if name == "Alice":
    print ("Hello, Alice!")
elif age < 18:
        print ("You are not Alice, kiddo.")
elif age > 2000:
    print ("Unlike you, Alice is not an immortal vampire.")
elif age > 100:
    print ("You are neither Alice nor a vampire.")
