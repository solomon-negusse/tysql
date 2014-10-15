from sqlalchemy import and_, not_
import tables

session = tables.Session()

print "\n 'like %' filtering"
for query in session.query(tables.Products).filter(
	tables.Products.prod_name.like('%bean bag%')):
	print query.prod_id.strip() + ' ' + query.prod_name.strip()

print "\n 'like _' filtering"
for query in session.query(tables.Products).filter(
	tables.Products.prod_name.like('__ inch teddy bear%')):
	print query.prod_id.strip() + ' ' + query.prod_name.strip()

print "\n 'like []' filtering"
for query in session.query(tables.Customers).filter(
	tables.Customers.cust_contact.like('[JM]%')):
	print query.cust_contact