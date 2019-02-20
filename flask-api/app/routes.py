from app import app
from app import api
from app import db
from flask_restful import Resource

class apiVersion(Resource):
	def get(self):
		return { 'api-version' : 1.0 }
api.add_resource(apiVersion, '/api')

class SimilarProducts(Resource):
	def get(self, product_id):
		SIMILAR_PRODUCTS_QUERY = '''
		select product.product_id, product.product_url from similarproducts
		JOIN product on similarproducts.similar_product_id = product.product_id
		where similarproducts.product_id = ? 
		'''
		SIMILAR_PRODUCTS_ARGS = [product_id]
		result = db.getData(SIMILAR_PRODUCTS_QUERY, SIMILAR_PRODUCTS_ARGS, include_field_names=True)
		returnList = []
		for i,row in enumerate(result):
			if i == 0 :
				field_names = row
			else :
				newDict = {}
				for j,f in enumerate(field_names) : 
					newDict[f] = row[j]
				returnList.append(newDict)

		return returnList 
api.add_resource(SimilarProducts, '/api/similar_products/<string:product_id>')




