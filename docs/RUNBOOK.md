# Reviewing and running Novah source

## Maintained checks

From the root, use Python 3.12 or a compatible recent Python:

```sh
python -m unittest discover -s tests -v
```

These checks do not launch audio, the GUI or external APIs.

## Source-based desktop attempt

main.py uses Windows APIs. Use a disposable Windows environment, virtual environment, microphone/audio output and network access. Tkinter must be available in the Python distribution.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-desktop.in
python -m spacy download en_core_web_sm
Set-Location 'Nova Software'
python main.py
```

requirements-desktop.in is a source-derived inventory, not an installed/locked environment verified here. PyAudio may need a suitable platform wheel/build tools. Capture OS/Python/package versions if setup fails.

Weather/time-location features require your own OPENWEATHERMAP_API_KEY in the process environment; .env is not automatically loaded. See [SECURITY.md](../SECURITY.md). SpeechRecognition's Google recognizer can send audio to an external service.

## Entry points and real limits

main.py loads spaCy, starts listening and accepts a wake phrase such as “hey novah”. Its dispatcher covers application open/close, scrolling, jokes, weather and date/time. Other modules are standalone experiments, not a unified catalogue. Ctrl+C can stop the terminal process; no tested global emergency-stop flow is provided.

web.py has its own speech/Tkinter interface. The 14 November callback fix keeps results visible instead of destroying the window immediately. Network and speech work still run on the GUI thread, so responsiveness remains limited. A full microphone/GUI run is not verified here.

Camera modules need additional native vision dependencies and can retain biometric material locally. They are optional separate experiments, not protection for a real account. Review storage/deletion and obtain consent from anyone recorded.

## Outstanding setup/distribution gaps

- No verified installer, build/release artifact or supported OS matrix.
- No dependency lock or clean-machine installation result.
- Historical tests include imports/classes absent from current source.
- The old landing page references missing image assets.
- Presentation mentions of Gemini do not establish a working integration in the dispatcher.
