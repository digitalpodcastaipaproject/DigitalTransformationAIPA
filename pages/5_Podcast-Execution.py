import streamlit as st
from components.podcastmanager import PodcastManager
from components.llmservice import LLMService
#import key

llmService = LLMService()
podcastManager = PodcastManager()

st.title("Podcast-Durchführung")
st.write("Willkommen auf der Podcast-Durchführungsseite. Hier können Sie Ihren vorbereiteten Podcast live führen. Basierend auf Ihrer vorher erstellten Struktur, finden Sie hier die generierten Fragen und Inhalte. Sie können Antworten Ihres Gastes mithilfe einer Transkriptionssoftware eingeben und unser Tool wird darauf basierend weitere Folgefragen generieren. Am Ende Ihrer Session können Sie eine Zusammenfassung Ihres Podcasts erstellen, um Ihren Zuhörern einen klaren und zusammenfassenden Überblick zu bieten.")
if not llmService.isAPIKeySet():
    st.error("Bitte zunächst API-Schlüssel hinzufügen.")
elif not podcastManager.isPodcastStructureSet():
    st.error("Bitte nutzen Sie zunächst den Podcast-Planer")
else:
    st.success("Podcast ist bereit zum Durchführen!")
    with st.sidebar:
        st.radio(
            label = "Podcast-Struktur",
            options = podcastManager.getSectionNames(),
            disabled=True,
            index=podcastManager.getCurrentSection()
        )
    if st.button(f"Weiter zu {podcastManager.getSectionByIndex(podcastManager.getCurrentSection())}"):
        podcastManager.nextSection()
