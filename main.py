

def binarySum(a, b):
        while (b != 0):
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a


def calculate_checkSum(cls, data):
        checkSum = 0
        for char in data:
            checkSum = binarySum(checkSum, ord(char))

            while (checkSum > 255):
                checkSum = checkSum % 256
                checkSum = binarySum(checkSum, 1)
        return checkSum


def corrupt(msg, computed_checksum_S):
        checksum_S = calculate_checkSum(msg)
        inverted_checksum = ~computed_checksum_S & 255

        return binarySum(checksum_S, inverted_checksum) != 255