from marshmallow import Schema, fields

class CategoriesSchema(Schema):
	class Meta:
		fields = ('id', 'name')
		exclude = ('products', )

class ProductResourcesSchema(Schema):
	class Meta:
		fields = ('pictureFileUrl', 'productDescription')
		exclude = ('id', 'product_id')

class ProductsSchema(Schema):
	id = fields.Integer()
	name = fields.String()
	price = fields.Float()
	resources = fields.Nested(ProductResourcesSchema)
