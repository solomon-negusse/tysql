import tables

session = tables.Session()

print "\n...filter where price == 3.49\n"

for query in session.query(tables.Products).filter(tables.Products.prod_price == 3.49):
    print query.prod_name + ' ' +  query.prod_price.to_eng_string()

print "\n...filter where prod_price < 10 \n"

for query in session.query(tables.Products).filter(tables.Products.prod_price < 10):
    print query.vend_id + ' ' + query.prod_name + ' ' +  query.prod_price.to_eng_string()

print "\n...filter where 5 < prod_price < 10 \n"

for query in session.query(tables.Products).filter(
    tables.Products.prod_price < 10).filter(tables.Products.prod_price > 5):
        print query.prod_name + ' ' +  query.prod_price.to_eng_string()