window.MathJax = {tex: {inlineMath: {"[+]": [["$", "$"]]}}};

fetch("https://gregorylimeurhen.goatcounter.com/counter/TOTAL.json")
	.then(response => response.json())
	.then(response => console.log(response.count));

const article = document.querySelector("article");
const blog = document.querySelector("blog");
const postList = document.querySelector("dl");
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
for (const anchor of document.querySelectorAll("nav a")) {
	anchor.onclick = () => {
		for (const element of document.querySelectorAll("home, blog")) {
			element.hidden = element.localName !== anchor.textContent;
		}
		blog.replaceChildren(postList);
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
		if (!response.ok) {
			throw new Error(`Failed to fetch ${response.url}: ${response.status}`);
		}
		const markdown = await response.text();
		const postMarkdown = markdown.replace(/^---\n.*?\n---\n/s, "");
		await MathJax.startup.promise;
		MathJax.typesetClear([article]);
		article.innerHTML = marked.parse(postMarkdown);
		blog.replaceChildren(article);
		await MathJax.typesetPromise([article]);
	};
}
