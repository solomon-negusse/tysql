from sqlalchemy import and_, not_
import tables

session = tables.Session()

print "\n 'AND' filtering"
for query in session.query(tables.Products).filter(
	and_(tables.Products.prod_price < 4, 
	tables.Products.vend_id == 'DLL01')):
	print query.prod_id.strip() + ' ' + query.prod_price.to_eng_string() + \
		' ' + query.prod_name

print "\n 'IN' filtering\n"
for query in session.query(tables.Products).filter(
	tables.Products.vend_id.in_(['DLL01', 'BRS01'])):
	print query.prod_name.strip() + ' ' + query.prod_price.to_eng_string()

print "\n 'NOT' filtering\n"
for query in session.query(tables.Products).filter(
	not_(tables.Products.vend_id == 'DLL01')):
	print query.prod_name.strip()


