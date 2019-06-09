from marshmallow import Schema, fields

class CategoriesSchema(Schema):
	class Meta:
		fields = ('id', 'name')

class ProductResourcesSchema(Schema):
	class Meta:
		fields = ('picture_file_url', 'product_description')
		exclude = ('id', 'product_id', 'product')
