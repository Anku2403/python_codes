n=int(input("Enter the number:"))

def swapEndian(n):
    byte0=(n & eval('0x000000FF')) << 24
    byte1=(n & eval('0x0000FF00')) << 8
    byte2=(n & eval('0x00FF0000')) >> 8
    byte3=(n & eval('0xFF000000')) >> 24

    return byte0 | byte1 | byte2 | byte3

print(swapEndian(n))