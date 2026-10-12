import { marked } from "https://cdn.jsdelivr.net/npm/marked/lib/marked.esm.js";

document.body.innerHTML = marked.parse(
	document.body.firstChild.textContent
		.replace(/\\\[[\s\S]*?\\\]/g, math => `<div>${math}</div>`)
		.replaceAll("\\", "&#92;")
);

window.MathJax = {
	loader: {
		paths: {
			mathjax: "https://cdn.jsdelivr.net/npm/mathjax@3/es5"
		}
	}
};

await import("https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js");
