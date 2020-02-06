Getting Started
===============

You can import sty like this:

.. code:: python

   import sty

However, if you need to style a lot of stuff, you might consider
importing the register-objects directly, like this:

.. code:: python

   from sty import fg, bg, ef, rs


*Sty* all the strings!
----------------------

.. literalinclude:: ../../sty/tests/docs/getting_started.py
   :language: py
   :start-after: Example("gettings started: sty all the strings")
   :end-before: # ===== End

The code above will print like this in the terminal:

.. image:: ../../assets/example_so.png
   :alt: example usage



A quick look at the primitives:
-------------------------------

sty provides a bunch of tiny, but flexible primitives (called register-objects)
that can be used to style your strings:

* ``ef`` (:ref:`effect-register <anchor_effect_register>`)
* ``fg`` (:ref:`foreground-register <anchor_fg_register>`)
* ``bg`` (:ref:`background-register <anchor_bg_register>`)
* ``rs`` (:ref:`reset-register <anchor_reset_register>`)

Each register-object carries a default selection of attributes, which you can
select like this:


.. code:: python

   ef.italic
   fg.blue
   bg.green
   rs.all

Or like this, which is nice in case you need to dynamically select
attributes:

.. literalinclude:: ../../sty/tests/docs/getting_started.py
   :language: py
   :start-after: Example("gettings started: select dynamically")
   :end-before: # ===== End

``fg`` and ``bg`` are special in the way that they allow you to select
8bit and 24bit colors directly:

.. literalinclude:: ../../sty/tests/docs/getting_started.py
   :language: py
   :start-after: Example("gettings started: select 8bit and 24bit directly")
   :end-before: # ===== End

I think this is all you need to know to get going. Check out the
documentation or the codebase for more detail or feel free to create an
issue and ask. Have fun! :D


