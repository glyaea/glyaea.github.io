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
