djangocms-demo
==============


Sample website for demos.

Created for internal use, so it may have rough edges and it totally lacks
documentation.

Do not use as a base for your own projects, check
https://github.com/nephila/aldryn-installer instead.

Created for the DjangoBeer event, in Florence: http://djangobeer.com


Caveats
=======

When adding apphooks, you **must** provide the namespace in the advanced settings:

 * News Apphook: namespace **news**
 * Polls Apphook: namespace **polls**
 * TransNews Apphook: namespace **transnews**
