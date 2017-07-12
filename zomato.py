def calculate_bill(price):
    service_charge=float(price*0.1)
    service_tax=float(price*0.06)
    vat=float(price*0.15)
    cal_bill=float(price+service_charge+service_tax+vat)
    print 'bill='+str(cal_bill)

restaurants_n={
    'restaurants':{
        'pizza hut':{
            'Menu':{
                'Brick oven pizza':'160',
                'italian pizza':'167',
                'chicago style':'180'

            },
            'owner name':'nidhi jakhmola',
            'Rating ':4.9
        },
        'McDonalds burger':{
            'Menu':{
                'Taco Burgers':110,
                'Chicken Caesar Burger':160,
                'Canyon Creek Burger':170
            },
            'owner name':'NN',
            'Rating':4.8
        }

    }
}
ch=raw_input('1.owner \n2.customer')
if ch=='1':
    update_information=raw_input('update information \nyes or no')
    if update_information=='yes':
        print restaurants_n['restaurants'].keys()
        select_restaurant=raw_input('enter the restaurant name which you want to update')
        if select_restaurant in restaurants_n['restaurants'].keys():
            item_name=raw_input('enter the name of the new item \nYes or No ')
            print item_name
            if item_name=='yes':
                 choosed_item_name=raw_input('enter the name of food \nYes or No')
                 if choosed_item_name in restaurants_n['restaurants'][select_restaurant]['Menu']:
                     print choosed_item_name,'already exist in item list'
                 elif choosed_item_name not in restaurants_n['restaurants'][select_restaurant]['Menu']:
                     print choosed_item_name,'item is updated'
        elif select_restaurant not in restaurants_n['restaurants'].keys():
            print select_restaurant,'restaurant is unavailable'
    elif update_information=='no':
        print'bye'
elif ch=='2':
    print restaurants_n['restaurants'].keys()
    orders=raw_input('if you wants to order press \n1.yes or no')
    if orders=='yes':
        restaurant_select=raw_input('select the name of the restaurant you want to select')
        if restaurant_select not in restaurants_n['restaurants'].keys():
            print restaurant_select,'restaurant is not available'
        elif restaurant_select in restaurants_n['restaurants'].keys():
            food_name=raw_input('enter your food name')
            if food_name in restaurants_n['restaurants'][restaurant_select]['Menu']:
                print food_name
                total=restaurants_n['restaurants'][restaurant_select]['Menu'][food_name]
                cost = total + (total * 0.5) + (total * 0.8)+(total*0.15)
                print 'your order is successful'
                print 'total price is', cost
            else:
                print'unavailable food item'
    method_of_ordering=raw_input('1.by delivery \n2by walk \n.please enter')
    if method_of_ordering=='1':
        print 'you choosed by delivery'
        print'amount to be paid'+str(cost)
    elif method_of_ordering=='2':
        print'you choosed by walk-in'
        print'amount to be paid'+str(cost)
    rating_no=raw_input('Rate us\n press 1 for rating')
    if rating_no=='1':
        rate=float(raw_input('what is your rating'))
        restaurants_n['restaurants'][restaurant_select][rate]=rate
        print'thnk u for rating'
else:
      print'bye'
















