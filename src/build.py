#!/usr/bin/env python3
"""Build the drafts site.

Reads src/content/*.md, src/template.html and src/VERSION; writes
<site>/index.html (current) and <site>/versions/v<ver>/index.html (frozen copy).

Markdown subset: #/##/### headings, paragraphs, - bullets, 1. numbered,
| tables |, > blockquotes, **bold**, *italic*, `code`, ---.
Provenance: lines starting with "::src " directly under a heading:
    ::src Label :: explanation
The document's own (# heading) sources render beside the first paragraph;
each ##/### heading gets a Source pill in the side column.
"""
import html, re, pathlib

ROOT = pathlib.Path(__file__).parent          # src/
SITE = ROOT.parent                             # site root (index.html lives here)

DOCS = [
    # key, tab title, content file, group
    ("case",      "Case-making",          "01-case-making.md",          "deliverable"),
    ("district",  "District commitments", "02-district-commitments.md", "deliverable"),
    ("chss",      "CHSS commitment",      "03-chss-commitment.md",      "deliverable"),
    ("james",     "Notes",                "04-notes-for-james.md",      "note"),
    ("decisions", "Decisions",            "05-decisions.md",            "note"),
]

LABEL_CLASS = {
    "Luke's experience": "src-luke",
    "AFUHSD precedent": "src-luke",
    "Conversation": "src-call",
    "James's collateral": "src-james",
    "James's MOU draft": "src-james",
    "Emily's architecture": "src-emily",
    "Emily's email": "src-emily",
    "FERPA": "src-law",
    "PPRA": "src-law",
    "COPPA": "src-law",
    "State law": "src-law",
    "Case law / guidance": "src-law",
    "SDPC NDPA": "src-sdpc",
    "Columbus City DSA": "src-district",
    "San Diego CCAP": "src-district",
    "Lewis County": "src-district",
    "af-dpa": "src-afdpa",
    "Drafting choice": "src-choice",
}

HOWTO = (
    '<div class="srcwrap howto"><button class="pillbtn" type="button" aria-expanded="false" '
    'aria-label="How to read this page">How to read this</button>'
    '<div class="pop" role="dialog"><div class="pop-h">How to read this</div>'
    '<p>Working drafts for the accelerator agreement. Every section has a <span class="tag src-choice">Source</span> '
    'pill in the right-hand column; hover or tap it to see where the language came from.</p>'
    '<p><span class="tag src-luke">Luke\'s experience</span><span class="tag src-call">Conversation</span>'
    '<span class="tag src-james">James\'s collateral</span><span class="tag src-emily">Emily\'s architecture</span>'
    '<span class="tag src-law">FERPA / PPRA / state law</span><span class="tag src-sdpc">SDPC NDPA</span>'
    '<span class="tag src-district">District agreements</span><span class="tag src-afdpa">af-dpa knowledge base</span>'
    '<span class="tag src-choice">Drafting choice</span></p>'
    '<p>For discussion among the CHSS team and partner districts. Not legal advice; counsel reviews before anything is signed.</p>'
    '</div></div>'
)


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
    return ('<div class="srcwrap"><button class="pillbtn" type="button" aria-expanded="false" '
            'aria-label="Where this language came from">Source</button>'
            f'<div class="pop" role="dialog"><div class="pop-h">Where this came from</div><ul>{"".join(items)}</ul></div></div>')


