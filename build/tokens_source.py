"""
Luci design tokens: the single source of truth.

Edit values HERE, then run `python3 build/build.py`.
Every CSS file, JSON file and the inventory CSV is generated from this file,
so the design layer and the code layer cannot drift apart.

Status flags on primitives:
  approved  = from the Luci palette image (do not change without sign-off)
  proposed  = extension derived from the approved colours, awaiting approval
"""

# ---------------------------------------------------------------------------
# LAYER 1: PRIMITIVES (raw values, no meaning attached)
# ---------------------------------------------------------------------------

COLOR = {
    # Brand greens
    "green.50":  ("#e9ece7", "proposed", "10% Sage over neutral.50"),
    "green.100": ("#dfe4db", "proposed", "20% Sage over neutral.50"),
    "green.200": ("#9eb192", "proposed", "Sage, 15% toward neutral.50"),
    "green.300": ("#8fa581", "approved", "Sage"),
    "green.400": ("#849977", "proposed", "Sage, 10% toward Forest"),
    "green.600": ("#5a6850", "proposed", "50/50 Forest and Sage"),
    "green.800": ("#31392c", "proposed", "Forest, 12% toward Sage"),
    "green.850": ("#2d312a", "proposed", "15% Sage over neutral.900"),
    "green.900": ("#242a20", "approved", "Forest"),
    "green.950": ("#1c1f1a", "proposed", "Forest, 50% toward neutral.950"),
    # Neutrals
    "neutral.0":   ("#fbfbfa", "proposed", "neutral.50 lifted, tint kept"),
    "neutral.50":  ("#f3f4f2", "approved", "Light canvas"),
    "neutral.100": ("#e7e8e5", "proposed", "neutral.50, 5% darker"),
    "neutral.300": ("#bbbcbb", "approved", "Light grey"),
    "neutral.400": ("#9a9a98", "proposed", "Between neutral.300 and neutral.500"),
    "neutral.500": ("#848483", "approved", "Mid grey"),
    "neutral.600": ("#656565", "proposed", "neutral.500, 55% toward neutral.700"),
    "neutral.700": ("#4c4c4c", "approved", "Dark grey"),
    "neutral.750": ("#3a3b39", "proposed", "Dark-mode border step"),
    "neutral.800": ("#2e2f2d", "proposed", "Dark overlay surface"),
    "neutral.850": ("#242523", "proposed", "Dark raised surface"),
    "neutral.900": ("#1c1d1b", "proposed", "Dark standard surface"),
    "neutral.950": ("#141414", "approved", "Near-black"),
    # Status (palette has none; all proposed)
    "success.light":      ("#2f6b3a", "proposed", "Success text/icon, light"),
    "success.tint-light": ("#e7ede7", "proposed", "Success tint, light"),
    "success.dark":       ("#8cc98a", "proposed", "Success text/icon, dark"),
    "success.tint-dark":  ("#2c352b", "proposed", "Success tint, dark"),
    "warning.light":      ("#8a5a00", "proposed", "Warning text/icon, light"),
    "warning.tint-light": ("#f0ebe1", "proposed", "Warning tint, light"),
    "warning.dark":       ("#e0b45a", "proposed", "Warning text/icon, dark"),
    "warning.tint-dark":  ("#373224", "proposed", "Warning tint, dark"),
    "danger.light":       ("#b3261e", "proposed", "Danger text/icon, light"),
    "danger.light-hover": ("#951f19", "proposed", "Danger button hover, light"),
    "danger.tint-light":  ("#f4e6e4", "proposed", "Danger tint, light"),
    "danger.dark":        ("#f2a39b", "proposed", "Danger text/icon, dark"),
    "danger.dark-hover":  ("#f6bcb6", "proposed", "Danger button hover, dark"),
    "danger.tint-dark":   ("#3a302d", "proposed", "Danger tint, dark"),
    "info.light":         ("#2f5f8a", "proposed", "Info text/icon, light"),
    "info.tint-light":    ("#e7ebef", "proposed", "Info tint, light"),
    "info.dark":          ("#9cc3e6", "proposed", "Info text/icon, dark"),
    "info.tint-dark":     ("#2e3437", "proposed", "Info tint, dark"),
    # Scrims (based on neutral.950, never pure black)
    "scrim.light": ("rgb(20 20 20 / 0.48)", "proposed", "neutral.950 at 48%"),
    "scrim.dark":  ("rgb(10 11 10 / 0.64)", "proposed", "neutral.950 darkened, at 64%"),
}

