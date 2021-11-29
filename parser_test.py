from Parser import Parser

test_strs = ["exc test_prog.py -f argval1 -v argval2", "exc test_prog.py -f \"argval1.csv\" -v argval2", "exc test_prog.py -f \"arg val1.csv\" -v argval2"]
res_lst =[]
for i in range(0,len(test_strs)): 
	print("Testing: \"{0}\"".format(test_strs[i]))
	m_inst = Parser(test_strs[i])
	res_lst = m_inst.parse()
	print(res_lst)
