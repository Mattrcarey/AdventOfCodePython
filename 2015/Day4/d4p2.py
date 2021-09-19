import hashlib


def main():
    message = "iwrupvqb"
    count = 1

    while (1):
        message2 = message + str(count)
        result = hashlib.md5(message2.encode())
        result = result.hexdigest()
        if(result[0 : 6] == "000000") :
            print(count)
            break
        count+=1


if __name__ == "__main__" :
     main()
