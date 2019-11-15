

Exporting / Copying
===================


``as_dict`` method
~~~~~~~~~~~~~~~~~~

.. automethod:: sty.Register.as_dict

**Example:**

.. literalinclude:: ../../sty/tests/docs/exporting.py
   :language: py
   :start-after: Example("as dict")
   :end-before: # ===== End



``as_namedtuple`` method
~~~~~~~~~~~~~~~~~~~~~~~~

.. automethod:: sty.Register.as_namedtuple

**Example:**

.. literalinclude:: ../../sty/tests/docs/exporting.py
   :language: py
   :start-after: Example("as namedtuple")
   :end-before: # ===== End


.. _copy_method:

``copy`` method
~~~~~~~~~~~~~~~

The copy method allows you to create deep copies of register-objects. This can
be very useful in case you don't want to mess with sty's *global*
register-classes (sty.fg., sty.bg, sty.ef, sty.rs).

.. automethod:: sty.Register.copy

**Example:**

.. literalinclude:: ../../sty/tests/docs/exporting.py
   :language: py
   :start-after: Example("copy")
   :end-before: # ===== End

