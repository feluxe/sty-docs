
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
rs.all              sty.renderfunc.sgr(0)
rs.fg               sty.renderfunc.sgr(39)
rs.bg               sty.renderfunc.sgr(49)
rs.bold_faint       sty.renderfunc.sgr(22)
rs.faint_bold       sty.renderfunc.sgr(22)
rs.italic (alias i) sty.renderfunc.sgr(23)
rs.underl (alias u) sty.renderfunc.sgr(24)
rs.blink            sty.renderfunc.sgr(25)
rs.hidden           sty.renderfunc.sgr(28)
rs.strike           sty.renderfunc.sgr(29)
=================== ======================

