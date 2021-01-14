import sys
import numpy as np
import json


paswd_id={}
user_role_tb=list(''for i in range(100))
role_perm_tb={}
#role_extend_tb={}
role_contract={}
role_contract_standard={}

def init():

	#密码--用户表
	paswd_id={'admin':'ad','number i':'user i'}

	#用户--角色表 假定初始有17个user	

	user_role_tb[0]='boss'
	user_role_tb[1]='M1'
	user_role_tb[2]='M1'
	user_role_tb[3]='M2'
	user_role_tb[4]='M2'
	for i in range(3):
		user_role_tb[5+i]='A'
	for i in range(3):
		user_role_tb[8+i]='B'	
	for i in range(3):
		user_role_tb[11+i]='C'
	for i in range(3):
		user_role_tb[14+i]='D'


	#角色--权限表	
	role_perm_tb=({'boss':['r','w','de','ex','n','chg'],'manager':['r','de'],'M1':['ex'],'M2':['n','chg'],'employee':['r'],'A':['ex'],'B':['ex'],'C':['n','chg'],'D':['n','chg']})

	#角色--互斥表，表面每个角色已经被分配给了多少用户
	role_contract={'boss':1,'M1':2,'M2':2,'A':3,'B':3,'C':3,'D':3}
	role_contract_standard={'boss':1,'M1':2,'M2':2,'A':3,'B':3,'C':3,'D':3}

	np.save('role_perm_tb.npy',role_perm_tb)
	np.save('user_role_tb.npy',user_role_tb)
	np.save('paswd_id.npy',paswd_id)
	np.save('role_contract.npy',role_contract)
	np.save('role_contract_standard.npy',role_contract_standard)


init()
