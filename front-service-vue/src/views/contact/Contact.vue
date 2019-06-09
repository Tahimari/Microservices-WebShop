<template>
    <div class="add container">
		<b-jumbotron header="Contact Us">
			<b-form class="w-100" method="POST" action="https://formspree.io/galgreg@wp.pl">
				<!-- Email -->
				<b-form-group id="form-email-group" label="Email:" label-for="form-email-input">
					<b-form-input id="form-email-input" name="Email" type="email" required autofocus placeholder="Your email">
					</b-form-input>
				</b-form-group>
				
				<!-- Name -->
				<b-form-group id="form-name-group" label="Name:" label-for="form-name-input">
					<b-form-input id="form-name-input" name="Name" type="text" required placeholder="Your name">
					</b-form-input>
				</b-form-group>

				<!-- Message -->
				<b-form-group id="form-message-group" label="Message:" label-for="form-message-input">
					<b-form-textarea id="form-message-input" name="Message" required placeholder="Your message">
					</b-form-textarea>
				</b-form-group>

				<!-- Submit button -->
				<b-button type="submit" variant="primary">Submit</b-button>
        	</b-form>
		</b-jumbotron>
    </div>
</template>
