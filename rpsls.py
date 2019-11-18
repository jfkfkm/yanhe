#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：严贺
日期：2019年11月14日
"""

import random

def name_to_number(name):
	if name=="石头":
		 name=0
		 return name
	elif name=="史波克":
		 name=1
		 return name
	elif name=="纸":
		 name=2
		 return name
	elif name=="蜥蜴":
		 name=3
		 return name
	elif name=="剪刀":
	     return name
	else:
         print('Error: No Correct Name')
def number_to_name(number):
	if number==0:
		number= "石头"
	elif number==1:
		number="史波克"
	elif number==2:
		number= "纸"
	elif number==3:
		number= "蜥蜴"
	elif number==4:
		number= "剪刀"
	return number
    		

def rpsls(player_choice):
	if(player_choice==0 and comp_number==4)or(player_choice==0 and comp_number==3)or(player_choice==3 and comp_number==1)or(player_choice==4 and comp_number==2)or(player_choice==2 and comp_number==0):
		print("您赢了")
	elif(player_choice==4 and comp_number==0)or(player_choice==3 and comp_number==0)or(player_choice==1 and comp_number==3)or(player_choice==2 and comp_number==4)or(player_choice==0 and comp_number==2):
		print("计算机赢了")
	elif(player_choice==comp_number):
		print("您和计算机的选择一样呢")	
	
		
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name = input()
comp_number=random.randint(0,5)
n=comp_number
print("你的选择是",choice_name)
print("计算机的选择是",number_to_name(n))
player_choice=name_to_number(choice_name)
rpsls(player_choice)
















