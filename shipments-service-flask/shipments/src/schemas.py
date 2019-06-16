from marshmallow import Schema, fields

class ShipmentTypesSchema(Schema):
	class Meta:
		fields = ('id', 'name', 'price', 'shipping_time', 'description')

class ShipmentStatesSchema(Schema):
	class Meta:
		fields = ('id', 'name', 'description')

class PersonalDataSchema(Schema):
	class Meta:
		fields = ('first_name', 'last_name', 'phone_number')
		exclude = ('id', )

class AddressDataSchema(Schema):
	class Meta:
		fields = ('address_line', 'postal_code', 'city', 'country')
		exclude = ('id', )
