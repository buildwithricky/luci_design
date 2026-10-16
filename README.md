# Luci design tokens

Three-layer tokens (primitive → semantic → component) with first-class light and dark themes,
built from the approved Luci palette: Forest #242a20, Sage #8fa581, and greys #141414, #4c4c4c,
#848483, #bbbcbb, #f3f4f2. Values marked `proposed` are extensions awaiting approval.

## Use

```html
<head>
  <meta name="theme-color" content="#f3f4f2">
  <script>/* paste js/theme-init.js here, inline, before the stylesheet */</script>
  <link rel="stylesheet" href="/tokens/css/index.css">
</head>
```

```js
import { setTheme } from '/tokens/js/theme.js';
setTheme('dark'); // 'light' | 'dark' | 'system'
```

Components read semantic (`--color-text-muted`) or component (`--button-primary-background`)
variables only, never primitives (`--green-900`).

## Change a value

1. Edit `build/tokens_source.py` (the single source of truth).
2. Run `python3 build/build.py`. It regenerates `css/`, `json/`, `token-inventory.csv`,
   `contrast-audit.csv` and `examples/preview.html`, and prints any contrast failure.
3. Commit only when it prints `fails: 0`, after checking `examples/preview.html` in both themes.

## Files

| Path | Contents |
| --- | --- |
| `build/tokens_source.py` | Every token, with descriptions and approval status |
| `build/build.py` | Generator and WCAG contrast audit |
| `css/primitives.css` | Layer 1 colours |
| `css/foundation.css` | Type, spacing, radius, borders, opacity, motion, layout; type/space/motion roles; reduced motion |
| `css/semantic.css` | Layer 2, light and dark |
| `css/components.css` | Layer 3 |
| `css/index.css` | Imports all four in order |
| `json/*.tokens.json` | W3C Design Tokens (DTCG) format, for Tokens Studio / Style Dictionary |
| `js/theme-init.js` | No-flash inline head script |
| `js/theme.js` | Runtime switching, persistence, OS and cross-tab sync |
| `examples/components.css` | Reference buttons, inputs, cards, nav, modal, badges, etc. using tokens only |
| `examples/preview.html` | Self-contained visual check of every component in both themes |

Full documentation: Luci Design System doc in Claude.
# luci_design
