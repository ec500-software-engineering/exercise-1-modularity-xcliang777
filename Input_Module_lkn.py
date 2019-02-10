def read_data(path):
    time = []
    value = []
    try:
        with open(path,'r') as f:
            data = f.readline()
            if data:
                for i in data:
                    i = i.split()
                    time.append(float(i[0]))
                    value.append(float(i[1]))
                print("Read data successfully\n")
                return data,value
            else:
                print("Empty data file!\n")
                return 2
    except:
        print("Error:No input data\n")

        
