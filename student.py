def student():
    student_name_list =["Meghan","Praavalika","Bharath","Madhu Venkata suriya Narayana","Nithin Rajesh","Mani Prasad"]
    res=list(filter(lambda x:len(x)>6,student_name_list))
    print(res)
student()