FONT = {
    "font.family.sans": "'Inter', ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif",
    "font.family.mono": "ui-monospace, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace",
    "font.weight.regular": "400",
    "font.weight.semibold": "600",
    "font.size.12": "0.75rem",
    "font.size.14": "0.875rem",
    "font.size.16": "1rem",
    "font.size.18": "1.125rem",
    "font.size.20": "1.25rem",
    "font.size.28": "1.75rem",
    "font.size.36": "2.25rem",
    "font.size.48": "3rem",
    "line-height.16": "1rem",
    "line-height.20": "1.25rem",
    "line-height.24": "1.5rem",
    "line-height.28": "1.75rem",
    "line-height.36": "2.25rem",
    "line-height.44": "2.75rem",
    "line-height.56": "3.5rem",
    "letter-spacing.tight": "-0.02em",
    "letter-spacing.snug": "-0.01em",
    "letter-spacing.normal": "0",
    "letter-spacing.wide": "0.01em",
}

SPACE = {f"space.{n}": f"{n/16:g}rem" if n else "0" for n in
         [0, 2, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96]}

RADIUS = {
    "radius.none": "0",
    "radius.sm": "4px",
    "radius.md": "8px",
    "radius.lg": "12px",
    "radius.xl": "16px",
    "radius.full": "9999px",
}

BORDER_WIDTH = {"border-width.1": "1px", "border-width.2": "2px"}

OPACITY = {"opacity.0": "0", "opacity.48": "0.48", "opacity.64": "0.64", "opacity.100": "1"}

DURATION = {
    "duration.instant": "100ms",
    "duration.fast": "150ms",
    "duration.base": "200ms",
    "duration.medium": "300ms",
    "duration.slow": "400ms",
    "duration.pulse": "600ms",
    "duration.shimmer": "1500ms",
}

EASING = {
    "easing.enter": "cubic-bezier(0.05, 0.7, 0.1, 1)",
    "easing.exit": "cubic-bezier(0.3, 0, 0.8, 0.15)",
    "easing.move": "cubic-bezier(0.2, 0, 0, 1)",
    "easing.linear": "linear",
}

LAYOUT = {
    "breakpoint.sm": "640px",
    "breakpoint.md": "768px",
    "breakpoint.lg": "1024px",
    "breakpoint.xl": "1280px",
    "size.sidebar": "240px",
    "size.content-max": "1120px",
    "size.header": "56px",
    "size.control-sm": "32px",
    "size.control-md": "40px",
    "size.control-lg": "48px",
    "z.base": "0",
    "z.sticky": "100",
    "z.dropdown": "200",
    "z.overlay": "300",
    "z.modal": "400",
    "z.spotlight": "450",
    "z.toast": "500",
    "z.tooltip": "600",
}

# ---------------------------------------------------------------------------
# LAYER 2: SEMANTIC TOKENS
# name: (light ref, dark ref, description, usage)
# A ref is a primitive name; a literal value is allowed only for shadows.
# ---------------------------------------------------------------------------

