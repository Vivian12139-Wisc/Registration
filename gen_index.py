import os

HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

  :root {{
    --bg: #f2f2f7;
    --card: #ffffff;
    --card2: #f9f9fb;
    --text: #1c1c1e;
    --sub: #6e6e73;
    --accent: #0071e3;
    --accent-bg: #e8f1fd;
    --folder-icon: #ff9f0a;
    --file-icon: #30b0c7;
    --border: rgba(0,0,0,0.06);
    --shadow: 0 2px 16px rgba(0,0,0,0.08), 0 0 0 0.5px rgba(0,0,0,0.04);
    --shadow-hover: 0 8px 32px rgba(0,0,0,0.13), 0 0 0 0.5px rgba(0,0,0,0.06);
    --radius: 18px;
    --radius-sm: 10px;
    --font: -apple-system, 'SF Pro Display', 'Helvetica Neue', sans-serif;
    --mono: 'SF Mono', 'Fira Code', ui-monospace, monospace;
  }}

  @media (prefers-color-scheme: dark) {{
    :root {{
      --bg: #1c1c1e;
      --card: #2c2c2e;
      --card2: #3a3a3c;
      --text: #f5f5f7;
      --sub: #98989d;
      --accent: #2997ff;
      --accent-bg: #1a2a3d;
      --border: rgba(255,255,255,0.08);
      --shadow: 0 2px 16px rgba(0,0,0,0.4), 0 0 0 0.5px rgba(255,255,255,0.04);
      --shadow-hover: 0 8px 32px rgba(0,0,0,0.5), 0 0 0 0.5px rgba(255,255,255,0.06);
    }}
  }}

  body {{
    background: var(--bg);
    color: var(--text);
    font-family: var(--font);
    min-height: 100vh;
    padding: 2.5rem 1.25rem 4rem;
    -webkit-font-smoothing: antialiased;
  }}

  .wrap {{ max-width: 760px; margin: 0 auto; }}

  /* ── 面包屑 ── */
  .crumbs {{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 4px 2px;
    font-size: 13px;
    color: var(--sub);
    margin-bottom: 2rem;
    font-family: var(--mono);
  }}
  .crumbs a {{ color: var(--accent); text-decoration: none; padding: 2px 6px; border-radius: 6px; transition: background .15s; }}
  .crumbs a:hover {{ background: var(--accent-bg); }}
  .crumbs .sep {{ color: var(--border); user-select: none; padding: 0 1px; }}
  .crumbs .now {{ color: var(--sub); padding: 2px 6px; }}

  /* ── 标题 ── */
  .page-title {{
    font-size: clamp(1.6rem, 4vw, 2.2rem);
    font-weight: 700;
    letter-spacing: -0.03em;
    color: var(--text);
    margin-bottom: 2rem;
    line-height: 1.15;
  }}
  .page-title small {{
    display: block;
    font-size: 0.9rem;
    font-weight: 400;
    color: var(--sub);
    letter-spacing: 0;
    margin-top: 4px;
  }}

  /* ── Section 标题 ── */
  .section-hd {{
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--sub);
    margin: 0 4px 10px;
  }}

  /* ── 文件夹卡片网格 ── */
  .folder-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 14px;
    margin-bottom: 2rem;
  }}
  .folder-card {{
    background: var(--card);
    border-radius: var(--radius);
    box-shadow: var(--shadow);
    padding: 1.2rem 1.2rem 1rem;
    text-decoration: none;
    color: var(--text);
    display: flex;
    flex-direction: column;
    gap: 10px;
    transition: box-shadow .2s, transform .2s;
    cursor: pointer;
  }}
  .folder-card:hover {{
    box-shadow: var(--shadow-hover);
    transform: translateY(-2px);
  }}
  .folder-card:active {{ transform: translateY(0); }}
  .folder-icon {{
    width: 44px; height: 44px;
    background: linear-gradient(145deg, #ffbe42, var(--folder-icon));
    border-radius: 11px;
    display: flex; align-items: center; justify-content: center;
    font-size: 22px;
    box-shadow: 0 2px 8px rgba(255,159,10,.3);
    flex-shrink: 0;
  }}
  .folder-name {{
    font-size: 15px;
    font-weight: 600;
    line-height: 1.3;
    word-break: break-all;
  }}
  .folder-arrow {{
    font-size: 12px;
    color: var(--sub);
    align-self: flex-end;
    margin-top: auto;
  }}

  /* ── 文件列表卡片 ── */
  .file-card {{
    background: var(--card);
    border-radius: var(--radius);
    box-shadow: var(--shadow);
    overflow: hidden;
    margin-bottom: 2rem;
  }}
  .file-row {{
    display: flex;
    align-items: center;
    gap: 12px;
    padding: .85rem 1.2rem;
    text-decoration: none;
    color: var(--text);
    border-bottom: 0.5px solid var(--border);
    transition: background .15s;
  }}
  .file-row:last-child {{ border-bottom: none; }}
  .file-row:hover {{ background: var(--card2); }}
  .file-icon-wrap {{
    width: 34px; height: 34px;
    background: linear-gradient(145deg, #5ad4e6, var(--file-icon));
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 17px;
    flex-shrink: 0;
    box-shadow: 0 2px 6px rgba(48,176,199,.25);
  }}
  .file-name {{
    flex: 1;
    font-size: 14px;
    font-weight: 500;
  }}
  .file-arrow {{ font-size: 12px; color: var(--sub); }}

  /* ── 空状态 ── */
  .empty-state {{
    text-align: center;
    padding: 3rem 1rem;
    background: var(--card);
    border-radius: var(--radius);
    box-shadow: var(--shadow);
    color: var(--sub);
    font-size: 14px;
  }}
  .empty-state .emoji {{ font-size: 2.5rem; margin-bottom: .75rem; }}

  footer {{
    text-align: center;
    font-size: 11px;
    color: var(--sub);
    margin-top: 3rem;
    opacity: .6;
    font-family: var(--mono);
  }}
</style>
</head>
<body>
<div class="wrap">
  <nav class="crumbs">{breadcrumb}</nav>
  <div class="page-title">{title}<small>{subtitle}</small></div>
  {body}
  <footer>gen_index.py</footer>
</div>
</body>
</html>
"""

def build_breadcrumb(rel_dir: str) -> str:
    root_a = '<a href="{depth}index.html">🏠 根目录</a>'
    sep = ' <span class="sep">/</span> '

    if rel_dir == ".":
        return root_a.format(depth="") + sep + '<span class="now">根目录</span>'

    parts = rel_dir.replace("\\", "/").split("/")
    depth = len(parts)
    crumbs = [root_a.format(depth="../" * depth)]

    for i, part in enumerate(parts[:-1]):
        back = "../" * (depth - i - 1)
        crumbs.append(f'<a href="{back}index.html">{part}</a>')

    crumbs.append(f'<span class="now">{parts[-1]}</span>')
    return sep.join(crumbs)


def build_body(dirpath: str, rel_dir: str) -> str:
    try:
        items = sorted(os.listdir(dirpath), key=lambda x: x.lower())
    except PermissionError:
        return '<div class="empty-state"><div class="emoji">🔒</div>无权限访问此目录</div>'

    subdirs = [i for i in items
               if os.path.isdir(os.path.join(dirpath, i)) and not i.startswith(".")]
    files   = [i for i in items
               if i.endswith(".html") and i != "index.html"]

    parts = []

    # ── 文件夹网格 ──
    if subdirs:
        cards = "\n".join(
            f'<a href="{d}/index.html" class="folder-card">'
            f'  <div class="folder-icon">📁</div>'
            f'  <div class="folder-name">{d}</div>'
            f'  <div class="folder-arrow">打开 ›</div>'
            f'</a>'
            for d in subdirs
        )
        parts.append(
            f'<p class="section-hd">文件夹</p>'
            f'<div class="folder-grid">{cards}</div>'
        )

    # ── 文件列表 ──
    if files:
        rows = "\n".join(
            f'<a href="{f}" class="file-row">'
            f'  <div class="file-icon-wrap">📄</div>'
            f'  <span class="file-name">{f}</span>'
            f'  <span class="file-arrow">↗</span>'
            f'</a>'
            for f in files
        )
        parts.append(
            f'<p class="section-hd">文档</p>'
            f'<div class="file-card">{rows}</div>'
        )

    if not subdirs and not files:
        parts.append('<div class="empty-state"><div class="emoji">📭</div>此目录下暂无内容</div>')

    return "\n\n".join(parts)


def gen_index_for_dir(dirpath: str, root: str = ".") -> None:
    rel_dir = os.path.relpath(dirpath, root)
    is_root = (rel_dir == ".")

    name = "易面" if is_root else os.path.basename(dirpath)

    # 统计当前目录内容数量作为副标题
    try:
        children = [i for i in os.listdir(dirpath) if not i.startswith(".")]
        subdirs  = sum(1 for i in children if os.path.isdir(os.path.join(dirpath, i)))
        files    = sum(1 for i in children if i.endswith(".html") and i != "index.html")
        if subdirs and files:
            subtitle = f"{subdirs} 个文件夹 · {files} 个文档"
        elif subdirs:
            subtitle = f"{subdirs} 个文件夹"
        elif files:
            subtitle = f"{files} 个文档"
        else:
            subtitle = "空目录"
    except Exception:
        subtitle = ""

    html = HTML_TEMPLATE.format(
        title=name,
        subtitle=subtitle,
        breadcrumb=build_breadcrumb(rel_dir),
        body=build_body(dirpath, rel_dir),
    )

    out = os.path.join(dirpath, "index.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✔  {out}")


def main(root: str = ".") -> None:
    count = 0
    for dirpath, dirs, _ in os.walk(root):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        gen_index_for_dir(dirpath, root)
        count += 1
    print(f"\n完成！共生成 {count} 个 index.html")


if __name__ == "__main__":
    main()
