
Effects
=======

Sty uses ANSI SGR parameters to apply effects. More about ANSI Select Graphic Rendition (SGR) on wikipedia:
`ANSI SGR <https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_parameters>`__


.. _anchor_effect_register:

Sty's default effect register
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are the default attributes for the ``sty.ef`` register-object.

.. rst-class:: table-register

=================== ============================ =====================
Attribute           Description                  Default Renderer
=================== ============================ =====================
ef.bold (alias b)   Bold or increased intensity  sgr(1)
ef.dim              Decreased intensity          sgr(2)
ef.italic (alias i) Italic..                     sgr(3)
ef.underl (alias u) Underline..                  sgr(4)
ef.blink            Blink..                      sgr(5)
ef.inverse          Inverse fore- and background sgr(7)
ef.hidden           Conceal/Hide                 sgr(8)
ef.strike           Strike-through               sgr(9)
ef.rs               Reset effects                sgr(22), sgr(23), sgr(24), sgr(25), sgr(27), sgr(28), sgr(29)
=================== ============================ =====================


Italic
~~~~~~

.. literalinclude:: ../../sty/tests/docs/effects.py
   :language: py
   :start-after: Example("italic")
   :end-before: # ===== End

.. image:: ../../assets/italic.png
   :alt: italic example


Bold
~~~~

.. literalinclude:: ../../sty/tests/docs/effects.py
   :language: py
   :start-after: Example("bold")
   :end-before: # ===== End

.. image:: ../../assets/bold.png
   :alt: bold example


Underline
~~~~~~~~~

.. literalinclude:: ../../sty/tests/docs/effects.py
   :language: py
   :start-after: Example("underline")
   :end-before: # ===== End

.. image:: ../../assets/underline.png
   :alt: underline example


TODO:
~~~~~

Add examples for strike, blink, etc..

