gift = []
ans = input('What is the first of three gifts that you want under 100 dolllars each?')
gift.append(ans)
print(gift)
ans = input('What else do you want?')
gift.append(ans)
print(gift)
ans = input('What is the third gift you want?')
gift.append(ans)
print(gift)
price = input('How much does ' + gift[0] + ' cost?')
gift_price1 = int(price)
while gift_price1 > 100:
    print(gift[0] + ' costs too much!!')
    gift.remove(gift[0])
    ans = input('What do you want instead?')
    gift.insert(0, ans)
    print(gift)
    price = input('How much does ' + gift[0] + ' cost?')
    gift_price1 = int(price)
if gift_price1 <= 100:
    print('Getting  a ' + gift[0] + ' is a great idea it fits within your price range!!')
price = input('How much does ' + gift[1] + ' cost?')
gift_price2 = int(price)
while gift_price2 > 100:
    print(gift[1] + ' costs too much!!')
    gift.remove(gift[1])
    ans = input('What do you want instead?')
    gift.insert(1, ans)
    print(gift)
    price = input('How much does ' + gift[1] + ' cost?')
    gift_price2 = int(price)
if gift_price2 <= 100:
    print('Getting  a ' + gift[1] + ' is a great idea it fits within your price range!!')
price = input('How much does ' + gift[2] + ' cost?')
gift_price3 = int(price)
while gift_price3 > 100:
    print(gift[2] + ' costs too much!!')
    gift.remove(gift[2])
    ans = input('What do you want instead?')
    gift.insert(2, ans)
    print(gift)
    price = input('How much does ' + gift[2] + ' cost?')
    gift_price3 = int(price)
if gift_price3 <= 100:
    print('Getting  a ' + gift[2] + ' is a great idea and it fits within your price range!!')
    print('These are all good choices congratulations on your three gifts!!!')
    print(gift)

Total_Price = gift_price1 + gift_price2 + gift_price3
print('The total cost of all the gifts will cost around ')
print ('$'(int(Total_Price)))