SEMANTIC_COLOR = {
    # Backgrounds
    "color.background.canvas": ("neutral.50", "neutral.950", "App and page background", "Only the outermost layer; never on cards"),
    "color.background.surface": ("neutral.0", "neutral.900", "Standard surface: cards, panels, sidebar", "Default container fill"),
    "color.background.surface-raised": ("neutral.0", "neutral.850", "Card that sits above another surface", "Pair with elevation.raised"),
    "color.background.surface-sunken": ("neutral.100", "neutral.950", "Wells inside a surface: code, input groups, filter bars", "Never for clickable items"),
    "color.background.surface-overlay": ("neutral.0", "neutral.800", "Menus, popovers, modals, drawers", "Pair with elevation.overlay or elevation.modal"),
    "color.background.surface-inverse": ("green.900", "neutral.50", "Tooltips and toasts", "Text on it uses color.text.inverse"),
    "color.background.hover": ("neutral.100", "neutral.800", "Hover fill for rows, menu items, ghost buttons", "Never for selection"),
    "color.background.selected": ("green.50", "green.850", "Selected rows, chips, nav items", "Always pair with a non-colour cue (check, bar, weight)"),
    "color.background.scrim": ("scrim.light", "scrim.dark", "Dims the page behind modals and onboarding spotlight", "One scrim at a time"),
    # Text
    "color.text.primary": ("neutral.950", "neutral.50", "Headings and body text", "Default text colour"),
    "color.text.secondary": ("neutral.700", "neutral.300", "Supporting text, labels, metadata", "Never for the only copy of an instruction"),
    "color.text.muted": ("neutral.600", "neutral.400", "Placeholder, helper text, timestamps", "Passes 4.5:1 on every surface in its theme"),
    "color.text.disabled": ("neutral.500", "neutral.600", "Disabled controls only", "Exempt from contrast rules; never for live content"),
    "color.text.inverse": ("neutral.50", "neutral.950", "Text on surface-inverse", "Tooltips, toasts"),
    "color.text.link": ("green.600", "green.300", "Inline links", "Always underlined in body copy"),
    "color.text.selected": ("green.900", "neutral.50", "Text on color.background.selected", "Pair with weight 600"),
    # Icons
    "color.icon.default": ("neutral.700", "neutral.300", "Interface icons", "Meaningful icons meet 3:1"),
    "color.icon.strong": ("neutral.950", "neutral.50", "Icons that carry the only label", "Icon-only buttons"),
    # Borders
    "color.border.subtle": ("neutral.100", "neutral.800", "Dividers between rows and sections", "Decorative; no contrast minimum"),
    "color.border.default": ("neutral.300", "neutral.750", "Card and panel outlines", "Decorative; pair with a fill change"),
    "color.border.strong": ("neutral.500", "neutral.500", "Input and control boundaries", "Meets 3:1 against its surface"),
    "color.border.hover": ("neutral.700", "neutral.400", "Control boundary on hover", "Inputs and outlined buttons"),
    "color.border.selected": ("green.600", "green.300", "Selected card or option outline", "Use 2px width"),
    "color.focus.ring": ("green.600", "green.300", "Keyboard focus indicator", "2px ring, 2px offset in the canvas colour"),
    # Actions
    "color.action.primary.background": ("green.900", "green.300", "Primary button fill", "One per view"),
    "color.action.primary.foreground": ("neutral.50", "green.900", "Text and icon on primary", ""),
    "color.action.primary.hover": ("green.800", "green.200", "Primary hover fill", ""),
    "color.action.primary.pressed": ("green.950", "green.400", "Primary pressed fill", ""),
    "color.action.tonal.background": ("green.50", "green.850", "Brand-tinted secondary action", "Second most important action"),
    "color.action.tonal.foreground": ("green.900", "green.200", "Text on tonal", ""),
    "color.action.tonal.hover": ("green.100", "green.800", "Tonal hover fill", ""),
    "color.action.danger.background": ("danger.light", "danger.dark", "Destructive button fill", "Confirmations only"),
    "color.action.danger.foreground": ("neutral.0", "neutral.950", "Text on danger", ""),
    "color.action.danger.hover": ("danger.light-hover", "danger.dark-hover", "Danger hover fill", ""),
    "color.action.disabled.background": ("neutral.100", "neutral.800", "Disabled control fill", ""),
    "color.accent.background": ("green.300", "green.300", "Sage brand fill: 'New' badges, onboarding step numbers, celebration marks", "Always carries color.accent.foreground text or icon"),
    "color.accent.foreground": ("green.900", "green.900", "Text and icons on the Sage fill", "5.5:1 in both themes"),
    "color.accent.indicator": ("green.600", "green.300", "Standalone brand marks that must be seen: active dots, progress, onboarding outline", "Meets 3:1 in both themes"),
    # Status
    "color.status.success.foreground": ("success.light", "success.dark", "Success text and icon", "Pair with a check icon and a word"),
    "color.status.success.background": ("success.tint-light", "success.tint-dark", "Success banner and badge fill", ""),
    "color.status.warning.foreground": ("warning.light", "warning.dark", "Warning text and icon", "Pair with a warning icon and a word"),
    "color.status.warning.background": ("warning.tint-light", "warning.tint-dark", "Warning banner and badge fill", ""),
    "color.status.danger.foreground": ("danger.light", "danger.dark", "Error text, icon and invalid-field border", "Pair with an error icon and a message"),
    "color.status.danger.background": ("danger.tint-light", "danger.tint-dark", "Error banner and badge fill", ""),
    "color.status.info.foreground": ("info.light", "info.dark", "Information text and icon", "Pair with an info icon"),
    "color.status.info.background": ("info.tint-light", "info.tint-dark", "Info banner and badge fill", ""),
    # Data visualisation (ordered; series 1 is the brand)
    "color.chart.series-1": ("green.600", "green.300", "First data series", "Brand series"),
    "color.chart.series-2": ("info.light", "info.dark", "Second data series", ""),
    "color.chart.series-3": ("warning.light", "warning.dark", "Third data series", ""),
    "color.chart.series-4": ("neutral.500", "neutral.300", "Fourth series or 'other'", ""),
    "color.chart.grid": ("neutral.100", "neutral.800", "Gridlines", "Decorative"),
    "color.chart.axis": ("neutral.500", "neutral.500", "Axis lines and ticks", ""),
}

