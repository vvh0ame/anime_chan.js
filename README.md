# anime_chan.js
Web-API for [animechan.io](https://animechan.io/) a free restful API that serves quality anime quotes. [Source](https://github.com/Animechan-API/animechan)

## Example
```JavaScript
async function main() {
	const { AnimeChan } = require("./anime_chan.js")
	const animeChan = new AnimeChan("apiKey")
	const randomQuote = await animeChan.getRandomQuote()
	console.log(randomQuote)
}

main()
```
