# Pradeep Biswal — former domain

Small GitHub Pages forwarding site for `pb.kabitawithoutborders.org`. The main website lives at https://pradeepbiswal.in/ and is maintained in ahimanikya/pradeep-biswal.

The browser redirect preserves path, query and fragment, including book chapters and private review invitation fragments. No analytics or external resources run here. Both index and 404 implement the same forwarding, so old deep links work. JavaScript is required for automatic forwarding; a visible destination link and instructions remain as a fallback. This is browser forwarding, not a server-side HTTP 301.

`routes.json` lists maintained website pages. Run `python3 generate-redirects.py` to regenerate HTML and extensionless forwarding pages; known bookmarks return HTTP 200 before forwarding. Unknown legacy paths use the 404 fallback.
