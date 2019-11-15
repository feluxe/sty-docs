
Muting
======

.. CAUTION::

   If you use sty for a *library* that is shared among other projects, I highly
   suggest not to mute the "global" register-objects (sty.fg,
   sty.bg, sty.ef, sty.rs) directly, because that might cause conflicts
   with other packages that share the same sty dependency.

   If you want to mute sty's register-obejcts in a *library* you should either:

   * Use the :ref:`copy method <copy_method>` to create copies of them, which
     you can mute safely.
   * :ref:`Create custom register-classes <Extending register-classes and creating new instances>`
     and create new register-objects from them, which you can mute safely.



The ``mute`` and ``unmute`` methods
-----------------------------------

.. automethod:: sty.Register.mute
.. automethod:: sty.Register.unmute

**Example:**

.. literalinclude:: ../../sty/tests/docs/muting.py
   :language: py
   :start-after: Example("mute formatting")
   :end-before: # ===== End



The ``mute`` and ``unmute`` batch functions
-------------------------------------------

.. autofunction:: sty.mute
.. autofunction:: sty.unmute

**Example:**

.. literalinclude:: ../../sty/tests/docs/muting.py
   :language: py
   :start-after: Example("mute formatting batch")
   :end-before: # ===== End

