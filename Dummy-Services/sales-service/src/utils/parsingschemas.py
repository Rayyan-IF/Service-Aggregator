read_data = open("inp_schema.txt","r")
out_data = open("out_schema.txt","w")
lines = read_data.readlines()
i = 0
for check in lines:
    i = i+1
    check_data = check.find("Column(")
    get_type = check[check_data+7:]
    get_field = check[:check.find("=")-1]
    if get_type.__contains__("Boolean"):
        out_data.write(get_field+":bool")
    elif get_type.__contains__("Integer"):
        out_data.write(get_field+":int")
    elif get_type.__contains__("String") or get_type.__contains__("CHAR") :
        out_data.write(get_field+":str")
    elif get_type.__contains__("DateTime"):
        out_data.write(get_field+":datetime")
    elif get_type.__contains__("Float"):
        out_data.write(get_field+":float")
    out_data.write("\n")
out_data.close()