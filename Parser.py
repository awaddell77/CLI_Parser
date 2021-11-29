

class Parser:
	def __init__(self,p_str):
		if not isinstance(p_str,str): raise TypeError("Must be str")
		self._p_str = p_str
	def parse(self):
		p_lst = []
		temp_str = ""
		q_esc = False
		for i in range(0, len(self._p_str)):
			if self._p_str[i] == "\"" and not q_esc: q_esc = True
			elif self._p_str[i] == "\"" and q_esc: q_esc = False
			elif self._p_str[i] != " " and not q_esc: 
				temp_str += self._p_str[i]


			elif q_esc and self._p_str[i] != "\"":
				print("Adding {0}".format(self._p_str[i]))
				temp_str += self._p_str[i]
			elif not q_esc and self._p_str[i] == " ":
				print("Finished {0}".format(temp_str))
				p_lst.append(temp_str)
				temp_str = ""
		return p_lst


