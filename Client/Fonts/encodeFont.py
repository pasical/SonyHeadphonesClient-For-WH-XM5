font = "unsigned char CascadiaCodeTTF[{}] = {{{}}};"
fontDecl = "extern unsigned char CascadiaCodeTTF[{}];"

with open("./CascadiaCode.ttf", "rb") as f:
    fbytes = f.read()

font = font.format(len(fbytes), ",".join(map(lambda x: f"{x}", fbytes)))

with open("../CascadiaCodeFont.cpp", "w") as f:
    f.write('#include "CascadiaCodeFont.h"\n\n')
    f.write("/*\n")
    with open("FontLicense.txt", "r") as h:
        f.write(h.read())
    f.write("*/\n\n")
    f.write(font)

with open("../CascadiaCodeFont.h", "w") as f:
    f.write("#pragma once\n\n")
    f.write("//Generated by Fonts/encodeFont.py\n//This is crossplatform and works well, although it is a bit weird.\n\n")
    f.write(fontDecl.format(len(fbytes)))