import {marked} from "https://cdn.jsdelivr.net/npm/marked@18.0.6/lib/marked.esm.js";
import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";

mermaid.initialize({startOnLoad: false});
await mermaid.run();

window.MathJax = {tex: {inlineMath: {"[+]": [["$", "$"]]}}};

await new Promise((resolve, reject) =>
	document.head.append(Object.assign(document.createElement("script"), {
		onerror: reject,
		onload: resolve,
		src: "https://cdn.jsdelivr.net/npm/mathjax@4.1.3/tex-mml-chtml.js"
	}))
);

fetch("https://gregorylimeurhen.goatcounter.com/counter/TOTAL.json")
	.then(response => response.json())
	.then(response => console.log(response.count));

const article = document.querySelector("article");
const blog = document.querySelector("blog");
const posts = document.querySelector("dl");

marked.use({
	extensions: [
		{
			name: "mathBlock",
			level: "block",
			tokenizer(source) {
				const match = /^\$\$[\s\S]+?\$\$(?:\n|$)/.exec(source);
				if (match) return {type: "mathBlock", raw: match[0]};
			},
			renderer(token) {
				return token.raw;
			}
		},
		{
			name: "mathInline",
			level: "inline",
			tokenizer(source) {
				const match = /^\$[^$\n]+?\$/.exec(source);
				if (match) return {type: "mathInline", raw: match[0]};
			},
			renderer(token) {
				return token.raw;
			}
		}
	],
	hooks: {
		preprocess(markdown) {
			return markdown.replace(/\$\$[\s\S]+?\$\$|\$[^$\n]+?\$/g, math =>
				math.replaceAll("\\", "&#92;"));
		}
	}
});

for (const anchor of document.querySelectorAll("nav a:not([href])")) {
	anchor.onclick = () => {
		for (const element of document.querySelectorAll("home, blog")) {
			element.hidden = element.localName !== anchor.textContent.toLowerCase();
		}
		blog.replaceChildren(posts);
	};
}

for (const anchor of document.querySelectorAll("blog a")) {
	anchor.onclick = async () => {
		const slug = anchor.textContent
			.normalize("NFKD")
			.toLowerCase()
			.replace(/[^\w\s-]/g, "")
			.replace(/[-\s]+/g, "-")
			.replace(/^[-_]+|[-_]+$/g, "");
		const response = await fetch(`posts/${slug}.md`);
		const markdown = await response.text();
		const postMarkdown = markdown.replace(/^---\n.*?\n---\n/s, "");
		await MathJax.startup.promise;
		MathJax.typesetClear([article]);
		article.innerHTML = marked.parse(postMarkdown);
		await MathJax.typesetPromise([article]);
		blog.replaceChildren(article);
	};
}
