def main():
    data0 = input()
    data1 = input()

    flag = True
    data_tmp = data0
    count = 0
    len_data = len(data0)
    while True:
        if data0 == "":
            break
        data0 = data0.replace(data0[0], "")
        print(data0)
        data1 = data1.replace(data1[0], "")
        print(data1)
        if len(data0) != len(data1):
            print('No')
            exit()

    print('Yes')

if __name__ == "__main__":
    main()
