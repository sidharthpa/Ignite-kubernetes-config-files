from pyignite import Client

client = Client()
client.connect('127.0.0.1', 10800)
PRODUCT_CREATE_TABLE = '''
create table product(
	product_id VARCHAR PRIMARY KEY,
	product_url VARCHAR
)
'''
client.sql(PRODUCT_CREATE_TABLE)
SIMILARPRODUCTS_CREATE_TABLE = '''
create table similarproducts(
	product_id VARCHAR ,
	similar_product_id VARCHAR ,
	similariy_score DOUBLE ,
	PRIMARY KEY (product_id, similar_product_id)
)
'''
client.sql(SIMILARPRODUCTS_CREATE_TABLE)

PRODUCT_INSERT_QUERY = '''
insert into product values (? , ?)
'''
SIMILARPRODUCTS_INSERT_QUERY = '''
insert into similarproducts values (? , ?, ?)
'''

# Code for inserting dummy data
# INSERT_PRODUCT_DATA= []
# for i in range(10) :
# 	INSERT_PRODUCT_DATA.append( [str(i),str(i)] )

# for row in INSERT_PRODUCT_DATA :
# 	client.sql(PRODUCT_INSERT_QUERY, query_args=row)

# INSERT_SIMILARPRODUCT_DATA= [['1','2',2.2],['1','3',2.2],['1','4',2.2],['5','0',11.1],['5','9',11.1],['7','6',0.99]]

# for row in INSERT_SIMILARPRODUCT_DATA :
# 	client.sql(SIMILARPRODUCTS_INSERT_QUERY,  query_args=row)
