#Q-1
# Flattens the list 
#ie input = [1,2,3, [1,2,3,[3,4],2]]
# output = [1,2,3,1,2,3,3,4,2]


input_data=[1,2,3, [1,2,3,[3,4],2]]

def flatten(lst1):
    output=[]
    for i in lst1:
        if  isinstance(i,list):
            output.extend(flatten(i))
        else:
            output.append(i)
    return output
print(flatten(input_data))   


#Q-2
#input = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
#output = [[[[0,1,2],[3,4,5]],[[5,6,7],[9,4,2]]]]

in_data = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]

def convert(data):
    result = []
    for item in data:
        if isinstance(item, list):
            result.append(convert(item))
        else:
            numbers = list(map(int, item.strip("()").split(",")))
            result.append(numbers)
    return result

print(convert(in_data))



