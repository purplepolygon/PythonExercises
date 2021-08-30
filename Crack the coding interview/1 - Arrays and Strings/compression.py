# Compress multiple characters (lower and uppercase) as follows: aaabbbcc -> a3b3c2. Return shortest string.


def compressor(compressible):
    uncompressed_list = [x for x in compressible]
    compressed_list = []
    repetition_counter = 0
    for x in range(0, len(uncompressed_list)):
        if x == 0:
            repetition_counter += 1
            compressed_list.append(uncompressed_list[x])
            continue
        elif x >= 1:
            if (
                x == len(uncompressed_list) - 1
                and uncompressed_list[x] == uncompressed_list[x - 1]
            ):
                repetition_counter += 1
                compressed_list.append(str(repetition_counter))
                break
            if (
                x == len(uncompressed_list) - 1
                and uncompressed_list[x] != uncompressed_list[x - 1]
            ):
                compressed_list.append(str(repetition_counter))
                compressed_list.append(uncompressed_list[x])
                compressed_list.append("1")
                break
            if uncompressed_list[x] == uncompressed_list[x - 1]:
                repetition_counter += 1
                continue
            elif uncompressed_list[x] != uncompressed_list[x - 1]:
                compressed_list.append(str(repetition_counter))
                compressed_list.append(uncompressed_list[x])
                repetition_counter = 1
                continue
    if len(compressed_list) < len(compressible):
        return compressed_list
    else:
        return compressible


print(compressor("abbbbcz"))
