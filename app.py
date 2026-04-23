import streamlit as st
from telethon import TelegramClient
import asyncio

# Récupération des clés depuis les secrets Streamlit
api_id = st.secrets["API_ID"]
api_hash = st.secrets["API_HASH"]

st.title("Mon Tunnel Telegram")

# Initialisation du client
# Note: 'anon' est utilisé ici pour simplifier, 
# mais pour une session persistante, on utilisera un fichier .session
client = TelegramClient('anon', api_id, api_hash)

async def main():
    if not client.is_connected():
        await client.start()
        
    st.write("Connecté à Telegram !")
    
    # Exemple : Lister les 5 dernières discussions
    async for dialog in client.iter_dialogs(limit=5):
        st.write(f"- {dialog.name}")

if __name__ == '__main__':
    # Streamlit et async ne font pas toujours bon ménage, 
    # on utilise asyncio.run pour exécuter la logique
    asyncio.run(main())