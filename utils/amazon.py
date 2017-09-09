import random
from utils import const
from utils import var

def new_sku(num):
    az_strs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
    def rannum(num):
        rand_str = ''
        for x in range(num):
            rand_str += random.choice(az_strs)
        return rand_str
    sku = rannum(num)
    return sku

def every_line(x):
    if x!=[]:
        raw_line_data = x
        asin = raw_line_data[var.asin_index]
        price = str(raw_line_data[var.price_index]).strip()
        return real_need(asin,price)

def real_need(asin,price):
        sku = new_sku(12)
        max_price = random.randint(200,400)
        stock = random.randint(300,600)
        price = str(price).strip()
        price = price.split('-')[0].strip()
        if price == '' or float(price) < 1:
            price = var.order_price
            min_price = price -1

        else:
            price = round(float(price),2)
            min_price = round(float(price) -1,2)


        good_line = '{sku}\t{product_id}\t{product_id_type}\t{price}\t{min_price}\t{max_price}\t{item_condition}\t{quantity}\t{add_delete}\n'.format(
            sku = sku,
            product_id = asin,
            product_id_type = '1',
            price = str(price),
            min_price = str(min_price),
            max_price = str(max_price),
            item_condition = '11',
            quantity = str(stock),
            add_delete = 'a'

        )
        print(good_line)
        return good_line
# every_line('2	Quickie	Quickie Glass and Mug Sponge	B000QOIH3M	 Brushes		 - 	7	136	Parent	采集完成	美国		http://www.amazon.com/dp/B000QOIH3M	https://images-na.ssl-images-amazon.com/images/I/31ApOQ3yIHL.jpg	https://images-na.ssl-images-amazon.com/images/I/811ckbKI%2BEL._SL1500_.jpg		[已采集详情]					 - 	#792955|#2352')


