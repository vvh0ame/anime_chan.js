class AnimeChan {
	constructor(apiKey) {
		this.api = "https://animechan.io/api/v1"
		this.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
			"x-api-key": apiKey
		}
	}

	async getRandomQuote() {
		const response = await fetch(
			`${this.api}/quotes/random`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getQuoteByAnime(animeName) {
		const response = await fetch(
			`${this.api}/quotes?anime=${animeName}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getQuoteByCharacter(characterName) {
		const response = await fetch(
			`${this.api}/quotes?character=${characterName}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}
 }

module.exports = {AnimeChan}
