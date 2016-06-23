# update only the last number in the ip addr
input='22.145.132.156'
print "input  : " , input
inputlist=input.split('.')
# print inputlist
num_list=map(lambda x : int(x), inputlist)
# print num_list
new_num=num_list[3]+1
# print new_num
num_list[3]=new_num
# print "num_list : ", num_list
output=''
for i in range(len(num_list)):
    output = output + str(num_list[i]) + '.'
    # print output
# print len(output)-1
output=output[0:len(output)-1]
print "output : " , output
