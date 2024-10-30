ext = input("File name: ").lower().strip()

if "png" in ext:
    print("image/png")
elif "jpg" in ext:
    print("image/jpeg")
elif "jpeg" in ext:
    print("image/jpeg")
elif "gif" in ext:
    print("image/gif")

elif "pdf" in ext:
    print("application/pdf")

elif "txt" in ext:
    print("text/plain")

elif "zip" in ext:
    print("application/zip")

else:
    print("application/octet-stream")

