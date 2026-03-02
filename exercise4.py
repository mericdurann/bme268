extensions = input ("File Name:")

if extensions == ".gif":
    print("image/gif")
elif extensions == ".jpg":
    print("image/jpeg")
elif extensions == ".jpeg":
    print("image/jpeg")
elif extensions == ".png":
    print("image/png")
elif extensions == ".pdf":
    print("application/pdf")
elif extensions == ".txt":
    print("text/plain")
else:
    print("application/octet-stream")