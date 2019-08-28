<template>
    <div class="add container" v-if="token">
		<b-jumbotron v-if="isCartEmpty">
                <h2 align="center" class="display-3"> Cannot send delivery request, your cart is empty! </h2>
		</b-jumbotron>
		<b-jumbotron header="Delivery" v-else>
			<b-form class="w-100" @submit="onSubmit">
				<b-form-group id="form-shipment-group" label="Shipment Type:" label-for="form-shipment-input">
					<b-form-select id="form-shipment-input" v-model="addShipmentForm.shipmentTypeID" :options="shipmentTypeOptions">
                    </b-form-select>
				</b-form-group>
				<b-form-group id="form-first-name-group" label="First Name:" label-for="form-first-name-input">
					<b-form-input id="form-first-name-input" type="text" required v-model="addShipmentForm.firstName" placeholder="Enter your first name">
					</b-form-input>
				</b-form-group>
				<b-form-group id="form-last-name-group" label="Last Name:" label-for="form-last-name-input">
					<b-form-input id="form-last-name-input" type="text" required v-model="addShipmentForm.lastName" placeholder="Enter your last name">
					</b-form-input>
				</b-form-group>
				<b-form-group id="form-address-line-group" label="Address Line:" label-for="form-address-line-input">
					<b-form-input id="form-address-line-input" type="text" required v-model="addShipmentForm.addressLine" placeholder="Enter your address">
					</b-form-input>
				</b-form-group>
				<b-form-group id="form-postal-code-group" label="Postal Code:" label-for="form-postal-code-input">
					<b-form-input id="form-postal-code-input" type="text" pattern="[0-9]{2}-[0-9]{3}" v-model="addShipmentForm.postalCode" required placeholder="Enter postal code">
					</b-form-input>
				</b-form-group>
				<b-form-group id="form-city-group" label="City:" label-for="form-city-input">
					<b-form-input id="form-city-input" type="text" v-model="addShipmentForm.city" required placeholder="Enter your city">
					</b-form-input>
				</b-form-group>
				<b-form-group id="form-country-group" label="Country:" label-for="form-country-input">
					<b-form-input id="form-country-input" type="text" v-model="addShipmentForm.country" required placeholder="Enter your country">
					</b-form-input>
				</b-form-group>
				<b-form-group id="form-phone-number-group" label="Phone Number:" label-for="form-phone-number-input">
					<b-form-input id="form-phone-number-input" type="tel" pattern="[0-9]{9}" v-model="addShipmentForm.phoneNumber" required placeholder="Enter phone number">
					</b-form-input>
				</b-form-group>
				<div class="modal-footer">
					<b-button variant="danger" to="/"> Back to shop </b-button>
					<b-button variant="info" to="/cart" text-white> Back to cart </b-button>
					<b-button type="submit" variant="success"> Buy! </b-button>
				</div>
        	</b-form>
		</b-jumbotron>
    </div>
	<div v-else>
		<b-jumbotron>
                <h2 align="center" class="display-3"> Please log in to see this page! </h2>
		</b-jumbotron> 
	</div>
</template>

<script>
import axios from 'axios';

export default {
	data() {
		return {
            token: '',
			isCartEmpty: true,
			order_id: 0,
			shipmentTypes: [],
			shipmentTypeOptions: [],
			addShipmentForm: {
				shipmentTypeID: 0,
				firstName: '',
				lastName: '',
				addressLine: '',
				postalCode: '',
				city: '',
				country: '',
				phoneNumber: ''
			}
		}
    },
    mounted() {
        if (localStorage.token) {
            this.token = localStorage.token;
			this.checkIfCartIsNotEmpty();
        }
    },
	watch:{
		$route (to, from){
            if (localStorage.token) {
                this.token = localStorage.token;
				this.checkIfCartIsNotEmpty();
            } else {
                this.token = '';
            }
		}
	}, 
	methods: {
		clearAddShipmentForm() {
			this.addShipmentForm.shipmentTypeID = 0;
			this.addShipmentForm.firstName = '';
			this.addShipmentForm.lastName = '';
			this.addShipmentForm.addressLine = '';
			this.addShipmentForm.postalCode = '';
			this.addShipmentForm.city = '';
			this.addShipmentForm.country = '';
			this.addShipmentForm.phoneNumber = '';
		},
		addNewShipment(payload) {
			const path = `${process.env.VUE_APP_SHIPMENTS_SERVICE_URL}/shipments`;
			axios.post(path, payload)
			.then((res) => {
				this.setOrderAsComplete();
				this.clearAddShipmentForm();
				this.$router.push({path: '/'});
				window.eventBus.$emit('successOrderCompleted', 'Your order has been accepted')
			})
			.catch((error) => {
				console.error(error);
			});
		},
		setOrderAsComplete() {
			const path = `${process.env.VUE_APP_ORDERS_SERVICE_URL}/orders/${this.order_id}`;
			const payload = {
				token: this.token,
				new_status_code: 1
			}
			axios.put(path, payload)
			.then(() => {
				this.order_id = 0;
				this.isCartEmpty = true;
			})
			.catch((error) => {
				console.error(error);
			});
		},
		onSubmit(evt) {
			evt.preventDefault();
			const payload = {
				token: this.token,
				order_id: this.order_id,
				shipment_type_id: this.addShipmentForm.shipmentTypeID,
				mailing_data: {
					personal_data: {
						first_name: this.addShipmentForm.firstName,
						last_name: this.addShipmentForm.lastName,
						phone_number: this.addShipmentForm.phoneNumber
					},
					address_data : {
						address_line: this.addShipmentForm.addressLine,
						postal_code: this.addShipmentForm.postalCode,
						city: this.addShipmentForm.city,
						country: this.addShipmentForm.country
					}
				}
			};
			this.addNewShipment(payload);
		},
		setShipmentOptions(shipmentTypes) {
			let defaultOption = { value: 0, text: 'Select shipment type', disabled: true};
			this.shipmentTypeOptions.push(defaultOption);
			for (var i = 0; i < shipmentTypes.length; i++) {
				let tempType = shipmentTypes[i];
				let tempValue = tempType.id;
				let name = tempType.name;
				let price = tempType.price;
				let shippingTime = tempType.shipping_time;
				let tempText = `${name}, price: ${price} zł, delivery time: ${shippingTime} days.`;
				let tempOption = {value: tempValue, text: tempText};
				this.shipmentTypeOptions.push(tempOption);
			}
		},
		getShipmentTypes() {
			const path = `${process.env.VUE_APP_SHIPMENTS_SERVICE_URL}/shipments/types`;
			axios.get(path)
			.then((res) => {
				this.shipmentTypes = res.data.data;
				this.setShipmentOptions(this.shipmentTypes);
			})
			.catch((error) => {
				console.error(error);
			});
		},
        hideModal(modalID) {
            this.$bvModal.hide(modalID);
        },
		checkIfCartIsNotEmpty() {
			if (this.token) {
				const path = `${process.env.VUE_APP_ORDERS_SERVICE_URL}/orders/pending`;
				axios.get(path, {
					params: {
						token: this.token
					}
				})
				.then((res) => {
					this.isCartEmpty = false;
					this.order_id = res.data.data.order_id;
					this.getShipmentTypes();
				})
				.catch((error) => {
					if (error.response) {
						if (error.response.status === 404) {
							this.isCartEmpty = true;
							this.order_id = 0;
							return;
						}
					}
					console.error(error);
				});
			}
		}
	}
}
</script>