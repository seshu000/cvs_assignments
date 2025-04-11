input_data=[1,2,[3,4,[6,7],6],5,[8,9,0]]

def flatten(lst1):
    output=[]
    for i in lst1:
        if  isinstance(i,list):
            output.extend(flatten(i))
        else:
            output.append(i)
    return output
print(flatten(input_data))   


def process_nested_structure(in_data):
    output=[]
    for i in in_data:    
        if isinstance(i,tuple):
            o=list(map(int, i.strip("()").split(",")))
            output.append(o)
    return output
in_data = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
print(process_nested_structure(in_data))


