from marshmallow import Schema, fields

class OrderStatusSchema(Schema):
	class Meta:
		fields = ('id', 'description')
		exclude = ('order', )

class OrderItemsSchema(Schema):
	id = fields.Integer()
	order_id = fields.Integer()
	product_id = fields.Integer()
	quantity = fields.Integer()

class OrdersSchema(Schema):
	id = fields.Integer()
	customer_id = fields.Integer()
	order_status = fields.Nested(OrderStatusSchema)
	order_items = fields.Nested(OrderItemsSchema(many=True))
