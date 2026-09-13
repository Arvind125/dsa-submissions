from base64 import b64encode as encoder, b64decode as decoder

class Solution:

    def encode(self, strs: List[str]) -> str:
        ss = "|".join(strs)
        ss_bytes = ss.encode("ascii")
        encoded_bytes = encoder(ss_bytes)
        encoded_str = encoded_bytes.decode("ascii")
        
        # print("ENC ", encoded_str)
        return encoded_str


    def decode(self, s: str) -> List[str]:
        encoded_str = s
        encoded_bytes = encoded_str.encode("ascii")

        decoded_bytes = decoder(encoded_bytes)
        decoded_str = decoded_bytes.decode("ascii")

        # print("DEC ", decoded_str)
        return decoded_str.split("|")
