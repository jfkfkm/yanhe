#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ��Ϻ�
���ڣ�2019��11��14��
"""

import random

def name_to_number(name):
	if name=="ʯͷ":
		 name=0
		 return name
	elif name=="ʷ����":
		 name=1
		 return name
	elif name=="ֽ":
		 name=2
		 return name
	elif name=="����":
		 name=3
		 return name
	elif name=="����":
	     return name
	else:
         print('Error: No Correct Name')
def number_to_name(number):
	if number==0:
		number= "ʯͷ"
	elif number==1:
		number="ʷ����"
	elif number==2:
		number= "ֽ"
	elif number==3:
		number= "����"
	elif number==4:
		number= "����"
	return number
    		

def rpsls(player_choice):
	if(player_choice==0 and comp_number==4)or(player_choice==0 and comp_number==3)or(player_choice==3 and comp_number==1)or(player_choice==4 and comp_number==2)or(player_choice==2 and comp_number==0):
		print("��Ӯ��")
	elif(player_choice==4 and comp_number==0)or(player_choice==3 and comp_number==0)or(player_choice==1 and comp_number==3)or(player_choice==2 and comp_number==4)or(player_choice==0 and comp_number==2):
		print("�����Ӯ��")
	elif(player_choice==comp_number):
		print("���ͼ������ѡ��һ����")	
	
		
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name = input()
comp_number=random.randint(0,5)
n=comp_number
print("���ѡ����",choice_name)
print("�������ѡ����",number_to_name(n))
player_choice=name_to_number(choice_name)
rpsls(player_choice)
















