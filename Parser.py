

class Parser:
	def __init__(self,p_str):
		if not isinstance(p_str,str): raise TypeError("Must be str")
		#space must be added to a stripped p_str in order to ensure that the last arg or argval is added to the parameter list
		self._p_str = p_str.strip() + " "
	def parse(self):
		#parameter list
		p_lst = [] 
		temp_str = ""
		q_esc = False
		#a space has to be added to the end of the string

		
		for i in range(0, len(self._p_str)):
			if self._p_str[i] == "\"": q_esc = not q_esc
			#elif self._p_str[i] == "\"" and q_esc: q_esc = False
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


