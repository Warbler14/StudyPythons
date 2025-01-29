import urwid

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    text.set_text(repr(key))

text = urwid.Text(u"Hello, Multiuser Mode! Press 'q' to exit.", align='center')
fill = urwid.Filler(text, valign='middle')

loop = urwid.MainLoop(fill, unhandled_input=exit_on_q)
loop.run()

# --------------------------
# pip install urwid

# https://github.com/nec4/gpu-array/tree/mac