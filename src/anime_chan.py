from requests import get

class AnimeChan:
	def __init__(self) -> None:
		self.api = "https://animechan.vercel.app/api"
		self.headers = {
			"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.86 Chrome/73.0.3683.86 Safari/537.36"
		}

	def get_random_quote(self) -> dict:
		return get(
			f"{self.api}/random",
			headers=self.headers).json()
			
	def get_title_random_quote(
			self,
			title: str) -> dict:
		return get(
			f"{self.api}/random/anime?title={title}",
			headers=self.headers).json()
			
	def get_character_random_quote(
			self,
			name: str) -> dict:
		return get(
			f"{self.api}/random/character?name={name}",
			headers=self.headers).json()
			
	def get_ten_random_quotes(self, page: int = 1) -> list:
		return get(
			f"{self.api}/quotes?page={page}",
			headers=self.headers).json()
			
	def get_ten_title_random_quotes(
			self,
			title: str,
			page: int = 1) -> list:
		return get(
			f"{self.api}/quotes/anime?title={title}&page={page}",
			headers=self.headers).json()
			
	def get_ten_character_random_quotes(
			self,
			name: str,
			page: int = 1) -> list:
		return get(
			f"{self.api}/quotes/character?name={name}&page={page}",
			headers=self.headers).json()
