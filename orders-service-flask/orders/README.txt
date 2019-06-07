Uwierzytelnianie użytkowników odbywa się za pomocą mechanizmu tokenów (JWT).
Do ciała każdego żądania jest dołączany token, który jest zaszyfrowanym JSON-em o 
postaci {'customer_id' : <identyfikator_klienta>}, np. {'customer_id' : 1}

Token jest szyfrowany i odszyfrowywany algorytmem RS256.
Algorytm ten zakłada wykorzystanie dwóch kluczy - prywatnego i publicznego.

Szyfrować można tylko prywatnym kluczem.
Do odszyfrowywania wystarczy klucz publiczny.

Klucz publiczny przechowywany jest w pliku jwt-key.pub

Przykład tokenu:

zakodowany -> eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJjdXN0b21lcl9pZCI6Mn0.AZ61fdfPRBiHLyiO5WyTyu3uNQJaJpXb9H6COtoF8oyhIdrRazcbn-ebv-DYxt0Qno6FpGQnGOfwsxRdHWXyBMB5fL1mf1XZ7GxjVOFcNHNeL-5PfaEPPhwv-pr3--0U6AhOUn6zqG07fpWvvcMG1QYRoU4k2RngaI6zVDFRHaU
odkodowany -> {'customer_id': 2}


Przykład tokena w żądaniu:
{
	"token" : "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJjdXN0b21lcl9pZCI6Mn0.AZ61fdfPRBiHLyiO5WyTyu3uNQJaJpXb9H6COtoF8oyhIdrRazcbn-ebv-DYxt0Qno6FpGQnGOfwsxRdHWXyBMB5fL1mf1XZ7GxjVOFcNHNeL-5PfaEPPhwv-pr3--0U6AhOUn6zqG07fpWvvcMG1QYRoU4k2RngaI6zVDFRHaU"
}
