import { remark } from "https://esm.sh/remark";
import remarkMath from "https://esm.sh/remark-math";
import remarkRehype from "https://esm.sh/remark-rehype";
import rehypeMathjax from "https://esm.sh/rehype-mathjax@7?bundle";
import rehypeStringify from "https://esm.sh/rehype-stringify";
import smartquotes from "https://esm.sh/smartquotes@2.3.2";

document.body.innerHTML = String(
	await remark().use(remarkMath).use(remarkRehype).use(rehypeMathjax).use(rehypeStringify).process(
		document.body.firstChild.textContent
			.replaceAll("\\(", "$").replaceAll("\\)", "$")
			.replaceAll("\\[", "$$$$").replaceAll("\\]", "$$$$")
	)
);

smartquotes(document.body);
