# CHSS data agreement drafts

Working drafts of the data partnership language for the Center for High School Success
National 9th Grade Success Accelerator agreement: case-making, the district commitments
(replacement Sections Five and Six), and the CHSS privacy and security commitment
(NDPA posture, Appendix A, system specifications).

Every section carries a Source button showing where its language came from.
The page is marked `noindex`. Drafts for discussion; not legal advice.

Build: `python3 src/build.py` reads `src/content/*.md`, `src/template.html` and `src/VERSION`,
writes `index.html` (always the current version) and freezes a copy at `versions/v<ver>/`.
To cut a new version, edit `src/VERSION` (number on line 1, date on line 2) and rebuild;
the draft tag in the header lists every frozen version.
