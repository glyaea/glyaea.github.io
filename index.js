import("./base.js");

document.head.append(Object.assign(document.createElement("script"), {
	type: "speculationrules",
	textContent: '{ "prerender": [{ "source": "document", "eagerness": "moderate" }] }'
}));
