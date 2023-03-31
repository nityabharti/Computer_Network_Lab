import time

def loading(txt, delay_time=0.5, itr=3):
    print()
    for i in range(itr):
        print(f"\r{txt}", end="")
        time.sleep(delay_time)
        print(f"\r{txt}..", end="")
        time.sleep(delay_time)
        print(f"\r{txt}....", end="")
        time.sleep(delay_time)
        print(f"\r{txt}.....", end="")

def crc_remainder(bitstring, divisor):
    # removes additional zeroes on left side of divisor
    divisor = divisor.lstrip('0')
    len_bitstring = len(bitstring)

    padding = (len(divisor)-1) * '0'  # initially padding with zeroes

    bitstring_and_padding = list(bitstring+padding)

    while '1' in bitstring_and_padding[:len_bitstring]:
        cur_pos = bitstring_and_padding.index('1')

        for i in range(len(divisor)):
            # Applying XOR operation on
            bitstring_and_padding[cur_pos+i] = str(
                int(bitstring_and_padding[cur_pos+i]) ^ int(divisor[i]))

    return "".join(bitstring_and_padding[len_bitstring:])


def crc_check(bitstring, divisor):
    # removes additional zeroes on left side of divisor
    divisor = divisor.lstrip('0')
    len_actual_data = len(bitstring)-(len(divisor)-1)
    bitstring = list(bitstring)
    while '1' in bitstring[:len_actual_data]:
        cur_pos = bitstring.index('1')

        for i in range(len(divisor)):
            bitstring[cur_pos +
                      i] = str(int(bitstring[cur_pos+i]) ^ int(divisor[i]))

    # If remainder is containes atleast one 1 in it, then its corrupted
    if '1' in bitstring:
        return False
    else:
        return True


data = input("Enter Data: ")
div = input("Enter Divisor: ")

remainder = crc_remainder(data, div)

loading("Calculating Remainder")
print(f"\n\nRemainder is {remainder}")

data_with_remainder = data+remainder

time.sleep(2)
print(f'\nAdded remainder to the data.\n{data_with_remainder}')

loading("Checking Data with Remainder")

print("\nStatus: ")
time.sleep(2)
if crc_check(data_with_remainder, div):
    print("[SUCCESS] Check Passed /")
else:
    print("[FAILED] Check Failed X")