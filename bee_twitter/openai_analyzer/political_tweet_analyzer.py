import openai
from loguru import logger


class PoliticalTweetAnalyzer:
    def __init__(self, api_key):
        self.api_key = api_key

    def analyze_tweet(self, post_text):
        openai.api_key = self.api_key

        prompt = f"""
        Textos oriúndos de figuras políticas devem necessariamente conter alguns elementos que façam jus ao cargo. 
        Analise o post a seguir do ponto de vista do que se espera de um servidor público falando a seus eleitores. 
        No final, mostre o percentual desas características em uma lista:
        Objetividade, Autruísmo, Tom Acusatório, Ironia, Sarcasmo, Utilidade Pública.
        Dê, também o percentual geral de qualidade do post do ponto de vista da mensagem de uma figura política 
        importante. No final, faça um texto resumo do porquê da nota.  
        no formato da resposta utilize este formato - exemplo: Objetividade: 0%, Autruísmo: 0%, Tom Acusatório: 0%, Ironia: 0%, Sarcasmo: 0%, Utilidade Pública: 0%, Percentual geral: 0%, texto: ´´
        Post: \n{post_text}
        """

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=750,
            n=7,
            stop=None,
            temperature=0.4,
            frequency_penalty=0.2,
            presence_penalty=0.0
        )
        logger.info(f"Resposta do OpenAI: {response}")

        return response['choices'][0]['text']
