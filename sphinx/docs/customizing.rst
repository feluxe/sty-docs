
Customizing
===========

Sty allows you to change or to extend the default registers as you like.
You can also create a complete new register. More on these things in the
following chapters.


.. CAUTION::

   If you use sty for a *library* that is shared among other projects, I highly
   suggest not to customize the "global" register-objects (sty.fg ,sty.bg,
   sty.ef, sty.rs) directly, because that might cause conflicts
   with other packages that share the same sty dependency.

   If you want to customize sty's register-objects in a *library* you should
   either:

   * Use the :ref:`copy method <copy_method>` to create copies of them, which
     you can customize safely.
   * :ref:`Create custom register-classes <Extending register-classes and creating new instances>`
     and create new customized register-objects from them.



Add custom styles to a register-object
--------------------------------------

In order to add new or update existing styles for a register-object, you can simply assing a new styling rule to an attribute:

**Example:**

.. literalinclude:: ../../sty/tests/docs/customizing.py
   :language: py
   :start-after: Example("customizing the register-objects: assignment")
   :end-before: # ===== End

There are multiple :ref:`Render Types` that you can use to define different styles.

The ``Style()`` type allows you to compose styles from multiple new rules, as well as from existing register-objects:

.. literalinclude:: ../../sty/tests/docs/customizing.py
   :language: py
   :start-after: Example("customizing the register-objects: compose")
   :end-before: # ===== End


Render Types
------------

These are the render-types, which you can use to create custom styles:

.. autoclass:: sty.Sgr
.. autoclass:: sty.EightbitFg
.. autoclass:: sty.EightbitBg
.. autoclass:: sty.RgbFg
.. autoclass:: sty.RgbBg



Changing the render-functions for a register-obejct
---------------------------------------------------

If you want to fix compatibility issues with old terminals, you might want to customize the render-functions.

.. automethod:: sty.Register.set_renderfunc

**Example:**

.. literalinclude:: ../../sty/tests/docs/customizing.py
   :language: py
   :start-after: Example("customizing the register-objects: render-func")
   :end-before: # ===== End


Changing the ``__call__`` behaviour for a register-object
---------------------------------------------------------

Remember that you can call the register-objects like a function? You can change the behaviour for such calls.

.. automethod:: sty.Register.set_eightbit_call
.. automethod:: sty.Register.set_rgb_call

**Example**:

.. literalinclude:: ../../sty/tests/docs/customizing.py
   :language: py
   :start-after: Example("customizing the register-objects: calls")
   :end-before: # ===== End



Extending register-classes and creating new instances
-----------------------------------------------------

If you want to create a large register of custom styles, it may be convenient
to extend the default register-classes and create new register-objects from them.

Customizing sty this way has some advantages:

* You get better editor support (auto-completion, mypy, pylint, etc) for the register-objects.
* You aren't mutating sty's *global* register-objects (``sty.ef``, ``sty.fg``, etc.).
  This is important for library projects to prevent conflicts with other packages that use sty.

.. literalinclude:: ../../sty/tests/docs/customizing.py
   :language: py
   :start-after: Example("extending register-classes")
   :end-before: # ===== End


A register-class from scratch
-----------------------------

This example show how to create a complete register class from scratch, including custom render-functions:

.. literalinclude:: ../../sty/tests/docs/customizing.py
   :language: py
   :start-after: Example("register-class from scratch")
   :end-before: # ===== End

This is exactly how sty's default register-classes are created.


