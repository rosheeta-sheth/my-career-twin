---
title: twin
app_file: app.py
sdk: gradio
sdk_version: 6.14.0
---
# Rosheeta's Career Twin — Text-Only UI

This version removes all microphone, transcription, text-to-speech, audio playback, and browser speech-synthesis features.

## Replace these files

Copy the following into the existing project:

- `app.py`
- `styles.py`
- `requirements.txt`

The old `voice.py` file is no longer imported and can be deleted.

## Run

```bash
pip install -r requirements.txt
python app.py
```

## Environment variables

The existing `.env` file should continue to contain:

```env
OPENAI_API_KEY=your_key
PUSHOVER_USER=your_pushover_user_key
PUSHOVER_TOKEN=your_pushover_app_token
```

Optionally override the model without editing code:

```env
OPENAI_MODEL=gpt-5.4-mini
```

## UI changes

- Replaced the voice toolbar with a simple chat status and New Chat control.
- Removed microphone upload/recording, playback controls, and read-aloud options.
- Added a cleaner career-focused header with contact links and skill tags.
- Reduced the chatbot to one visible surface per message to eliminate nested bubbles.
- Added a compact composer, responsive question cards, improved mobile behavior, and clearer loading/error states.
- Limited chatbot actions to Copy so the header is less cluttered.
