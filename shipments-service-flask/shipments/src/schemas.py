from marshmallow import Schema, fields

class ShipmentTypesSchema(Schema):
	class Meta:
		fields = ('id', 'name', 'price', 'shipping_time', 'description')

class ShipmentStatesSchema(Schema):
	class Meta:
		fields = ('id', 'name', 'description')