SEMANTIC_OTHER = {
    # Elevation: values differ by theme. Dark relies on tone + border, shadow only for overlays.
    "elevation.raised": (
        "0 1px 2px rgb(20 20 20 / 0.06), 0 1px 1px rgb(20 20 20 / 0.04)",
        "none",
        "Raised cards", "Light: soft shadow. Dark: tone step + border instead"),
    "elevation.overlay": (
        "0 4px 12px rgb(20 20 20 / 0.10), 0 1px 2px rgb(20 20 20 / 0.06)",
        "0 8px 24px rgb(10 11 10 / 0.48)",
        "Menus, popovers, tooltips", "Always with color.border.default"),
    "elevation.modal": (
        "0 16px 40px rgb(20 20 20 / 0.16), 0 2px 6px rgb(20 20 20 / 0.06)",
        "0 20px 48px rgb(10 11 10 / 0.64)",
        "Modals and drawers", "Paired with the scrim"),
}

# Theme-independent semantic aliases (typography roles, spacing roles, motion roles)
TYPE_ROLES = {
    # role: (size, line-height, weight, letter-spacing, family, usage)
    "display-lg": ("font.size.48", "line-height.56", "font.weight.semibold", "letter-spacing.tight", "font.family.sans", "Marketing hero headline"),
    "display-md": ("font.size.36", "line-height.44", "font.weight.semibold", "letter-spacing.tight", "font.family.sans", "Marketing section headline"),
    "title-page": ("font.size.28", "line-height.36", "font.weight.semibold", "letter-spacing.snug", "font.family.sans", "App page title, one per page"),
    "title-section": ("font.size.20", "line-height.28", "font.weight.semibold", "letter-spacing.snug", "font.family.sans", "Section heading"),
    "title-card": ("font.size.16", "line-height.24", "font.weight.semibold", "letter-spacing.normal", "font.family.sans", "Card and dialog title"),
    "body-lg": ("font.size.18", "line-height.28", "font.weight.regular", "letter-spacing.normal", "font.family.sans", "Marketing body copy"),
    "body-md": ("font.size.16", "line-height.24", "font.weight.regular", "letter-spacing.normal", "font.family.sans", "Default body, all mobile text"),
    "body-sm": ("font.size.14", "line-height.20", "font.weight.regular", "letter-spacing.normal", "font.family.sans", "Dense desktop views, secondary text"),
    "label": ("font.size.14", "line-height.20", "font.weight.semibold", "letter-spacing.normal", "font.family.sans", "Buttons, nav items, form labels"),
    "caption": ("font.size.12", "line-height.16", "font.weight.regular", "letter-spacing.wide", "font.family.sans", "Captions, badges, helper text"),
    "mono": ("font.size.14", "line-height.20", "font.weight.regular", "letter-spacing.normal", "font.family.mono", "IDs, amounts in tables, code"),
}

