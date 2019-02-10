def read_data(path):
    try:
        with open(path,'r') as f:
            data = f.readline().split()
            if data:
                time = data[0]
                value = data[1]
                float(value)
                print("Read data successfully\n")
            else:
                print("Empty data file!\n")
                return 2
        return value
    except:
        print("Error:No input data\n")

        
