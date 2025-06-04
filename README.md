# 🗣️ TEXT TO SPEECH EXTENSION
This Chrome extension converts selected text into speech, enabling users to hear content in a **realistic voice**. It supports **multiple tones based on emotional context**, enhancing the listening experience.

## 🔊 Key Features

- ✅ Convert any selected webpage text to speech
- 🎭 Tone detection to read text in **different emotional styles** (e.g., sad, happy, serious)
- 🌍 Language detection and voice switching
- 🎧 Human-like voice using advanced TTS models

## 🧠 How it Works

1. User **selects** a piece of text on a webpage
2. When the user clicks on the extension icon, the selected text gets highlighted.
3. The extension **detects the language and emotional tone**
4. The text is sent to a **MURF TTS  STREAM API**
5. Audio is played back to the user in the corresponding **voice and tone**

## 🛠️ Technologies Used

- JavaScript (Chrome Extension)
- Flask (Backend API)
- Hugging Face Transformers (`emotion-classification`)
- Murf API (for voice generation)
- Langdetect (for language identification)

## To run the project:
- Clone the repo from **https://github.com/UdayaNarne/MURFAI**
- Setup the Virtual Environment
- Install the Required Packages
- Run the Flask Server
- Load the Chrome Extension
  . Open Chrome and go to chrome://extensions/
  . Enable Developer mode (toggle at the top right)
  . Click "Load Unpacked"
  . Select the extension/ folder from the cloned repo
- Visit Any webpage
- Select the text
- Click on the extension icon
- The selected text will be highlighted, and you'll hear it spoken in the appropriate tone and language

