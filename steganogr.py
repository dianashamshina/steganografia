from stegano import lsb

secret = lsb.hide("1023.png", "Password: N4_q5MXi3")
secret.save("1023_secret.png")

result = lsb.reveal("1023_secret.png")
print(result)