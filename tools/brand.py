"""Frame Lab marka varlıkları: renkler, Kare maskotu ve FL monogram (SVG üretir)."""
INK="#111114"; PAPER="#F5F4F0"; LIME="#B8F24A"; VIOLET="#7B61FF"; SOFT="#EEF6DE"; GREY="#A9A9A2"; LIME_DARK="#5E9E00"; PINK="#FF2E93"
W="#FFFFFF"

def kare(size, face="mutlu", bg=INK, light_bg=False):
    """Kare maskotu. face: mutlu, goz, saskin, dusunen, fikir, calisiyor.
    bg: arka plan dairesi rengi ya da "none". light_bg=True açık zeminde ayağı koyu çizer."""
    faces = {
     "mutlu": f'<rect x="83" y="84" width="9" height="16" rx="4.5" fill="{W}"></rect><rect x="108" y="84" width="9" height="16" rx="4.5" fill="{W}"></rect><path d="M92 107 Q100 113 108 107" fill="none" stroke="{W}" stroke-width="3.5" stroke-linecap="round"></path>',
     "goz": f'<rect x="83" y="84" width="9" height="16" rx="4.5" fill="{W}"></rect><path d="M106 93 Q112.5 87 119 93" fill="none" stroke="{W}" stroke-width="3.5" stroke-linecap="round"></path><path d="M90 106 Q100 115 110 106" fill="none" stroke="{W}" stroke-width="3.5" stroke-linecap="round"></path>',
     "saskin": f'<circle cx="87" cy="91" r="7" fill="{W}"></circle><circle cx="113" cy="91" r="7" fill="{W}"></circle><circle cx="100" cy="110" r="4.5" fill="none" stroke="{W}" stroke-width="3"></circle>',
     "dusunen": f'<rect x="86" y="80" width="8" height="13" rx="4" fill="{W}"></rect><rect x="110" y="80" width="8" height="13" rx="4" fill="{W}"></rect><path d="M93 109 H107" fill="none" stroke="{W}" stroke-width="3.5" stroke-linecap="round"></path><circle cx="150" cy="44" r="4" fill="{VIOLET}"></circle><circle cx="162" cy="36" r="5" fill="{VIOLET}"></circle><circle cx="176" cy="26" r="6" fill="{VIOLET}"></circle>',
     "fikir": f'<path d="M81 94 Q87.5 86 94 94" fill="none" stroke="{W}" stroke-width="3.5" stroke-linecap="round"></path><path d="M106 94 Q112.5 86 119 94" fill="none" stroke="{W}" stroke-width="3.5" stroke-linecap="round"></path><path d="M88 104 H112 Q110 116 100 116 Q90 116 88 104 Z" fill="{W}"></path><circle cx="100" cy="35" r="15" fill="none" stroke="{LIME}" stroke-width="3" opacity="0.6"></circle>',
     "blink": f'<path d="M82 92 H93 M107 92 H118" stroke="{W}" stroke-width="4" stroke-linecap="round"></path><path d="M92 107 Q100 113 108 107" fill="none" stroke="{W}" stroke-width="3.5" stroke-linecap="round"></path>',
     "calisiyor": f'<rect x="76" y="92" width="48" height="8" rx="4" fill="none" stroke="{W}" stroke-width="2.5"></rect><rect x="78" y="94" width="28" height="4" rx="2" fill="{LIME}"></rect><circle cx="88" cy="110" r="2.5" fill="{W}"></circle><circle cx="100" cy="110" r="2.5" fill="{W}" opacity="0.6"></circle><circle cx="112" cy="110" r="2.5" fill="{W}" opacity="0.3"></circle>',
    }
    foot = INK if light_bg else PAPER
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 200 200" aria-hidden="true">
<circle cx="100" cy="100" r="100" fill="{bg}"></circle>
<line x1="100" y1="58" x2="100" y2="40" stroke="{LIME}" stroke-width="6" stroke-linecap="round"></line>
<circle cx="100" cy="35" r="8" fill="{VIOLET}"></circle>
<rect x="48" y="56" width="104" height="88" rx="24" fill="{LIME}"></rect>
<rect x="60" y="68" width="80" height="56" rx="13" fill="{INK}"></rect>
<path d="M68 82 V76 H74 M126 76 H132 V82 M132 110 V116 H126 M74 116 H68 V110" fill="none" stroke="{LIME}" stroke-width="3" stroke-linecap="round"></path>
{faces[face]}
<rect x="84" y="144" width="32" height="10" rx="5" fill="{LIME}"></rect>
<rect x="68" y="154" width="64" height="8" rx="4" fill="{foot}"></rect>
</svg>'''

def fl_monogram(size, bg=INK, fg=PAPER, accent=LIME):
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 200 200" aria-hidden="true">
<circle cx="100" cy="100" r="100" fill="{bg}"></circle>
<path d="M60 142 V60 H114 M60 100 H98" fill="none" stroke="{fg}" stroke-width="15" stroke-linecap="square"></path>
<path d="M126 80 V140 H156" fill="none" stroke="{fg}" stroke-width="15" stroke-linecap="square"></path>
<circle cx="146" cy="62" r="10" fill="{accent}"></circle></svg>'''
