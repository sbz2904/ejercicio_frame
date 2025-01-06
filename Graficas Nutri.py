import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os

# Load the dataset
file_path = '/content/Nutriway (Respuestas).xlsx'
data = pd.read_excel(file_path, sheet_name='Respuestas de formulario 1')

# Strip whitespace from column names
data.columns = data.columns.str.strip()

# Create output directory
output_dir = "graficos/"
os.makedirs(output_dir, exist_ok=True)

# Function for bar chart
def save_bar_chart(data, column, filename):
    counts = data[column].value_counts()
    plt.figure(figsize=(10, 6))
    counts.plot(kind='bar', color='skyblue')
    plt.title(f"{column}", fontsize=14)
    plt.xlabel("Respuestas", fontsize=12)
    plt.ylabel("Frecuencia", fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(output_dir + filename)
    plt.close()

# Function for word cloud
def save_word_cloud(data, column, filename):
    text = ' '.join(str(response) for response in data[column].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f"Nube de Palabras: {column}", fontsize=14)
    plt.tight_layout()
    plt.savefig(output_dir + filename)
    plt.close()

# Define questions
multiple_choice_questions = [
    "¿Qué tan importante es para ti llevar una alimentación saludable?",
    "¿Con qué frecuencia buscas mejorar tu alimentación o cumplir metas de salud?",
    "¿Tienes alguna meta nutricional específica?",
    "¿Te preocupa el impacto ambiental de tus elecciones alimentarias?",
    "¿Sueles investigar sobre los ingredientes de los alimentos que consumes?",
    "¿Qué te motiva a probar nuevos alimentos o dietas?",
    "¿Utilizas alguna aplicación o plataforma para llevar un seguimiento de tu alimentación?",
    "¿Estarías interesado/a en recibir recomendaciones personalizadas de alimentos saludables y sostenibles?",
    "¿Te gustaría que el asistente se conecte con productores locales para conseguir ingredientes frescos y económicos?",
    "¿Pagarías por un servicio que personalice tu alimentación y facilite el acceso a los ingredientes?",
    "¿Cuánto estarías dispuesto a pagar por un servicio de suscripción que te ofrezca recomendaciones personalizadas y acceso a productos exclusivos?",
    "¿Qué tan probable sería que recomendaras este producto a amigos o familiares interesados en mejorar su nutrición?"
]

open_ended_questions = [
    "¿Qué características te gustaría que tuviera este asistente para que sea más útil para ti?",
    "¿Qué mejorarías o agregarías a un asistente personalizado de nutrición como este?",
    "¿Cuáles son tus principales obstáculos para llevar una alimentación saludable en tu día a día?"
]

# Generate visualizations
for i, question in enumerate(multiple_choice_questions):
    save_bar_chart(data, question, f"multiple_choice_{i+1}.png")

for i, question in enumerate(open_ended_questions):
    save_word_cloud(data, question, f"open_ended_{i+1}.png")

print("Analysis completed. Graphs saved in the 'graficos' folder.")