SPACE_ROLES = {
    "space.inline.xs": ("space.4", "Icon to label"),
    "space.inline.sm": ("space.8", "Between buttons, chips"),
    "space.inline.md": ("space.12", "Control padding, horizontal"),
    "space.stack.xs": ("space.4", "Label to input"),
    "space.stack.sm": ("space.8", "Related lines"),
    "space.stack.md": ("space.16", "Form fields, list groups"),
    "space.stack.lg": ("space.24", "Between cards"),
    "space.section": ("space.48", "Between app page sections"),
    "space.section-marketing": ("space.96", "Between marketing sections (64 on mobile)"),
    "space.inset.card": ("space.16", "Card padding on mobile (24 from md up)"),
    "space.inset.card-lg": ("space.24", "Card padding from md up"),
    "space.gutter": ("space.16", "Page side gutter on mobile (32 from lg up)"),
    "space.gutter-lg": ("space.32", "Page side gutter from lg up"),
}

MOTION_ROLES = {
    # role: (duration, easing, usage, constraint)
    "motion.feedback": ("duration.instant", "easing.move", "Button press, toggle, chip select", "Never delayed"),
    "motion.hover": ("duration.fast", "easing.move", "Hover fills, focus ring appearance", "Colour and opacity only"),
    "motion.tooltip": ("duration.fast", "easing.enter", "Tooltip fade in", "300ms hover delay; instant on focus"),
    "motion.popover-enter": ("duration.base", "easing.enter", "Dropdowns, popovers, toasts appearing", "Max 4px travel"),
    "motion.popover-exit": ("duration.fast", "easing.exit", "Dropdowns and popovers closing", ""),
    "motion.modal-enter": ("duration.medium", "easing.enter", "Modal and drawer opening", "Scale from 0.96 or slide from edge"),
    "motion.modal-exit": ("duration.base", "easing.exit", "Modal and drawer closing", ""),
    "motion.route": ("duration.base", "easing.move", "Page cross-fade with 8px rise", "Sidebar and header never animate"),
    "motion.step": ("duration.medium", "easing.enter", "Onboarding step slide (24px)", "Back reverses direction"),
    "motion.emphasis": ("duration.slow", "easing.enter", "Completion check draw", "One per flow"),
    "motion.spotlight": ("duration.pulse", "easing.move", "Onboarding outline pulse", "Runs twice, then stops"),
    "motion.skeleton": ("duration.shimmer", "easing.linear", "Skeleton shimmer loop", "Only if load exceeds 300ms; static under reduced motion"),
    "motion.progress": ("duration.base", "easing.linear", "Progress bar width updates", ""),
}

# ---------------------------------------------------------------------------
# LAYER 3: COMPONENT TOKENS (only where they add control)
# name: (semantic or primitive ref, usage)
# ---------------------------------------------------------------------------

