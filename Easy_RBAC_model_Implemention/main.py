import sys
import numpy as np
import json

#表格
paswd_id={}
user_role_tb=list(range(100))
role_perm_tb={}
role_contract={}
role_contract_standard={}

def numpy_concatenate(a):
    return list(np.concatenate(a))

class role(object):
	def __init__(self):
		self.info =''
		self.perm =[]

	def set(self):
		#(self.num)++ 
		pass


class boss(role):
	def set(self):
		self.perm.append(role_perm_tb['boss'])

class manager(role):
	def set(self):
		self.perm.append(role_perm_tb['manager'])


class employee(role):
	def set(self):
		super().set()
		self.perm.append(role_perm_tb['employee'])


class A(employee):
	def set(self):
		super().set()
		self.perm.append(role_perm_tb['A'])

class B(employee):
	def set(self):
		super().set()
		self.perm.append(role_perm_tb['B'])

class C(employee):
	def set(self):
		super().set()
		self.perm.append(role_perm_tb['C'])		

class D(employee):
	def set(self):
		super().set()
		self.perm.append(role_perm_tb['D'])

#备用
class E(employee):
	def set(self):
		super().set()
		self.perm.append(role_perm_tb['E'])	

class M1(manager):
	def set(self):
		super().set()
		self.perm.append(role_perm_tb['M1'])

class M2(manager):
	def set(self):
		super().set()
		self.perm.append(role_perm_tb['M2'])

#备用
class M3(manager):
	def set(self):
		super().set()
		self.perm.append(role_perm_tb['M3'])


def load():
	global paswd_id
	global role_perm_tb
	global user_role_tb
	global role_contract
	global role_contract_standard

	paswd_id=(np.load('paswd_id.npy',allow_pickle=True)).tolist()
	role_perm_tb=(np.load('role_perm_tb.npy',allow_pickle=True)).tolist()
	user_role_tb=(np.load('user_role_tb.npy',allow_pickle=True)).tolist()
	role_contract=(np.load('role_contract.npy',allow_pickle=True)).tolist()
	role_contract_standard=(np.load('role_contract_standard.npy',allow_pickle=True)).tolist()
'''
	f = open('role_perm_tb.txt','w')
	f.write(str(role_perm_tb))
	f.close()

	f = open('user_role_tb.txt','w')
	f.write(str(user_role_tb))
	f.close()
'''



def success():
	print('you have done the acess succesfully!')


def fail():
	print('sorry,you have no permission!')


def admin():
	print('******************************************************')
	print('*  You are the admin. Now you can type these orders: *')
	print('*   tables -- check all the tables		     *')
	print('*   modify --modify any tables			     *')
	print('******************************************************')

	global paswd_id
	global role_perm_tb
	global user_role_tb
	global role_contract
	global role_contract_standard

	#print(role_contract_standard)

	while (1):
		func=input('input orders:')
		if not func:
			break

		#查看表格
		elif func=='tables':
			print ('password_id table:')
			for key,value in paswd_id.items():
				print('{key}:{value}'.format(key = key, value = value))
			print('-----------------------')

			print('role_permission_table:')
			for key,value in role_perm_tb.items():
				print('{key}:{value}'.format(key = key, value = value))
			print('-----------------------')

			print('user_role_table:')
			for i in range(len(user_role_tb)):
				if user_role_tb[i]:
					print('user '+str(i)+': '+str(user_role_tb[i]))
			print('-----------------------')


		elif func=='modify':
			print ('what to modify?\n type 1:password_id\n type 2:role_permission\n type 3:user_role')		
			md=input('>')
			if not func:
				break
			#switch(md):
			if md==('1'):
				pass

			elif md==('2'):
				print('the role you want to modify is:')
				r=input('role:')
				print('type a:add permission\ntype b:delete permission')
				f=input('>>')
				if f=='a':
					print('the permission to add is:')
					p=input('>>>')
					role_perm_tb[r].append(p)

				elif f=='b':
					print('the permission to delete is:')
					p=input('>>>')
					plist=(role_perm_tb[r])
					plist.remove(p)
					role_perm_tb[r]=plist

			#np.save('user_role_tb.npy',user_role_tb)
				for key,value in role_perm_tb.items():
					print('{key}:{value}'.format(key = key, value = value))	
				print('success')

				#np.save('user_role_tb.npy',user_role_tb)

			elif md==('3'):

				print('type a:add a user\ntype b:delete a user')
				f=input('>>')
				if f=='a':
					print('the role you want to modify is:')	
					r=input('role:')
					if role_contract_standard[r]<3 and role_contract[r]>=role_contract_standard[r]:
						print('access denied!')
						break

					print('the user number to add is:')
					p=int(input('>>>'))
					user_role_tb[p]=r
					role_contract[r]+=1

					for i in range(len(user_role_tb)):
						if user_role_tb[i]:
							print('user '+str(i)+': '+str(user_role_tb[i]))

					np.save('user_role_tb.npy',user_role_tb)			
					print('success')	

					
				elif f=='b':
					print('the user number to delete is:')
					p=int(input('>>>'))
					user_role_tb[p]='no role'
					role_contract[r]-=1

					print('user_role_table:')
					for i in range(len(user_role_tb)):
						if user_role_tb[i]:
							print('user '+str(i)+': '+str(user_role_tb[i]))

					np.save('user_role_tb.npy',user_role_tb)	
					print('success')	


def user(pwd):
	print('-----------------------')
	index=int(pwd)
	role=user_role_tb[index]
	print('｜  your role:'+role)

	if role=='boss':
		r=boss()
		r.set()
		perm=numpy_concatenate(r.perm)
		#print(perm)	

	elif role=='M1':
		r=M1()
		r.set()
		perm=numpy_concatenate(r.perm)
		#print(perm)	

	elif role=='M2':
		r=M2()
		r.set()
		perm=numpy_concatenate(r.perm)
		#print(perm)	

	elif role=='A':
		r=A()
		r.set()
		perm=numpy_concatenate(r.perm)
		#print(perm)

	elif role=='B':
		r=B()
		r.set()
		perm=numpy_concatenate(r.perm)
		#print(perm)	

	elif role=='C':
		r=C()
		r.set()
		perm=numpy_concatenate(r.perm)
		#print(perm)	

	elif role=='D':
		r=D()
		r.set()
		perm=numpy_concatenate(r.perm)
		#print(perm)	

	print('-----------------------')	
	print('|  please type in your order:')	

	while(1):
		order=input('>')
		if not order:
			break

		elif order in perm:
			success()

		else:
			fail()
		

def main():
	load()

	pwd=input('password:')
	print('identity:')
	#print(pwd)
	#print(paswd_id['admin'])

	if pwd == (paswd_id['admin']):
		print('admin')
		admin()
	else:
		print('normal user')
		user(pwd)



main()
