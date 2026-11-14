# Verification and release boundaries

Reviewed 14 November 2026; the academic result does not grade this maintenance.

```sh
python -m unittest discover -s tests -v
```

The maintained suite extracts actual functions using AST to avoid unavailable audio/GUI dependencies. It exercises web timeout/HTTP failure semantics and checks the web listener does not directly activate at import. Added callback tests use fake widgets and mocked speech/network functions to verify readable success/failure/empty-input results without destroying the window. They test callback behaviour, not Tkinter rendering.

Historical Unit and Integration Testing files are retained as evidence. Some import nova, Jarvis or symbols absent from this tree. They are outside maintained discovery and are not claimed to pass.

| Release gate | Required future evidence |
| --- | --- |
| Reproduction | Clean Windows VM installation, dependency lock, spaCy/PyAudio setup. |
| Devices | Permission denial, absent/noisy microphone, service failure and cancellation. |
| Automation safety | Confirmation for destructive actions, dependable stop control, ambiguous-command tests. |
| GUI responsiveness | Bounded background I/O and safe Tkinter-thread updates. |
| Camera security | Consent/storage/deletion review, liveness/failure tests and a threat model. |
| Distribution | Reproducible build, downloadable assets, uninstall instructions and OS matrix. |
| Accessibility | Evaluation with intended users; no certification is claimed. |

No dependency installation, live API call, biometric capture, full desktop demonstration or accessibility study was performed in this preparation.