COMPONENT = {
    # Button
    "button.radius": ("radius.md", "All buttons"),
    "button.height.sm": ("size.control-sm", "Dense tables, toolbars"),
    "button.height.md": ("size.control-md", "Default on desktop"),
    "button.height.lg": ("size.control-lg", "Default on mobile; touch target"),
    "button.primary.background": ("color.action.primary.background", ""),
    "button.primary.foreground": ("color.action.primary.foreground", ""),
    "button.primary.hover": ("color.action.primary.hover", ""),
    "button.primary.pressed": ("color.action.primary.pressed", ""),
    "button.secondary.background": ("color.background.surface", "Outlined neutral button"),
    "button.secondary.foreground": ("color.text.primary", ""),
    "button.secondary.border": ("color.border.strong", ""),
    "button.secondary.hover": ("color.background.hover", ""),
    "button.ghost.hover": ("color.background.hover", "Icon buttons, toolbar actions"),
    # Input
    "input.background": ("color.background.surface", "Text fields, text areas, selects"),
    "input.foreground": ("color.text.primary", ""),
    "input.placeholder": ("color.text.muted", ""),
    "input.border": ("color.border.strong", ""),
    "input.border.hover": ("color.border.hover", ""),
    "input.border.focus": ("color.focus.ring", "Plus the focus ring"),
    "input.border.error": ("color.status.danger.foreground", "Plus an icon and message"),
    "input.background.disabled": ("color.action.disabled.background", ""),
    "input.radius": ("radius.md", ""),
    "input.height": ("size.control-md", "Use size.control-lg on mobile"),
    # Card
    "card.background": ("color.background.surface", ""),
    "card.border": ("color.border.default", ""),
    "card.radius": ("radius.lg", ""),
    "card.shadow": ("elevation.raised", ""),
    # Navigation
    "sidebar.background": ("color.background.surface", "Quieter than content via border, not colour"),
    "sidebar.border": ("color.border.subtle", ""),
    "sidebar.item.hover": ("color.background.hover", ""),
    "sidebar.item.active.background": ("color.background.selected", "Plus 2px left bar"),
    "sidebar.item.active.foreground": ("color.text.selected", "Plus weight 600"),
    "sidebar.item.active.indicator": ("color.border.selected", "2px left bar"),
    "tabs.foreground": ("color.text.secondary", ""),
    "tabs.foreground.active": ("color.text.primary", ""),
    "tabs.indicator": ("color.border.selected", "2px underline"),
    # Overlays
    "popover.background": ("color.background.surface-overlay", "Menus, dropdowns, popovers"),
    "popover.border": ("color.border.default", ""),
    "popover.shadow": ("elevation.overlay", ""),
    "popover.radius": ("radius.lg", ""),
    "tooltip.background": ("color.background.surface-inverse", ""),
    "tooltip.foreground": ("color.text.inverse", ""),
    "tooltip.radius": ("radius.sm", ""),
    "modal.background": ("color.background.surface-overlay", "Modals and drawers"),
    "modal.shadow": ("elevation.modal", ""),
    "modal.radius": ("radius.xl", "Drawers use 0 on the attached edge"),
    "modal.scrim": ("color.background.scrim", ""),
    # Table
    "table.header.background": ("color.background.surface-sunken", ""),
    "table.row.border": ("color.border.subtle", ""),
    "table.row.hover": ("color.background.hover", ""),
    "table.row.selected": ("color.background.selected", "Plus a checked checkbox"),
    # Toast
    "toast.background": ("color.background.surface-inverse", ""),
    "toast.foreground": ("color.text.inverse", ""),
    # Onboarding
    "onboarding.spotlight.scrim": ("color.background.scrim", ""),
    "onboarding.spotlight.ring": ("color.focus.ring", "Same as focus, so guidance and focus read alike"),
    "onboarding.tip.background": ("color.background.surface-overlay", ""),
    "onboarding.tip.border": ("color.border.selected", ""),
    "progress.track": ("color.background.surface-sunken", ""),
    "progress.fill": ("color.action.primary.background", "Forest in light, Sage in dark"),
    # Loading and empty
    "skeleton.base": ("color.background.hover", ""),
    "skeleton.highlight": ("color.background.surface", "Moving band"),
    "empty-state.icon.background": ("color.background.selected", ""),
    "empty-state.icon.foreground": ("color.text.link", ""),
}
