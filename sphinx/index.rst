

.. meta::
   :description: String styling for your terminal
   :keywords: sty, python, terminal, style, colors, coloring
   :author: Felix Meyer-Wolters


.. image:: ../assets/logo_readme.png
   :alt: charts


|

Description
===========

------------

Simple, flexible and extensible string styling for your terminal.
Supports 3/4bit, 8bit and 24bit (truecolor, rgb) colors. Should work on most
Unix platfroms with most terminals. Works with recent Windows terminals. Window
legacy terminal (cmd) needs a `shim <https://github.com/feluxe/sty/issues/2#issuecomment-501890699>`__ to work.


Sty comes with default color palettes and renderers, but you can easily
replace/customize them, without touching the markup.

Sty's goal is to provide Python with a little string styling markup, which
is decoupled from color palettes and terminal implementations.

Sty has no dependencies.

If you run into compatibility problems with sty, please file an `issue <https://github.com/feluxe/sty/issues>`__!


Code Example
============

------------

.. literalinclude:: ../sty/tests/docs/getting_started.py
   :language: py
   :start-after: Example("gettings started: sty all the strings")
   :end-before: # ===== End

The code above will print like this in the terminal:

.. image:: ../assets/example_so.png
   :alt: example usage


Demo
====

------------

.. image:: ../assets/charts.png
   :alt: charts


Contents
========

------------

.. toctree::
   :maxdepth: 1
   :titlesonly:
   :caption: Source Files (github):

   Code Repo <https://github.com/feluxe/sty>
   Docs Repo <https://github.com/feluxe/sty-docs>


.. toctree::
   :maxdepth: 1
   :titlesonly:
   :caption: Introduction:

   intro/requirements.rst
   intro/install.rst
   intro/getting_started.rst



.. toctree::
   :maxdepth: 1
   :caption: Documentation:

   docs/effects.rst
   docs/coloring.rst
   docs/resetting.rst
   docs/muting.rst
   docs/customizing.rst
   docs/exporting.rst
   docs/developing_testing.rst
   docs/known_issues.rst



