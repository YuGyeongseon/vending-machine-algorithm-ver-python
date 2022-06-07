# vending-machine-ver-python
# made by 30618
num1 = " 1번) "
num2 = " 2번) "
num3 = " 3번) "
num4 = " 4번) "
num5 = " 5번) "
price ="가격:"

stackMoney = 0
stackMoney = float(stackMoney)

password = input("비밀번호를 설정해주세요. (숫자만 가능)입력:")
password = float(password)
while True:
    question = input("안녕하세요 자판기 프로그램입니다. 다음 선택사항중 하나를 선택해주세요. 1.제품 넣기  2.제품 구매하기 3. 돈 확인하기")
    if question =='1':
        checkPassword=input("비밀번호를 입력해주세요. 입력:")
        checkPassword=float(checkPassword)
        if checkPassword == password:
 	       product1 = input("1번 제품을 입력해주세요.")
 	       print(product1)
 	       product1Price = input("제품의 가격을 입력해주세요.")
 	       product1Price = float(product1Price)
 	       print(product1Price)
 	       
 	       product2 = input("2번 제품을 입력해주세요.")
 	       print(product2)
 	       product2Price = input("제품의 가격을 입력해주세요.")
 	       product1Price = float(product1Price)
 	       print(product2Price)
 	       
 	       product3 = input("3번 제품을 입력해주세요.")
 	       print(product3)
 	       product3Price = input("제품의 가격을 입력해주세요.")
 	       product3Price = float(product3Price)
 	       print(product3Price)
 	       product4 = input("4번 제품을 입력해주세요.")
 	       print(product4)
 	       product4Price = input("제품의 가격을 입력해주세요.")
 	       product4Price = float(product4Price)
 	       print(product4Price)
 	       
 	       product5 = input("5번 제품을 입력해주세요.")
 	       print(product5)
 	       product5Price = input("제품의 가격을 입력해주세요.")
 	       product5Price = float(product5Price)
 	       print(product5Price)
 	       continue
        elif checkPassword != password:
       	 print("비밀번호가 틀렸습니다.")
       	 continue
    elif question =='2':
        print("제품목록")
        print(num1+product1+price)
        print(product1Price)
        print(num2+product2+price)
        print(product2Price)
        print(num3+product3+price)
        print(product3Price)
        print(num4+product4+price)
        print(product4Price)
        print(num5+product5+price)
        print(product5Price)
        money=input("돈을 넣어주세요.")
        money=float(money)
        
        productnum=input("제품번호를 입력해주세요.")
        productnum=float(productnum)
        if productnum == 1:
        	if money >= product1Price:
        		remainMoney = money - product1Price
        		print(product1)
        		print("잔돈은")
        		print(remainMoney)
        		print("원 입니다.")
        		stackMoney = stackMoney + product1Price
        	
        		
        	else:
        		print("돈이 부족합니다.")
        	continue
        elif productnum ==2:
        	
        	if money >= product2Price:
        		remainMoney2 = money - product2Price
        		print(product2)
        		print("잔돈은")
        		print(remainMoney2)
        		print("원 입니다.")
        		stackMoney = stackMoney + product2Price
        	else:
        		print("돈이 부족합니다.")
        	continue
        	
        elif productnum == 3:
        	
        	if money >= product3Price:
        		remainMoney3 = money - product3Price
        		print(product3)
        		print("잔돈은")
        		print(remainMoney3)
        		print("원 입니다.")
        		stackMoney = stackMoney + product3Price
        	else:
        		print("돈이 부족합니다.")
        	continue
        	
        elif productnum ==4:
        	
        	if money >= product4Price:
        		remainMoney4 = money - product4Price
        		print(product4)
        		print("잔돈은")
        		print(remainMoney4)
        		print("원 입니다.")
        		stackMoney = stackMoney + product4Price
        		
        	else:
        		print("돈이 부족합니다.")
        	continue
        	
        elif productnum ==5:
        	
        	if money >= product5Price:
        		remainMoney5 = money - product5Price
        		print(product5)
        		print("잔돈은")
        		print(remainMoney5)
        		print("원 입니다.")
        		stackMoney = stackMoney + product5Price
        		
        	else:
        		print("돈이 부족합니다.")
        	continue
        	
        else:
        	print("제품이 선택되지 않았습니다. 처음부터 다시해주세요.")
        continue
    elif question =='3':
    	checkPassword = input("비밀번호를 입력해주세요.")
    	checkPassword = float(checkPassword)
    	if checkPassword == password:
    		print(stackMoney)
    		print("won")
    	else:
    		print("비밀번호가 틀렸습니다.")
    	continue
    
    else:
        print("선택지에 맞는 숫자를 입력하세요")
        continue 
   
