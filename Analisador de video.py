import openai
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

# Defina sua chave da API OpenAI
openai.api_key = 'sua-chave-api-openai'


def obter_transcricao(video_url):
    # Extrair o ID do vídeo da URL do YouTube
    video_id = video_url.split('v=')[-1]

    try:
        # Obtém a transcrição automática (se disponível)
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        formatter = TextFormatter()
        transcript_text = formatter.format_transcript(transcript)
        return transcript_text
    except Exception as e:
        print("Erro ao obter a transcrição:", e)
        return None


def resumir_como_chatgpt(texto):
    try:
        # Fazendo uma chamada para o modelo GPT-3 para resumir o texto
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "Você é um assistente inteligente que resume e analisa conteúdo de vídeos."},
                {"role": "user", "content": f"Por favor, resuma e analise o seguinte texto: {texto}"}
            ]
        )
        resumo = response['choices'][0]['message']['content']
        return resumo
    except Exception as e:
        print("Erro ao interagir com o ChatGPT:", e)
        return None


def analisar_video(video_url):
    # Extrair transcrição do vídeo
    transcricao = obter_transcricao(video_url)

    if transcricao:
        print("\nTranscrição extraída com sucesso!")
        print("\n--- Início do resumo ---\n")

        # Passar a transcrição para o ChatGPT para análise
        resumo = resumir_como_chatgpt(transcricao)

        if resumo:
            print("Resumo do vídeo:\n")
            print(resumo)
        else:
            print("Erro ao gerar resumo com o ChatGPT.")
    else:
        print("Não foi possível obter a transcrição do vídeo.")


# URL do vídeo do YouTube que você quer analisar
video_url = input("Informe a URL do vídeo do YouTube: ")
analisar_video(video_url)
