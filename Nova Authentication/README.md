# Face and hand coursework experiments

Separate Novah camera experiments; not a verified multifactor authentication system.

| Source | Purpose |
| --- | --- |
| Auth.py | Tkinter/OpenCV/MediaPipe hand-sign capture/comparison. |
| face_auth.py | Camera capture, face comparison and locally encrypted image storage. |
| test.py | Historical manual driver, not an automated security audit. |

Review before enabling a camera. Use only consented test captures and establish deletion/recovery procedures. A match does not prove liveness, spoof resistance, secure enrolment or independent authentication factors.

The main [runbook](../docs/RUNBOOK.md) does not require these modules. Their additional imports include OpenCV, Pillow, NumPy, MediaPipe, face_recognition and cryptography. Native dependency compatibility, a secure release and a dependency lock were not verified.

Placeholder clone/requirements commands and the unsupported MIT assertion were removed. See [academic context](../docs/ACADEMIC-CONTEXT.md) for team attribution and [verification](../docs/VERIFICATION.md) for tested boundaries.
