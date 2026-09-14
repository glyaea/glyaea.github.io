import markedKatex from "https://esm.sh/marked-katex-extension@5.1.10";
import {marked} from "https://cdn.jsdelivr.net/npm/marked/lib/marked.esm.js";

const article = document.querySelector("article");

marked.use(markedKatex({nonStandard: true}));

if (article) {
	const indentation = article.textContent.match(/^\n([\t ]*)/)[1];
	const postSource = article.textContent.trim().replaceAll(`\n${indentation}`, "\n");
	article.innerHTML = marked.parse(postSource);
	article.hidden = false;
}

const playlist = document.querySelector("table[playlist]");

if (playlist) {
	playlist.addEventListener("click", event => {
		const row = event.target.closest("tr[url]");
		if (row) {
				window.open(row.getAttribute("url"), "_blank", "noopener,noreferrer");
		}
	});
}

fetch("https://gregorylimeurhen.goatcounter.com/counter/TOTAL.json")
	.then(response => response.json())
	.then(response => console.log(response.count));
