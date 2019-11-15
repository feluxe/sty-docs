Coloring
========

Sty uses ANSI escape sequences for coloring. More about ANSI colors on wikipedia:
`3/4bit colors <https://en.wikipedia.org/wiki/ANSI_escape_code#3/4_bit>`__
| `8bit colors <https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit>`__
| `24bit colors <https://en.wikipedia.org/wiki/ANSI_escape_code#24-bit>`__.


.. _anchor_color_register:

Sty's default color register
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Colors that use the :code:`sgr()` renderer are most widely supported.


.. _anchor_fg_register:

Foreground
----------

.. rst-class:: table-color-fg

============= ========= ======== =======================================
Attribute     Ex. Light Ex. Dark          Default Renderer
============= ========= ======== =======================================
fg.li_black   Example   Example  sty.renderfunc.sgr(90)
fg.black      Example   Example  sty.renderfunc.sgr(30)
fg.da_black   Example   Example  sty.renderfunc.eightbit_fg(0)
fg.li_red     Example   Example  sty.renderfunc.sgr(91)
fg.red        Example   Example  sty.renderfunc.sgr(31)
fg.da_red     Example   Example  sty.renderfunc.eightbit_fg(88)
fg.li_green   Example   Example  sty.renderfunc.sgr(92)
fg.green      Example   Example  sty.renderfunc.sgr(32)
fg.da_green   Example   Example  sty.renderfunc.eightbit_fg(22)
fg.li_yellow  Example   Example  sty.renderfunc.sgr(93)
fg.yellow     Example   Example  sty.renderfunc.sgr(33)
fg.da_yellow  Example   Example  sty.renderfunc.eightbit_fg(58)
fg.li_blue    Example   Example  sty.renderfunc.sgr(94)
fg.blue       Example   Example  sty.renderfunc.sgr(34)
fg.da_blue    Example   Example  sty.renderfunc.eightbit_fg(18)
fg.li_magenta Example   Example  sty.renderfunc.sgr(95)
fg.magenta    Example   Example  sty.renderfunc.sgr(35)
fg.da_magenta Example   Example  sty.renderfunc.eightbit_fg(89)
fg.li_cyan    Example   Example  sty.renderfunc.sgr(96)
fg.cyan       Example   Example  sty.renderfunc.sgr(36)
fg.da_cyan    Example   Example  sty.renderfunc.eightbit_fg(23)
fg.li_white   Example   Example  sty.renderfunc.sgr(97)
fg.white      Example   Example  sty.renderfunc.sgr(37)
fg.da_white   Example   Example  sty.renderfunc.eightbit_fg(249)
============= ========= ======== =======================================


.. _anchor_bg_register:

Background
----------

.. rst-class:: table-color-bg

============= ========= ======== =======================================
Attribute     Ex. Light Ex. Dark Default Renderer
============= ========= ======== =======================================
bg.li_black   Example   Example  sty.renderfunc.sgr(90)
bg.black      Example   Example  sty.renderfunc.sgr(30)
bg.da_black   Example   Example  sty.renderfunc.eightbit_bg(0)
bg.li_red     Example   Example  sty.renderfunc.sgr(91)
bg.red        Example   Example  sty.renderfunc.sgr(31)
bg.da_red     Example   Example  sty.renderfunc.eightbit_bg(88)
bg.li_green   Example   Example  sty.renderfunc.sgr(92)
bg.green      Example   Example  sty.renderfunc.sgr(32)
bg.da_green   Example   Example  sty.renderfunc.eightbit_bg(22)
bg.li_yellow  Example   Example  sty.renderfunc.sgr(93)
bg.yellow     Example   Example  sty.renderfunc.sgr(33)
bg.da_yellow  Example   Example  sty.renderfunc.eightbit_bg(58)
bg.li_blue    Example   Example  sty.renderfunc.sgr(94)
bg.blue       Example   Example  sty.renderfunc.sgr(34)
bg.da_blue    Example   Example  sty.renderfunc.eightbit_bg(18)
bg.li_magenta Example   Example  sty.renderfunc.sgr(95)
bg.magenta    Example   Example  sty.renderfunc.sgr(35)
bg.da_magenta Example   Example  sty.renderfunc.eightbit_bg(89)
bg.li_cyan    Example   Example  sty.renderfunc.sgr(96)
bg.cyan       Example   Example  sty.renderfunc.sgr(36)
bg.da_cyan    Example   Example  sty.renderfunc.eightbit_bg(23)
bg.li_white   Example   Example  sty.renderfunc.sgr(97)
bg.white      Example   Example  sty.renderfunc.sgr(37)
bg.da_white   Example   Example  sty.renderfunc.eightbit_bg(249)
============= ========= ======== =======================================



Coloring by name
~~~~~~~~~~~~~~~~

.. literalinclude:: ../../sty/tests/docs/coloring.py
   :language: py
   :start-after: Example("coloring by name")
   :end-before: # ===== End

.. image:: ../../assets/color_by_name.png
   :alt: coloring by name


Coloring with 8-bit codes
~~~~~~~~~~~~~~~~~~~~~~~~~

Link:
`wikipedia:8bit <https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit>`__

.. literalinclude:: ../../sty/tests/docs/coloring.py
   :language: py
   :start-after: Example("coloring by 8bit number")
   :end-before: # ===== End

.. image:: ../../assets/8bit.png
   :alt: coloring by 8bit number


Coloring with 24bit codes
~~~~~~~~~~~~~~~~~~~~~~~~~

Link:
`wikipedia:24bit <https://en.wikipedia.org/wiki/ANSI_escape_code#24-bit>`__

.. literalinclude:: ../../sty/tests/docs/coloring.py
   :language: py
   :start-after: Example("coloring by 24bit rgb number")
   :end-before: # ===== End

.. image:: ../../assets/24bit.png
   :alt: coloring by 24bit number




