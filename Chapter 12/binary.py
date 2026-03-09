# blist = [1, 2, 3, 255]

# the_bytes = bytes(blist)
# print(the_bytes)

# the_byte_array = bytearray(blist)
# print(the_byte_array)

# print(b'\x61')
# print(b'\x01abc\xff')

# blist = [1, 2, 3, 255]

# the_byte_array = bytearray(blist)
# print(the_byte_array)

# the_byte_array[1] = 127
# print(the_byte_array)

# the_bytes = bytes(range(0, 256))
# the_byte_array = bytearray(range(0, 256))

# print(the_bytes)


# import struct

# valid_png_header = b'\x89PNG\r\n\x1a\n'
# data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
# if data[:8] == valid_png_header:
#     width, height = struct.unpack('>LL', data[16:24])
#     print('Valid PNG, width', width, 'height', height)
# else:
#     print('Not a valid PNG')

# print(data[16:20])
# print(data[20:24])

# print(0x9a)
# print(0x8d)

# import struct

# print(struct.pack('>L', 154))
# print(struct.pack('>L', 141))


# print(struct.unpack('>2L', data[16:24]))
# print(struct.unpack('>16x2L6x', data))

# from construct import Struct, Magic, UBInt32, Const, String

# fmt = Struct('png',
#              Magic(b'\x89PNG\r\n\x1a\n'),
#              UBInt32('length'),
#              Const(String('type', 4), b'IHDR'),
#              UBInt32('width'),
#              UBInt32('height'))

# data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
# result = fmt.parse(data)
# print(result)
# print(result.width, result.height)


# import binascii

# valid_png_header = b'\x89PNG\r\n\x1a\n'
# print(binascii.hexlify(valid_png_header))
# print(binascii.unhexlify(b'89504e470d0a1a0a'))