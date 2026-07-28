fetch("https://gregorylimeurhen.goatcounter.com/counter/TOTAL.json")
	.then(response => response.json())
	.then(response => console.log(response.count));