def convert(md):
    lines = md.splitlines()
    out = []
    i = 0
    pending = None          # (level, text, srcs) heading waiting for ::src lines
    sec_open = False
    list_stack = []
    doc_srcs = None         # sources of the # heading, shown beside the first paragraph
    first_block = False

    def close_lists():
        while list_stack:
            out.append(f"</{list_stack.pop()}>")

    def emit_block(h):
        nonlocal first_block
        if first_block:
            out.append(f'<div class="firstwrap">{h}{render_sources(doc_srcs)}</div>')
            first_block = False
        else:
            out.append(h)

    def flush_heading():
        nonlocal pending, sec_open, doc_srcs, first_block
        if pending is None:
            return
        level, text, srcs = pending
        close_lists()
        if level >= 2:
            if first_block:          # no paragraph followed the title; attach there instead
                out.append(render_sources(doc_srcs)); first_block = False
            if sec_open:
                out.append("</section>")
            sid = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
            out.append(f'<section class="sec lvl{level}" id="{sid}">')
            sec_open = True
            out.append(f'<div class="sec-head"><h{level}>{inline(text)}</h{level}>{render_sources(srcs)}</div>')
        else:
            out.append(f'<div class="titlewrap"><h1>{inline(text)}</h1>{HOWTO}</div>')
            doc_srcs = srcs
            first_block = bool(srcs)
        pending = None

    while i < len(lines):
        ln = lines[i]
        if ln.startswith("::src "):
            if pending is not None:
                label, _, text = ln[6:].partition(" :: ")
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
            close_lists(); i += 1; continue
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
                t.append("<thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in cells[0]) + "</tr></thead><tbody>")
                for r in cells[1:]:
                    t.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
                t.append("</tbody>")
            t.append("</table>")
            emit_block("".join(t))
            continue
        if ln.startswith("> "):
            close_lists()
            q = []
            while i < len(lines) and lines[i].startswith(">"):
                q.append(lines[i][1:].strip()); i += 1
            paras = "\n".join(q).split("\n\n")
            emit_block("<blockquote>" + "".join(f"<p>{inline(p.replace(chr(10), ' '))}</p>" for p in paras if p.strip()) + "</blockquote>")
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
        p = [ln.strip()]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#{1,3} |::src |- |\d+\. |\| |> |---$)", lines[i]):
            p.append(lines[i].strip()); i += 1
        close_lists()
        emit_block(f"<p>{inline(' '.join(p))}</p>")
    flush_heading()
    close_lists()
    if first_block:
        out.append(render_sources(doc_srcs))
    if sec_open:
        out.append("</section>")
    return "\n".join(out)


def version_info():
    raw = (ROOT / "VERSION").read_text().strip().splitlines()
    ver = raw[0].strip()
    date = raw[1].strip() if len(raw) > 1 else ""
    return ver, date


def versions_list(current):
    vdir = SITE / "versions"
    found = set()
    if vdir.exists():
        for d in vdir.iterdir():
            if d.is_dir() and (d / "index.html").exists():
                found.add(d.name.lstrip("v"))
    found.add(current)

    def key(v):
        return tuple(int(x) if x.isdigit() else 0 for x in v.split("."))
    return sorted(found, key=key, reverse=True)


def main():
    tpl = (ROOT / "template.html").read_text()
    ver, date = version_info()
    panels, tabs, notetabs = [], [], []
    for key, title, fn, group in DOCS:
        body = convert((ROOT / "content" / fn).read_text())
        panels.append(f'<article class="doc" id="doc-{key}" data-doc="{key}" hidden>{body}</article>')
        t = f'<button class="tab" type="button" data-doc="{key}" role="tab" aria-selected="false">{html.escape(title)}</button>'
        (notetabs if group == "note" else tabs).append(t)

    vlist = versions_list(ver)
    vitems = []
    for v in vlist:
        label = f"v{v}" + (" (current)" if v == ver else "")
        href = "./" if v == ver else f"versions/v{v}/"
        vitems.append(f'<li><a href="{href}">{label}</a></li>')
    versions_html = "".join(vitems)

    page = (tpl.replace("<!--TABS-->", "\n".join(tabs))
               .replace("<!--NOTETABS-->", "\n".join(notetabs))
               .replace("<!--PANELS-->", "\n".join(panels))
               .replace("<!--VERSIONS-->", versions_html)
               .replace("{{VERSION}}", html.escape(ver))
               .replace("{{DATE}}", html.escape(date)))
    (SITE / "index.html").write_text(page)

    snap_dir = SITE / "versions" / f"v{ver}"
    snap_dir.mkdir(parents=True, exist_ok=True)
    snap = (page.replace('href="assets/', 'href="../../assets/')
                .replace('href="versions/', 'href="../../versions/')
                .replace('href="./"', 'href="../../"'))
    (snap_dir / "index.html").write_text(snap)
    print(f"wrote {SITE / 'index.html'} ({len(page)} bytes) and {snap_dir / 'index.html'}; versions: {vlist}")


if __name__ == "__main__":
    main()
