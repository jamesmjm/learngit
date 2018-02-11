def discount (price,rate):
	final_price = price * rate
	return final_price
old_price = float(input('原价：'))
rate = float(input('折扣：'))
new_price = discount(old_price,rate)
print('打折后价格：', new_price)
