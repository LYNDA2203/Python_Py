def read_2d_array(row,col,datatype):
    array = []
    
    print(f"Enter the {row * col} values ({datatype}):")
    for _ in range(row):
        row = []
        for _ in range(col):
            value =input()
            if datatype == 'int':
                row.append(int(value))
            elif datatype == 'float':
                row.append(float(value))
            elif datatype == 'bool':
                row.append(value.lower() in ['true','1']) 
            else:
                print("unsupported data_type")
        array.append(row)
    return array

def print_2d_array(array):
    print("2D Array output:")
    for row in array:
        print(' '.join(str(val) for val in row))
        
def main():
    row=int(input("Enter the Number of rows:"))
    col=int(input("Enter the Number of columns:"))
    
    print("Choose data type: int/float/bool")
    datatype=input("Enter the Data_type:").strip().lower()
    
    array=read_2d_array(row,col,datatype)
    print_2d_array(array)
        
    
if __name__ == "__main__":
    main()