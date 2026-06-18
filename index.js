const article = document.querySelector("article")
const title = document.querySelector("h1")
const homeTitle = title.textContent
const table = document.querySelector("table")

const slugify = title => title.normalize("NFKD").replace(/[^\x00-\x7F]/g, "").toLowerCase()
	.replace(/'/g, "").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "") || "post"

const hyphenateArticle = () => {
	const walker = document.createTreeWalker(article, NodeFilter.SHOW_TEXT)
	const nodes = []
	for (let node = walker.nextNode(); node; node = walker.nextNode()) nodes.push(node)
	nodes
		.filter(node => !node.parentElement.closest(".donthyphenate"))
		.forEach(node => node.data = node.data.replace(/[A-Za-z]{4,}/g, word => [...word].join("\u00AD")))
}

const smartenArticle = () => {
	const walker = document.createTreeWalker(article, NodeFilter.SHOW_TEXT)
	const nodes = []
	for (let node = walker.nextNode(); node; node = walker.nextNode()) nodes.push(node)
	nodes
		.filter(node => !node.parentElement.closest("code, pre, .katex"))
		.forEach(node => node.data = smartquotes.string(node.data))
}

const showTable = () => {
	title.textContent = homeTitle
	article.hidden = true
	table.hidden = false
}

const showPost = async (path, titleValue) => {
	const markdown = (await (await fetch(path)).text()).replace(/^---[\s\S]*?---\s*/, "")
	const math = []
	const text = markdown.replace(/\$\$[\s\S]*?\$\$|\$[^$\n]*?\$/g, value => `@@MATH${math.push(value) - 1}@@`)

	article.innerHTML = marked.parse(text)
		.replace(/@@MATH(\d+)@@([,.)])/g, (_, i, x) => `<nowrap class="donthyphenate">${math[i]}${x}</nowrap>`)
		.replace(/@@MATH(\d+)@@/g, (_, i) => math[i])

	renderMathInElement(article, {
		delimiters: [
			{left: "$$", right: "$$", display: true},
			{left: "$", right: "$", display: false}
		],
		throwOnError: false,
	})

	article.querySelectorAll("pre code").forEach(code => {
		if (window.hljs) hljs.highlightElement(code)
		code.classList.add("donthyphenate")
	})
	article.querySelectorAll(".katex").forEach(math => math.classList.add("donthyphenate"))

	smartenArticle()
	hyphenateArticle()

	table.hidden = true

	article.hidden = false

	title.textContent = titleValue
}

const route = async () => {
	const slug = location.hash.slice(1)
	if (slug) {
		const link = [...document.querySelectorAll("td:nth-child(2) a")].find(link => slugify(link.textContent) === slug)
		await showPost(`posts/${slug}.md`, link.textContent)
		return
	}
	showTable()
}

document.querySelectorAll("td:nth-child(2) a").forEach(link => link.addEventListener("click", async event => {
	event.preventDefault()
	const slug = slugify(link.textContent)
	history.pushState(null, "", `#${slug}`)
	await route()
}))

window.addEventListener("popstate", route)
route()
