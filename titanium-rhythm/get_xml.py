import acoustid
import sys
import urllib.request

class Identify():
	def __init__(self, api_key, filename):
		self.api_key = api_key
		self.filename = filename
		
	def aidmatch(self):
		try:
			results = acoustid.match(self.api_key, self.filename)
		except acoustid.NoBackendError:
			print("chromaprint library/tool not found", file=sys.stderr)
			sys.exit(1)
		except acoustid.FingerprintGenerationError:
			print("fingerprint could not be calculated", file=sys.stderr)
			sys.exit(1)
		except acoustid.WebServiceError as exc:
			print("web service request failed:", exc.message, file=sys.stderr)
			sys.exit(1)

		for score, rid, title, artist in results:
			url = "https://musicbrainz.org/ws/2/recording/{0}?inc=aliases%2Bartist-credits%2Breleases".format(rid)
			response = urllib.request.urlopen(url)
			data = response.read()      # a `bytes` object
			text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
			with open(self.filename[:-4]+'.xml', 'w') as f:
				print(text, file = f)
			
if __name__ == '__main__':
	i = Identify('PMaILC8xG3', sys.argv[1])
	i.aidmatch()
