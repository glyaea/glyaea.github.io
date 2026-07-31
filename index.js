import markedKatex from "https://cdn.jsdelivr.net/npm/marked-katex-extension@5.1.10/+esm";
import {marked} from "https://cdn.jsdelivr.net/npm/marked/lib/marked.esm.js";

const article = document.querySelector("article");
const blogLink = document.querySelector('nav a[href="#"]');
const postList = document.querySelector("dl");

marked.use(markedKatex({nonStandard: true}));

blogLink.addEventListener("click", event => {
	event.preventDefault();
	article.hidden = true;
	postList.hidden = false;
});

for (const postLink of postList.querySelectorAll("a")) {
	postLink.addEventListener("click", async event => {
		event.preventDefault();
		const response = await fetch(postLink.href);
		if (!response.ok) throw new Error();
		const postSource = await response.text();
		const postBody = postSource.replace(/^---\r?\n.*?\r?\n---\r?\n/s, "").trim();
		article.innerHTML = marked.parse(postBody);
		postList.hidden = true;
		article.hidden = false;
	});
}

fetch("https://gregorylimeurhen.goatcounter.com/counter/TOTAL.json")
	.then(response => response.json())
	.then(response => console.log(response.count));
