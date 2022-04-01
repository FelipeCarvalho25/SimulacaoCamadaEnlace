

def binarySum(a, b):
        while (b != 0):
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a


def calculate_checkSum(data):
        checkSum = 0
        for char in data:
            checkSum = binarySum(checkSum, ord(char))

            while (checkSum > 255):
                checkSum = checkSum % 256
                checkSum = binarySum(checkSum, 1)
        print(str(checkSum))      
        return checkSum


def corrupt(msg, computed_checksum_S):
        checksum_S = calculate_checkSum(msg)

        return binarySum(checksum_S, computed_checksum_S) != 255
        
def simula_recebimento(pacote):
    if corrupt(pacote[0], pacote[1]):
        print("pacote corrompido")
    else:
        print("pacote recebido com sucesso")
        
        
mensagem = 'mensagem de teste'
checksum_mensagem = ~calculate_checkSum(mensagem) & 255
#mensagem = 'mensagem de t3ste' #descomentar para testar mensagem corrompida
print(str(checksum_mensagem))  
pacote = [mensagem,checksum_mensagem]

simula_recebimento(pacote)



