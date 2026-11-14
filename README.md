# Novah · MSc Computer Science

**Software Engineering · Keele University · 2023/24 · 15 CATS · final module result: 61%**

A team coursework prototype for voice-driven desktop assistance. Python modules explore speech input/output, spaCy command parsing, Windows application control, weather/time queries, notes and browsing. Separate camera experiments explore face/hand interaction. Reproducibility and security limits are documented.

[Academic context](docs/ACADEMIC-CONTEXT.md) · [Presentation text](docs/original/novah-presentation-redacted.md) · [Local setup](docs/RUNBOOK.md) · [Architecture](docs/ARCHITECTURE.md) · [Verification](docs/VERIFICATION.md)

## Engineering evidence

| Area | Inspectable evidence |
| --- | --- |
| Team delivery | Historical [Kanban account](KANBAN.md), MoSCoW priorities and group presentation; completion claims are historical self-report. |
| Object-oriented Python | VoiceAssistant/Novah classes and feature modules. |
| Speech/NLP | SpeechRecognition, pyttsx3 and spaCy; no deployed LLM agent is established by these. |
| Desktop integration | Windows automation through PyAutoGUI/ctypes; local files and Tkinter views. |
| Integration resilience | Bounded web requests, environment-based weather configuration and isolated regressions. |
| Critical evaluation | Honest [testing and release gaps](docs/VERIFICATION.md). |

## Repository map

| Path | Purpose |
| --- | --- |
| `Nova Software/` | Main assistant and standalone feature experiments; not every module is wired into main.py. |
| `Nova Authentication/` | Camera coursework experiments, not certified authentication. |
| `Unit and Integration Testing/` | Historical test artifacts; some imports/symbols no longer match this tree. |
| `tests/` | Maintained dependency-isolated regressions. |
| `index.html`, CSS and JavaScript | Historical promotional page with missing assets/incomplete navigation, not an application download. |
| `docs/original/` | Official brief and reviewed NOVAH presentation text. |

## Start with the checks

```sh
git clone https://github.com/jyotheshkar/MSc-CS-Software-Engineering-Keele-University-2024.git
cd MSc-CS-Software-Engineering-Keele-University-2024
python -m unittest discover -s tests -v
```

Follow the [runbook](docs/RUNBOOK.md) for a source-based desktop attempt. No prebuilt installer, successful full desktop run or supported release matrix is supplied. Review [security notes](SECURITY.md) before using microphone, camera or OS automation.

## Authorship and academic year

This is a team project retained in Jyothesh Karnam's portfolio. A reliable per-person contribution ledger was not supplied, so the entire implementation is not attributed solely to him. The final **module** mark of 61% was checked against the owner's private transcript.

Keele's [2023/24 programme specification](https://www.keele.ac.uk/media/keeleuniversity/sas/qa/pgtprogrammespecifications/pgtprogspecs2023-24/Programme-Specification-Computer-Science-Taught-Masters-2023-24.pdf) confirms title and credits. The `2024` suffix identifies that academic year. November 2026 AI-assisted maintenance is recorded separately in [provenance](docs/PROVENANCE.md). No repository-wide licence file is present in the retrieved tree; earlier README references to MIT are not an established licence grant.
