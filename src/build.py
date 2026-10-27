#!/usr/bin/env python3
"""Build index.html from content/*.md.

Markdown subset: #/##/### headings, paragraphs, - bullets, 1. numbered,
| tables |, > blockquotes, **bold**, *italic*, `code`, ---.
Provenance: one or more lines starting with "::src " directly under a heading:
    ::src Label :: explanation text
Each ##/### heading becomes a section with a Source button on the right.
"""
import html, re, sys, pathlib, json

ROOT = pathlib.Path(__file__).parent
DOCS = [
    ("case", "Case-making", "01-case-making.md"),
    ("district", "District commitments", "02-district-commitments.md"),
    ("chss", "CHSS commitment", "03-chss-commitment.md"),
]

LABEL_CLASS = {
    "Luke's experience": "src-luke",
    "Conversation": "src-call",
    "James's collateral": "src-james",
    "James's MOU draft": "src-james",
    "AFUHSD precedent": "src-luke",
    "Case law / guidance": "src-law",
    "Emily's architecture": "src-emily",
    "Emily's email": "src-emily",
    "FERPA": "src-law",
    "PPRA": "src-law",
    "COPPA": "src-law",
    "State law": "src-law",
    "SDPC NDPA": "src-sdpc",
    "Columbus City DSA": "src-district",
    "San Diego CCAP": "src-district",
    "Lewis County": "src-district",
    "af-dpa": "src-afdpa",
    "Drafting choice": "src-choice",
}

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    return s

def render_sources(srcs):
    if not srcs:
        return ""
    items = []
    for label, text in srcs:
        cls = LABEL_CLASS.get(label, "src-other")
        items.append(f'<li><span class="tag {cls}">{html.escape(label)}</span> {inline(text)}</li>')
    return ('<div class="srcwrap"><button class="srcbtn" type="button" aria-expanded="false" '
            'aria-label="Where this language came from">Source</button>'
            f'<div class="pop" role="dialog"><div class="pop-h">Where this came from</div><ul>{"".join(items)}</ul></div></div>')

def convert(md):
    lines = md.splitlines()
    out = []
    i = 0
    # pending heading waiting for ::src lines
    pending = None  # (level, text, srcs)
    sec_open = False
    list_stack = []  # 'ul' or 'ol'

    def close_lists():
        while list_stack:
            out.append(f"</{list_stack.pop()}>")

    def flush_heading():
        nonlocal pending, sec_open
        if pending is None:
            return
        level, text, srcs = pending
        close_lists()
        if level >= 2:
            if sec_open:
                out.append("</section>")
            sid = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
            out.append(f'<section class="sec lvl{level}" id="{sid}">')
            sec_open = True
            out.append(f'<div class="sec-head"><h{level}>{inline(text)}</h{level}>{render_sources(srcs)}</div>')
        else:
            out.append(f'<h1>{inline(text)}</h1>')
            if srcs:
                out.append(render_sources(srcs))
        pending = None

    while i < len(lines):
        ln = lines[i]
        if ln.startswith("::src "):
            if pending is not None:
                body = ln[6:]
                label, _, text = body.partition(" :: ")
                pending[2].append((label.strip(), text.strip()))
            i += 1
            continue
        m = re.match(r"^(#{1,3})\s+(.*)$", ln)
        if m:
            flush_heading()
            pending = (len(m.group(1)), m.group(2).strip(), [])
            i += 1
            continue
        flush_heading()
        if not ln.strip():
            close_lists()
            i += 1
            continue
        if ln.strip() == "---":
            close_lists(); out.append("<hr>"); i += 1; continue
        if ln.startswith("|"):
            close_lists()
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append(lines[i]); i += 1
            cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
            cells = [r for r in cells if not all(re.fullmatch(r":?-{2,}:?", c) for c in r)]
            t = ["<table>"]
            if cells:
                t.append("<thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in cells[0]) + "</tr></thead>")
                t.append("<tbody>")
                for r in cells[1:]:
                    t.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
                t.append("</tbody>")
            t.append("</table>")
            out.append("".join(t))
            continue
        if ln.startswith("> "):
            close_lists()
            q = []
            while i < len(lines) and lines[i].startswith(">"):
                q.append(lines[i][1:].strip()); i += 1
            paras = "\n".join(q).split("\n\n")
            out.append("<blockquote>" + "".join(f"<p>{inline(p.replace(chr(10),' '))}</p>" for p in paras if p.strip()) + "</blockquote>")
            continue
        mb = re.match(r"^(\s*)- (.*)$", ln)
        mo = re.match(r"^(\s*)\d+\. (.*)$", ln)
        if mb or mo:
            kind = "ul" if mb else "ol"
            text = (mb or mo).group(2)
            if not list_stack or list_stack[-1] != kind:
                close_lists(); out.append(f"<{kind}>"); list_stack.append(kind)
            out.append(f"<li>{inline(text)}</li>")
            i += 1
            continue
        # paragraph: gather continuation lines
        p = [ln.strip()]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#{1,3} |::src |- |\d+\. |\| |> |---$)", lines[i]):
            p.append(lines[i].strip()); i += 1
        close_lists()
        out.append(f"<p>{inline(' '.join(p))}</p>")
    flush_heading()
    close_lists()
    if sec_open:
        out.append("</section>")
    return "\n".join(out)

def main():
    tpl = (ROOT / "template.html").read_text()
    panels, tabs = [], []
    for key, title, fn in DOCS:
        body = convert((ROOT / "content" / fn).read_text())
        panels.append(f'<article class="doc" id="doc-{key}" data-doc="{key}" hidden>{body}</article>')
        tabs.append(f'<button class="tab" type="button" data-doc="{key}" role="tab" aria-selected="false">{html.escape(title)}</button>')
    page = tpl.replace("<!--TABS-->", "\n".join(tabs)).replace("<!--PANELS-->", "\n".join(panels))
    (ROOT / "dist").mkdir(exist_ok=True)
    (ROOT / "dist" / "index.html").write_text(page)
    print("wrote", ROOT / "dist" / "index.html", len(page), "bytes")

if __name__ == "__main__":
    main()
