from json import loads, dumps

products_path_file = './products.txt'

def get_all_products():
    with open(products_path_file, 'r') as file:
        return [loads(line.strip()) for line in file]


def buy_product(product_id):
    with open(products_path_file,'r+') as products_file:
        result = []
        for product_line in products_file:
            current_product = loads(product_line.strip())
            if current_product['id'] == product_id:
                if current_product['count'] > 0:
                    current_product['count'] -= 1
                    result.append(dumps(current_product) + '\n')
                else:
                    with open('./out_of_stock', 'a') as products_out_of_stock:
                        products_out_of_stock.write(dumps(current_product) + '\n')
            else:
                result.append(product_line)


        products_file.seek(0)
        products_file.truncate()

        products_file.writelines(result)
