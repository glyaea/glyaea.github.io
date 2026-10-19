import {
	remark,
	remarkGfm,
	remarkMath,
	remarkRehype,
	rehypeMathjax,
	rehypeStringify,
	smartquotes
} from "./imports.js";

document.body.innerHTML = String(
	await remark()
		.use(remarkGfm)
		.use(remarkMath)
		.use(remarkRehype)
		.use(rehypeMathjax)
		.use(rehypeStringify)
		.process(
			document.body.firstChild.textContent
				.replaceAll("\\(", "$")
				.replaceAll("\\)", "$")
				.replaceAll("\\[", () => "$$$$")
				.replaceAll("\\]", () => "$$$$")
		)
);

smartquotes(document.body);
