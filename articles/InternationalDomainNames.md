<!--
.. title: International Domain Names
.. slug: InternationalDomainNames
.. date: 2017-03-31
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

These days, domain names aren't restricted to being ASCII-only.  For example,
let's imagine that we at PythonAnywhere wanted to open a branch in China, and
call it 蟒蛇云端.  In the past, because domain names had to be in ASCII, we
would have been stuck with something like mangsheyunduan.cn as a domain name,
which would be hard for people to understand and remember.

Nowadays, you can use Unicode for domain names -- so we could get 蟒蛇云端.cn
and use it.  But the underlying DNS system still uses ASCII; the trick used
under the hood is the International Domain Name, or IDN, system.  IDNs work by mapping
non-ASCII characters into strings of standard seven-bit ASCII ones.  If you
register 蟒蛇云端.cn, what you're actually registering is the IDN equivalent,
which is xn--9kqp59h3ohr4a.cn.  [Verisign have a converter page](http://mct.verisign-grs.com/)
that allows you to find out the IDN equivalent of an non-ASCII domain, and
vice versa.

So let's say you've bought 蟒蛇云端.cn, and want to set up a website at
`http://www.蟒蛇云端.cn/` on PythonAnywhere.  All you need to do is go to the
"Web" tab, create a new website using the IDN version of the domain, "www.xn--9kqp59h3ohr4a.cn",
and then proceed as normal.  Once it's created, you'll get the value you
need to provide for a CNAME with your registrar, and you're all set!  When
people type www.蟒蛇云端.cn into their browser, they'll see your site.


