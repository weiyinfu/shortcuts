import parser

a, columns = parser.get_data()
all_keys = set()
for i in a:
    for cmd in i:
        all_keys.add(cmd)
ma = {}
ide = {}
for i in all_keys:
    now = []
    for file, filename in zip(a, columns):
        if i in file and file[i].strip():
            now.append(f"**{filename}** : {file[i]} ")
    if len(now) == 0:
        continue
    if len(now) == 1:
        for file, filename in zip(a, columns):
            if i in file:
                if filename not in ide:
                    ide[filename] = []
                ide[filename].append(f"**{i}** {file[i]}")
                break
        continue
    ma[i] = now

shortcuts = ma.items()
shortcuts = sorted(shortcuts, key=lambda x: (len(x[1]), x[0]), reverse=True)
lines = []
for cmd, short in shortcuts:
    if len(short) == 1:
        lines.append(f'{cmd} {short[0]}  \n')
    else:
        lines.append(f"## {cmd}")
        for sh in short:
            lines.append(f"* {sh}")
        lines[-1] += '\n\n'
lines.append("""

--------------------------

# 以下内容为各个IDE独有的快捷键

""")
for ide_name, ide_actions in ide.items():
    lines.append(f"## {ide_name} IDE独有的快捷键")
    for act in ide_actions:
        lines.append(f"* {act}\n")
    lines.append('\n')
open('doc/src/shortcut.md', 'w').write("\n".join(lines))
