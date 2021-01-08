
Resetting
=========

Sty uses ANSI SGR parameters to reset previously applied styles. More about ANSI Select Graphic Rendition (SGR) on wikipedia:
`ANSI SGR <https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_parameters>`__

.. _anchor_reset_register:

Sty's default reset register
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are the default attributes for the ``sty.rs`` register-object:

.. rst-class:: table-register

=================== ======================
Attribute           Default Renderer
=================== ======================
rs.all              sgr(0)
rs.fg               sgr(39)
rs.bg               sgr(49)
rs.bold_faint       sgr(22)
rs.faint_bold       sgr(22)
rs.italic (alias i) sgr(23)
rs.underl (alias u) sgr(24)
rs.blink            sgr(25)
rs.hidden           sgr(28)
rs.strike           sgr(29)
rs.ef               sgr(22), sgr(23), sgr(24), sgr(25), sgr(27), sgr(28), sgr(29)
=================== ======================

