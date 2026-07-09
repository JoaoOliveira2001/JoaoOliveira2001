#!/usr/bin/env python3
"""Generate customized neofetch-style profile SVGs."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASCII_LINES = (ROOT / "assets" / "ascii_lines.txt").read_text().splitlines()


def ascii_block(fill: str) -> str:
    lines = []
    y = 30
    for line in ASCII_LINES:
        escaped = (
            line.replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;')
        )
        lines.append(f'<tspan x="15" y="{y}">{escaped}</tspan>')
        y += 20
    return '\n'.join(lines)


def info_block(theme: str) -> str:
    rows = []
    y = 30
    rows.append(f'<tspan x="390" y="{y}">joao@oliveira</tspan> -———————————————————————————————————————————-—-')
    y += 20
    rows.append(f'<tspan x="390" y="{y}" class="cc">. </tspan><tspan class="key">OS</tspan>:<tspan class="cc"> ........................ </tspan><tspan class="value">macOS, Linux</tspan>')
    y += 20
    rows.append(f'<tspan x="390" y="{y}" class="cc">. </tspan><tspan class="key">Uptime</tspan>:<tspan class="cc" id="age_data_dots"> ...................... </tspan><tspan class="value" id="age_data">24 years, 6 months, 26 days</tspan>')
    y += 20
    rows.append(f'<tspan x="390" y="{y}" class="cc">. </tspan><tspan class="key">Host</tspan>:<tspan class="cc"> ............................. </tspan><tspan class="value">@whitewall-clients</tspan>')
    y += 20
    rows.append(f'<tspan x="390" y="{y}" class="cc">. </tspan><tspan class="key">Kernel</tspan>:<tspan class="cc"> .............................. </tspan><tspan class="value">Dev Pleno</tspan>')
    y += 20
    rows.append(f'<tspan x="390" y="{y}" class="cc">. </tspan><tspan class="key">IDE</tspan>:<tspan class="cc"> ........................... </tspan><tspan class="value">Cursor, VS Code</tspan>')
    y += 40
    rows.append(f'<tspan x="390" y="{y}" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Programming</tspan>:<tspan class="cc"> </tspan><tspan class="value">JavaScript, TypeScript, Python, Node.js</tspan>')
    y += 20
    rows.append(f'<tspan x="390" y="{y}" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Computer</tspan>:<tspan class="cc"> ......... </tspan><tspan class="value">HTML, CSS, SQL, YAML</tspan>')
    y += 20
    rows.append(f'<tspan x="390" y="{y}" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Real</tspan>:<tspan class="cc"> ......................... </tspan><tspan class="value">Português, English</tspan>')
    y += 40
    rows.append(f'<tspan x="390" y="{y}" class="cc">. </tspan><tspan class="key">Hobbies</tspan>.<tspan class="key">Software</tspan>:<tspan class="cc"> .... </tspan><tspan class="value">Automação n8n, APIs, React</tspan>')
    y += 20
    rows.append(f'<tspan x="390" y="{y}" class="cc">. </tspan><tspan class="key">Hobbies</tspan>.<tspan class="key">Hardware</tspan>:<tspan class="cc"> ............. </tspan><tspan class="value">Side projects</tspan>')
    y += 40
    rows.append(f'<tspan x="390" y="{y}">- Contact</tspan> -——————————————————————————————————————————————-—-')
    y += 20
    rows.append(f'<tspan x="390" y="{y}" class="cc">. </tspan><tspan class="key">LinkedIn</tspan>:<tspan class="cc"> ............................... </tspan><tspan class="value">joao-oliveira-618056215</tspan>')
    y += 20
    rows.append(f'<tspan x="390" y="{y}" class="cc">. </tspan><tspan class="key">WhatsApp</tspan>:<tspan class="cc"> ............................... </tspan><tspan class="value">+55 11 99883-6070</tspan>')
    y += 20
    rows.append(f'<tspan x="390" y="{y}" class="cc">. </tspan><tspan class="key">GitHub</tspan>:<tspan class="cc"> .................................. </tspan><tspan class="value">JoaoOliveira2001</tspan>')
    y += 40
    rows.append(f'<tspan x="390" y="{y}">- GitHub Stats</tspan> -—————————————————————————————————————————-—-')
    y += 20
    rows.append(
        f'<tspan x="390" y="{y}" class="cc">. </tspan><tspan class="key">Repos</tspan>:<tspan class="cc" id="repo_data_dots"> .... </tspan>'
        f'<tspan class="value" id="repo_data">14</tspan> {{<tspan class="key">Contributed</tspan>: <tspan class="value" id="contrib_data">14</tspan>}} | '
        f'<tspan class="key">Stars</tspan>:<tspan class="cc" id="star_data_dots"> ........... </tspan><tspan class="value" id="star_data">1</tspan>'
    )
    y += 20
    rows.append(
        f'<tspan x="390" y="{y}" class="cc">. </tspan><tspan class="key">Commmits</tspan>:<tspan class="cc" id="commit_data_dots"> ................. </tspan>'
        f'<tspan class="value" id="commit_data">0</tspan> | <tspan class="key">Followers</tspan>:<tspan class="cc" id="follower_data_dots"> ....... </tspan>'
        f'<tspan class="value" id="follower_data">0</tspan>'
    )
    y += 20
    rows.append(
        f'<tspan x="390" y="{y}" class="cc">. </tspan><tspan class="key">Lines of Code on GitHub</tspan>:<tspan class="cc" id="loc_data_dots">. </tspan>'
        f'<tspan class="value" id="loc_data">0</tspan> ( <tspan class="addColor" id="loc_add">0</tspan><tspan class="addColor">++</tspan>, '
        f'<tspan id="loc_del_dots"> </tspan><tspan class="delColor" id="loc_del">0</tspan><tspan class="delColor">--</tspan> )'
    )
    return '\n'.join(rows)


def build_svg(theme: str) -> str:
    if theme == 'dark':
        bg = '#161b22'
        text = '#c9d1d9'
        key = '#ffa657'
        value = '#a5d6ff'
        add = '#3fb950'
        delete = '#f85149'
        cc = '#616e7f'
    else:
        bg = '#f6f8fa'
        text = '#24292f'
        key = '#953800'
        value = '#0a3069'
        add = '#1a7f37'
        delete = '#cf222e'
        cc = '#c2cfde'

    return f'''<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="ConsolasFallback,Consolas,monospace" width="985px" height="530px" font-size="16px">
<style>
@font-face {{
src: local('Consolas'), local('Consolas Bold');
font-family: 'ConsolasFallback';
font-display: swap;
-webkit-size-adjust: 109%;
size-adjust: 109%;
}}
.key {{fill: {key};}}
.value {{fill: {value};}}
.addColor {{fill: {add};}}
.delColor {{fill: {delete};}}
.cc {{fill: {cc};}}
text, tspan {{white-space: pre;}}
</style>
<rect width="985px" height="530px" fill="{bg}" rx="15"/>
<text x="15" y="30" fill="{text}" class="ascii">
{ascii_block(text)}
</text>
<text x="390" y="30" fill="{text}">
{info_block(theme)}
</text>
</svg>
'''


def main() -> None:
    (ROOT / 'dark_mode.svg').write_text(build_svg('dark'))
    (ROOT / 'light_mode.svg').write_text(build_svg('light'))
    print('Wrote dark_mode.svg and light_mode.svg')


if __name__ == '__main__':
    main()
