<template>
    <div class="add container">
		<b-jumbotron header="Delivery">
			<b-form class="w-100">
				<!-- Shipment Type -->
				<b-form-group id="form-shipment-group" label="Shipment Type:" label-for="form-shipment-input">
					<b-form-select id="form-shipment-input" v-model="shipment_type_id" :options="shipment_options">
                    </b-form-select>
				</b-form-group>
				
				<!-- First Name -->
				<b-form-group id="form-first-name-group" label="First Name:" label-for="form-first-name-input">
					<b-form-input id="form-first-name-input" type="text" required placeholder="Enter your first name">
					</b-form-input>
				</b-form-group>

                <!-- Last Name -->
				<b-form-group id="form-last-name-group" label="Last Name:" label-for="form-last-name-input">
					<b-form-input id="form-last-name-input" type="text" required placeholder="Enter your last name">
					</b-form-input>
				</b-form-group>

                <!-- Postal Line -->
				<b-form-group id="form-postal-line-group" label="Postal Line:" label-for="form-postal-line-input">
					<b-form-input id="form-postal-line-input" type="text" required placeholder="Enter your address">
					</b-form-input>
				</b-form-group>

                <!-- Postal Code -->
				<b-form-group id="form-postal-code-group" label="Postal Code:" label-for="form-postal-code-input">
					<b-form-input id="form-postal-code-input" type="text" pattern="[0-9]{2}\-[0-9]{3}" required placeholder="Enter postal code">
					</b-form-input>
				</b-form-group>

                <!-- City -->
				<b-form-group id="form-city-group" label="City:" label-for="form-city-input">
					<b-form-input id="form-city-input" type="text" required placeholder="Enter your city">
					</b-form-input>
				</b-form-group>

                 <!-- Country -->
				<b-form-group id="form-country-group" label="Country:" label-for="form-country-input">
					<b-form-input id="form-country-input" type="text" required placeholder="Enter your country">
					</b-form-input>
				</b-form-group>

                <!-- Phone Number -->
				<b-form-group id="form-phone-number-group" label="Phone Number:" label-for="form-phone-number-input">
					<b-form-input id="form-phone-number-input" type="tel" pattern="[0-9]{9}" required placeholder="Enter phone number">
					</b-form-input>
				</b-form-group>

				<!-- Submit button -->
				<b-button type="submit" variant="primary"> Buy! </b-button>
        	</b-form>
		</b-jumbotron>
    </div>
</template>