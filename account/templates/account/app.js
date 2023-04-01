const searchInput = document.getElementById("search-input");
const contactList = document.getElementById("contact-list");
const messageList = document.getElementById("message-list");
let selectedContact = null;

searchInput.addEventListener("keyup", (event) => {
	const searchText = event.target.value.toLowerCase();
	const contacts = Array.from(contactList.children);
	const messages = Array.from(messageList.children);
